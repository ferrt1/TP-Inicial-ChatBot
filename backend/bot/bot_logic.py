from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.database import User, db
from flask import session
import numpy as np
import pandas as pd

# lee los datos de entrenamiento desde un archivo .csv
data = pd.read_csv('./bot/data.csv', delimiter=';')

# prepara los datos
questions, answers = data['questions'], data['answers']
vectorizer = TfidfVectorizer().fit(questions)

def get_bot_response(user_message):
    user_vector = vectorizer.transform([user_message])

    similarities = cosine_similarity(user_vector, vectorizer.transform(questions))

    closest_index = np.argmax(similarities)
    max_similarity = np.max(similarities)

    if max_similarity < 0.7:
        bot_message = "Disculpa, no comprendo a lo que te refieres. Recuerda que soy un bot para contestar tus preguntas en torno a internet y telefonía de UNGSNet. Si tienes preguntas puedes escribir 'opciones' y te diré las opciones que puedes escoger."
    else:
        bot_message = answers[closest_index]

    bot_message = bot_message.replace('"', '')

    return bot_message

def handle_name_request(user, user_message):
    user.first_name = user_message
    db.session.commit()
    session['asking_for_name'] = False
    session['asking_for_last_name'] = True
    return 'Gracias, ahora puedes decirme tu apellido'

def handle_last_name_request(user, user_message):
    user.last_name = user_message
    db.session.commit()
    session['asking_for_last_name'] = False
    user.first_visit_complete = True  # Marca la primera visita como completa
    db.session.commit()
    return 'Muchas Gracias, ¿En qué te puedo ayudar? Prueba escribiendo opciones'

def handle_first_visit():
    session['asking_for_name'] = True
    return 'Veo que es tu primera vez por aquí, puedes decirme tu nombre'

def handle_plan_request(user, user_message):
    valid_plans = ['plan base', 'base', 'plan premium', 'premium', 'plan exclusive', 'exclusive']

    if user_message.lower() not in valid_plans:
        return 'No entendí, prueba escribiendo una de estas opciones: plan base, base, plan premium, premium, plan exclusive, exclusive'
     
    if user_message.lower() in ['plan base', 'base']:
        user.plan = 'base'
    elif user_message.lower() in ['plan premium', 'premium']:
        user.plan = 'premium'
    elif user_message.lower() in ['plan exclusive', 'exclusive']:
        user.plan = 'exclusive'

    db.session.commit()
    session['asking_for_plan'] = False
    return 'Gracias, tu plan ha sido registrado. Ahora sí puedes ver opciones 😃'


def handle_plan(user):
    if user.plan == None:
        session['asking_for_plan'] = True
        return 'Hola, veo que aún no agregaste tu plan. Por favor, elige cuál posees: <br> Plan base: 25MB por $10000 al mes <br> Plan premium: 50MB por $15000 al mes <br> Plan exclusive: 100MB por $20000 al mes'
    
    if user.plan == 'base':
        factura = 10000
    elif user.plan == 'premium':
        factura = 15000
    elif user.plan == 'exclusive':
        factura = 20000

    return f'Hola {user.first_name}. Tu factura es de: <strong> ${factura} 😃 </strong>. Nos alegra ayudarte!'
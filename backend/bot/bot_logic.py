from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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



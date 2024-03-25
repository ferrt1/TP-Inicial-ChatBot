from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

# lee los datos de entrenamiento desde un archivo .csv
data = pd.read_csv('data.csv')

# prepara los datos
questions, answers = data['questions'], data['answers']
vectorizer = TfidfVectorizer().fit(questions)

def get_bot_response(user_message):
    user_vector = vectorizer.transform([user_message])

    similarities = cosine_similarity(user_vector, vectorizer.transform(questions))

    closest_index = np.argmax(similarities)
    bot_message = answers[closest_index]

    return bot_message

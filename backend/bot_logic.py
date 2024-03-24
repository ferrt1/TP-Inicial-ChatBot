from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# datos de entrenamiento
data = [
    ("Hola", "¡Hola! Soy un bot de UNGSNet, estoy aquí tus consultas."),
    ("¿Cómo reinicio mi router?", "Para reiniciar tu router, busca el botón de reinicio en el dispositivo. Puede ser necesario utilizar un objeto puntiagudo para presionarlo. Mantén presionado el botón durante unos 10 segundos y luego suéltalo. El router debería reiniciarse automáticamente."),
    ("No puedo conectarme a la red", "Lo siento por los problemas que estás experimentando. Aquí hay algunas cosas que puedes probar: 1. Asegúrate de que tu dispositivo esté dentro del rango de la red. 2. Comprueba si otros dispositivos pueden conectarse a la red. 3. Reinicia tu dispositivo y tu router. 4. Si el problema persiste, puede ser necesario ponerse en contacto con tu proveedor de servicios de Internet."),
    ("¿Cómo cambio mi contraseña de wifi?", "Para cambiar tu contraseña de Wi-Fi, necesitarás acceder a la configuración de tu router. La dirección IP para acceder a la configuración del router suele estar impresa en el router mismo. Una vez que hayas accedido a la configuración del router, busca la sección de seguridad o de Wi-Fi para cambiar la contraseña."),
]

# prepara los datos
questions, answers = zip(*data)
vectorizer = TfidfVectorizer().fit(questions)

def get_bot_response(user_message):
    user_vector = vectorizer.transform([user_message])

    similarities = cosine_similarity(user_vector, vectorizer.transform(questions))

    closest_index = np.argmax(similarities)
    bot_message = answers[closest_index]

    return bot_message

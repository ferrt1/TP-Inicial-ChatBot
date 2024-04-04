# Laboratorio de Construcción de Software - TP-Inicial-ChatBot

*Por: Flavio Ybarra flavio_712@hotmail.com, Ivan Sanchez ivansncz11@gmail.com, Fernando Trejo fernandotrejo125@gmail.com*

---

## Introducción

###  ¿Qué es la IA y cuál es su aplicación en diferentes procesos de la vida diaria, a nivel personal, profesional y empresarial?
La Inteligencia Artificial (IA) se refiere a sistemas informáticos capaces de realizar tareas complejas que históricamente solo podían ser realizadas por seres humanos. Estas tareas incluyen el razonamiento, la toma de decisiones y la resolución de problemas, por ejemplo la comunicación en línea con los clientes o jugar al ajedrez.

Su aplicación puede verse en diferentes procesos de la vida:
- A nivel personal la IA puede servir dando asistentes virtuales como Siri o Alexa, en aplicaciones como Google Maps que utilizan IA para calcular mejores rutas, recomendaciones a nivel gustos personales de cada uno por ejemplo en Netflix.
- A nivel profesional se puede utilizar para automatizar tareas, procesos, analizar datos.
- A nivel empresarial es usada para el Marketing, recursos humanos o automatización industrial, por ejemplo robótica.


### ¿Qué es el onboarding?

El onboarding digital se refiere al proceso de incorporación de nuevos usuarios o clientes a una plataforma, servicio o aplicación de manera digital. Este proceso es utilizado por las empresas que ofrecen productos o servicios en línea. El objetivo del onboarding es facilitar la introducción y adopción de los usuarios a una nueva herramienta o plataforma, asegurándose de que aprendan a utilizarla de manera efectiva. Esto se puede lograr guiando a los usuarios a través de las funciones clave y ofreciendo tutoriales interactivos. Con la ayuda de chatbots e Inteligencia Artificial, se pueden acelerar muchos de estos procesos, como por ejemplo:
- Asistencia en tiempo real para los usuarios.
- Análisis de datos para evaluar el rendimiento del onboarding.
- Automatización de tareas repetitivas.
- Recopilación de feedback.
- Si la plataforma o servicio utiliza múltiples sistemas, se puede usar la Inteligencia Artificial o un chatbot para facilitar la integración a dichos sistemas.

### Análisis de un documento de identidad
El análisis de un documento de identidad en el proceso de onboarding digital implica varios pasos para verificar la autenticidad del documento y confirmar la identidad del usuario de manera segura. Este proceso contribuye a garantizar la seguridad y confiabilidad de los servicios en línea para los usuarios y las empresas.
Estos son algunos de los pasos más comunes que se suelen seguir:

- Captura de la imagen del documento:
El usuario proporciona una imagen clara y legible de su documento de identidad, ya sea mediante la cámara de un dispositivo móvil o cargándola desde un archivo digital.

- Extracción de datos:
Se utiliza software de reconocimiento óptico de caracteres (OCR) para extraer los datos relevantes del documento, como el nombre del titular, la fecha de nacimiento, el número de identificación y la fecha de vencimiento.

- Verificación de la autenticidad del documento:
Empleando tecnología que incluye la lectura de códigos MRZ (Machine Readable Zone) se realizan verificaciones automáticas para determinar la autenticidad del documento. Esto puede incluir la detección de características de seguridad como marcas de agua, hologramas, microtextos y otros elementos de seguridad.

- Comparación de la imagen con el usuario:
Una de las formas más seguras de confirmar la identidad es a través de la verificación biométrica. Esta puede incluir el reconocimiento facial, la comparación de huellas digitales o el escaneo del iris, preferentemente realizada en tiempo real para confirmar que la persona presente durante el Onbording es la misma del documento.

- Comprobación en listas de AML (Anti Money Laundering):
Se realizan verificaciones en listas de AML para asegurarse de que el titular del documento no esté en ninguna lista de sanciones o restricciones.

- Análisis de riesgos:
Se pueden llevar a cabo análisis adicionales para evaluar el riesgo de fraude o actividad delictiva basada en la información proporcionada y el comportamiento del usuario durante el proceso de registro.

- Registro seguro de datos:
Todos los datos del documento de identidad y la información asociada se registran de forma segura y se utilizan solo para los fines previstos, en cumplimiento de las regulaciones de privacidad y protección de datos.

### Biometría
la biometría desempeña un papel importante en el proceso de onboarding digital al proporcionar una forma segura y conveniente de verificar la identidad de los usuarios, proteger datos sensibles y mejorar la experiencia del usuario.
Estas son algunas formas en que la biometría puede integrarse en el proceso de onboarding:

- Verificación de identidad:
La biometría puede utilizarse para verificar la identidad de los usuarios durante el proceso de registro. Esto puede incluir la autenticación biométrica basada en características físicas únicas, como el reconocimiento facial, el reconocimiento de voz, la huella dactilar o el escaneo de iris.

- Seguridad en el acceso:
Una vez que los usuarios han creado una cuenta, la biometría puede utilizarse para mejorar la seguridad en el acceso a la plataforma. Por ejemplo, los usuarios pueden utilizar la autenticación biométrica en lugar de contraseñas tradicionales para iniciar sesión en sus cuentas, lo que reduce el riesgo de acceso no autorizado.

- Protección de datos sensibles:
La biometría puede utilizarse para proteger datos sensibles almacenados en la plataforma, como información financiera o médica. La autenticación biométrica puede asegurar que solo los usuarios autorizados tengan acceso a estos datos, proporcionando una capa adicional de seguridad.

- Prevención de fraudes:
La biometría puede ayudar a prevenir el fraude durante el proceso de onboarding al detectar intentos de suplantación de identidad. Los sistemas biométricos pueden identificar patrones y comportamientos sospechosos y alertar a los administradores de la plataforma para que tomen medidas adecuadas.

- Experiencia del usuario: 
Además de mejorar la seguridad, la biometría también puede mejorar la experiencia del usuario al eliminar la necesidad de recordar contraseñas complicadas o realizar múltiples pasos de autenticación. Los usuarios pueden encontrar más conveniente y rápido utilizar la autenticación biométrica para acceder a sus cuentas.

### Listas AML (Anti Money laundering)
También existe la posibilidad de contrastar la identidad extraída con listados de control Anti Money Laundering o AML checks que permitan comprobar que la persona que está llevando a cabo el proceso de registro o verificación digital no esta inmersa en actividades fraudulentas como :
  * Fraude de identidad
  *  Blanqueo de capitales
  *  Financiacion del terrorismo
  * Persona bajo sanciones económicas
  * Personas expuestas políticamente

### Normativas Existentes

En la argentina como normativa que debemos tener en cuenta a la hora de desarrollar un sistema de inteligencia artificial es respetar la ley de protección de datos personales (ley nacional no.25.326/2000 y decreto ejecutivo presidencial no. 1558/2001), además el gobierno nos presenta aspectos éticos que debemos  tener en cuenta con estos sistemas. Para saber más sobre estos aspectos puede visitar este enlace
https://www.argentina.gob.ar/justicia/derechofacil/leysimple/educacion-ciencia-cultura/recomendaciones-para-el-uso-de

En Europa el Reglamento  es mucho más estricto ya que fija una serie de obligaciones para la IA en función de sus riesgos potenciales , su nivel de impacto y una categorización hacia estos sistemas. a continuación se presentarán algunas de estas  normativas

#### Aplicaciones prohibidas:

Prohíben ciertas aplicaciones de inteligencia artificial que atentan contra los derechos de la ciudadanía, como los sistemas de categorización biométrica basados en características sensibles y la captura indiscriminada de imágenes faciales de internet o grabaciones de cámaras de vigilancia para crear bases de datos de reconocimiento facial. 

#### Obligaciones para los sistemas de alto riesgo:

También se prevén obligaciones claras para otros sistemas de IA de alto riesgo (debido a que pueden ser muy perjudiciales para la salud, la seguridad, los derechos fundamentales, el medio ambiente, la democracia y el Estado de derecho). Algunos ejemplos de usos de alto riesgo de la IA son las infraestructuras críticas, la educación y la formación profesional, el empleo, los servicios públicos y privados esenciales (por ejemplo, la sanidad o la banca). Estos sistemas deben evaluar y reducir los riesgos, mantener registros de uso, ser transparentes y precisos y contar con supervisión humana.

#### Requisitos de transparencia 

Los sistemas de IA de uso general y los modelos en los que se basan deben cumplir ciertos requisitos de transparencia, respetar la legislación de la UE sobre derechos de autor y publicar resúmenes detallados del contenido usado para entrenar sus modelos. 

para mas informacion :
https://www.europarl.europa.eu/news/es/press-room/20231206IPR15699/artificial-intelligence-act-deal-on-comprehensive-rules-for-trustworthy-ai

---

## Implementación
Crearemos un chatbot para compañías telefónicas e internet utilizando la API de Telegram, el BotFather y Python. Estamos evaluando diferentes opciones para el hosting del chatbot. La combinación de estas herramientas nos permitirá tener una automatización para poder responder a consultas, brindar información sobre planes y servicios, y ayudar a los usuarios con sus necesidades de telefonía e internet. Python es un lenguaje versátil y ampliamente utilizado en el desarrollo de chatbots debido a su facilidad de uso y la gran cantidad de bibliotecas disponibles. El BotFather de Telegram nos permitirá crear y configurar nuestro bot, mientras que la API de Telegram nos proporcionará las funciones necesarias para interactuar con los usuarios. En cuanto al hosting, estamos considerando diferentes opciones según nuestras necesidades de escalabilidad, seguridad y costo. 


## Alcance
Es el desarrollo de un chatbot que permitirá a los clientes consultar sobre el centro de ayuda de la empresa respondiendo a preguntas típicas del servicio tales como las siguientes: “¿Cómo reinicio mi router?, No puedo conectarme a la red, ¿Cómo cambio mi contraseña de wifi?”, también se podrán registrar o iniciar sesión mediante huella digital. 
Lo siguiente quedaría fuera del proyecto o se podrán implementar en otras etapas de desarrollo:
* Cambios de servicios/planes.
* Pagos de servicios.
* Contratación de servicios.

## Documentación funcional:

### Requerimientos

En esta sección se detallarán las condiciones o capacidades que debe poseer el sistema a desarrollar con la finalidad de realizar un software que pueda solucionar el problema de nuestro cliente. La clasificación de los requerimientos se realiza en base a la importancia de cada requerimiento por eso están agrupados en:

1. Requerimiento funcional esencial (RFE): Lo utilizaremos para explicar que son requerimientos esenciales y que sin ellos el sistema no funcionaría para cumplir su cometido.
 
* Visualización del chatbot (RFE): El cliente debe poder visualizar el chatbot en la interfaz de la aplicación.
* Campo de entrada para texto (RFE): Debe haber un campo de entrada donde el cliente pueda escribir texto para interactuar con el chatbot. Este texto será enviado al chatbot al presionar un botón de “enviar” o al presionar la tecla “Enter”.
* Interacción con el chatbot (RFE): Se debe permitir la interacción del cliente con el chatbot a través de preguntas.
* Registro del cliente (RFE): Debe permitir al cliente registrarse en el sitio una vez que completa los campos de datos nombre, apellido, nro_telefono.
* Iniciar sesión mediante huella digital (RFE): El cliente podrá iniciar sesión mediante una lectura de huella digital.
  
2. Requerimiento no funcional (RFN): Lo utilizaremos para explicar que son los requerimientos que se enfocan en el diseño y que sin ellos el sistema puede seguir funcionando

* Disponibilidad de iniciar conversación con el chatbot en cualquier momento (RFN): El chatbot debe estar disponible 24/7 para que los clientes puedan iniciar una conversación en cualquier momento.
* El sistema debe ser fácil de usar y comprender (RFN): La interfaz de usuario debe ser intuitiva y amigable, permitiendo a los usuarios navegar y utilizar el chatbot sin dificultades.
* El sistema debe poder tener acceso en dispositivos móviles como de escritorio (RFN): El chatbot debe ser responsivo y compatible con diferentes tamaños de pantalla y sistemas operativos para garantizar una experiencia de usuario óptima en cualquier dispositivo.
* El tiempo de respuesta tendrá que ser eficaz (RFN): El chatbot debe ser capaz de procesar las consultas de los usuarios y proporcionar respuestas en un tiempo razonable.

## Documentación técnica

### Tecnologías Utilizadas

* Python: Lenguaje de programación utilizado para el backend.
* Flask: Framework de Python utilizado para crear la aplicación web.
* scikit-learn: Biblioteca de Machine Learning utilizada para entrenar el modelo del chatbot.
* HTML/CSS/JS: Lenguajes utilizados para la interfaz de usuario del chatbot.


### Estructura del código

#### bot_logic.py 

``` python

# lee los datos de entrenamiento desde un archivo .csv
data = pd.read_csv('data.csv')

# prepara los datos 
questions, answers = data['questions'], data['answers']
vectorizer = TfidfVectorizer().fit(questions)

```

Para que el chatbot responda las consultas de los clientes, primero hay que entrenarlo. Para hacer eso lo que se hizo fue adjuntar las posibles preguntas que hiciera el usuario con su correspondiente respuesta todo esto en un documento csv ("comma-separated values"). Luego le inyectamos ese documento en un vectorizador, aca estariamos haciendo como que aprenda vocabulario en la cual en la matriz que se va a formar estarian las palabras con mas frecuencia y la lineas del documento que agregamos.


``` python
def get_bot_response(user_message):
    user_vector = vectorizer.transform([user_message])

    similarities = cosine_similarity(user_vector, vectorizer.transform(questions))

    closest_index = np.argmax(similarities)
    bot_message = answers[closest_index]

    bot_message = bot_message.replace('"', '')

    return bot_message

```

Para la interpretacion de los mensajes recibidos por el chatbot lo que hace es transformar el mensaje en un vector (tal y como se explica antes) , luego se empiezan empieza a calcular la similitudes entre la matriz del mensaje del usuario con la matriz de las preguntas que almacenamos este calculo indicara al chatbot que es lo que tiene que responder.

#### app.py 

Este código define la aplicación web y las rutas para servir archivos estáticos y la ruta /bot para las solicitudes POST del chatbot.

#### HTML y Javascript

Este código define la interfaz de usuario del chatbot y la lógica para enviar las preguntas del usuario al servidor y mostrar las respuestas del bot.

---

### Entrega 3 05/04

#### Login Huella Digital

Login con huella digital : Para el login con huella digital lo que se hace es utilizar un autenticador web (WebAuthn) que permite  que en lugar de la contraseña habitual, los usuarios podrán identificarse con datos biométricos, del tipo huella dactilar, hardware específico o aplicaciones específicas.

Este proceso consta de dos instancias : Registro y Autenticación

##### Registro
el servidor debe proporcionar Opciones de creación de claves de acceso junto con un challenge único que se pasa a la API WebAuthn en el navegador. El usuario selecciona entre los autenticadores disponibles que cumplen con los requisitos de las opciones  de la organizacion, autoriza la acción y luego la respuesta se envía de vuelta a la organizacion para su validación y almacenamiento.

![Screenshot_9](https://github.com/ferrt1/TP-Inicial-ChatBot/assets/83597336/6ed814b5-e236-47ca-94a8-586e2fbd431f)

0. **Inicio de la solicitud:** El cliente inicia una solicitud para registrar un autenticador con el nombre de usuario (en este caso, el correo electrónico). Esta solicitud se realiza a través de una llamada a la API WebAuthn en el navegador del cliente.
1. **Creación de la instancia de la credencial:** La organización (UNGSNet) crea una instancia de la credencial y la devuelve al cliente. Esta instancia contiene información sobre el usuario, el RP (Relying Party, es decir, la organización) y el tipo de credencial deseada. Esta información se utiliza para crear una solicitud de registro que se envía a la API WebAuthn.
2. **Validación del ID de la organización:** El navegador del cliente valida el ID de la organización con el origen y aplica un hash a los datos del cliente. Este paso es crucial para garantizar que la solicitud proviene de una fuente confiable.
3. **Consentimiento del usuario y creación de las claves:** Antes de continuar, el autenticador solicitará algún tipo de consentimiento del usuario. Después de verificar el consentimiento, el autenticador creará un nuevo par de claves asimétricas y almacenará de forma segura la clave privada. Este paso se realiza dentro del dispositivo de autenticación y es transparente para el usuario y la organización.
4. **Devolución de la clave pública y otros datos:** La nueva clave pública, una identificación de credencial y otros datos de certificación se devuelven al navegador. Estos datos se empaquetan en un objeto PublicKeyCredential y se envían de vuelta a la organización.
5. **Finalización del registro:** La credencial de clave pública se devuelve al RP para finalizar el registro. La organización valida la firma y los datos de la credencial, y si todo es correcto, la credencial se almacena en el servidor para su uso en futuras autenticaciones.



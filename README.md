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
Crearemos un chatbot para compañías telefónicas e internet utilizando la API de Telegram, el BotFather y Python. Estamos evaluando diferentes opciones para el hosting del chatbot. La combinación de estas herramientas nos permitirá tener una automatización para poder responder a consultas, brindar información sobre planes y servicios, y ayudar a los usuarios con sus necesidades de telefonía e internet. Python es un lenguaje versátil y ampliamente utilizado en el desarrollo de chatbots debido a su facilidad de uso y la gran cantidad de bibliotecas disponibles. El BotFather de Telegram nos permitirá crear y configurar nuestro bot, mientras que la API de Telegram nos proporcionará las funciones necesarias para interactuar con los usuarios. En cuanto al hosting, estamos considerando diferentes opciones según nuestras necesidades de escalabilidad, seguridad y costo. ¡Estoy emocionado por este proyecto y espero que podamos crear un chatbot útil y eficiente


## Alcance
Es el desarrollo de un  chatbot que permitira a los clientes  consultar  sobre el centro de ayuda de la empresa respodiendo a preguntas tipicas del servicio tales como las siguientes :"¿Cómo reinicio mi router?,No puedo conectarme a la red,Cómo cambio mi contraseña de wifi" , tambien se podran registrar o iniciar sesion mediante huella digital.Lo siguiente quedaria afuera del proyecto o  se podran implementar en otras etapas de desarrollo.
cambios de servicios/planes.
pagos de servicios.
contratacion de servicios.

## Requerimientos
En esta sección se detallarán las condiciones o capacidades que debe poseer el sistema a desarrollar con la finalidad de realizar un software que pueda solucionar el problema de nuestro cliente asi satisfacerá sus necesidades. 
*Interraccion atravez de chatbot
*Registro del cliente
*Iniciar sesion mediante huella digital
*Disponibilidad de iniciar conversacion con el chatbot en cualquier momento
*El sistema debe ser fácil de usar y comprender
*No se deben guardar las imagenes de las huellas de datos en ninguna base de datos
*El sistema debe poder tener acceso en dispositivos moviles como de escritorio
*El tiempo de respuesta tendra que ser eficaz








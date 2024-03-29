from flask import Flask, request, send_from_directory, jsonify
from bot_logic import get_bot_response

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:labochatbot@localhost:3306/labochatbot'
db = SQLAlchemy(app)

# Define la tabla 'users'
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    mail =  db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)


@app.route('/chatbot')
def home():
    return send_from_directory('../frontend/', 'index.html')

@app.route('/')
def login_html():
    return send_from_directory('../frontend/', 'login.html')

# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    mail = data.get('mail')
    password = data.get('password')

    user = User(username=username, mail=mail, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado correctamente'})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    mail = data.get('mail')
    password = data.get('password')

    user = User.query.filter_by(mail=mail).first()

    if user and user.password == password:
        return send_from_directory('../frontend/', 'index.html')
    else:
        return jsonify({'message': 'Credenciales inválidas'})

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('../frontend/static/css', path)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('../frontend/static/images', path)

@app.route('/js/<path:path>')
def send_javascript(path):
    return send_from_directory('../frontend/static/js', path)

@app.route("/bot", methods=["POST"])
def bot_response():
    user_message = request.form["user_message"]
    bot_message = get_bot_response(user_message)
    return bot_message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

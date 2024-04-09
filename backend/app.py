from flask import Flask, request, send_from_directory, jsonify, session
from bot.bot_logic import get_bot_response, handle_name_request, handle_last_name_request, handle_first_visit
from auth.register import register_user, verify_registration
from auth.authentication import login_user, verify_authentication
from utils.database import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:labochatbot@localhost:3306/labochatbot'
app.config['SECRET_KEY'] = '123412az'
db.init_app(app)

@app.route("/user_id", methods=["GET"])
def get_user_id():
    user_id = session.get('user_id')
    return jsonify(user_id=user_id)

@app.route('/chatbot')
def home():
    user_id = request.cookies.get('user_id')
    if not user_id:
        return send_from_directory('../frontend/', 'error.html')
    return send_from_directory('../frontend/', 'index.html')

@app.route('/')
def login_html():
    return send_from_directory('../frontend/', 'login.html')

@app.route('/admin')
def admin_html():
    return send_from_directory('../frontend/', 'admin_panel.html')


@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    return register_user(email)

@app.route('/verify_registration', methods=['POST'])
def verify_reg():
    registration = session.get('registration')
    if registration is None:
        return jsonify({'status': 'failed', 'message': 'No registration in progress'}), 400

    email = registration['email']
    user_id = registration['user_id']
    client_response = request.json.get('response')

    return verify_registration(email, user_id, client_response)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_user(data)

@app.route('/verify_authentication', methods=['POST'])
def verify_auth():
    client_response = request.json.get('response')
    return verify_authentication(client_response)

@app.route("/bot", methods=["POST"])
def bot_response():
    user_message = request.form["user_message"]

    user_name = session.get('user_name')
    user = User.query.filter_by(email=user_name).first()

    if session.get('asking_for_name', False):
        return handle_name_request(user, user_message)

    elif session.get('asking_for_last_name', False):
        return handle_last_name_request(user, user_message)

    elif not user.first_visit_complete:  
        return handle_first_visit(user)

    else:
        bot_message = get_bot_response(user_message)
        return bot_message




@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('../frontend/static/css', path)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('../frontend/static/images', path)

@app.route('/js/<path:path>')
def send_javascript(path):
    return send_from_directory('../frontend/static/js', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, request, send_from_directory, jsonify, session
from bot_logic import get_bot_response
from flask_sqlalchemy import SQLAlchemy
from webauthn import generate_registration_options, options_to_json, verify_registration_response, generate_authentication_options, verify_authentication_response, base64url_to_bytes
from webauthn.helpers.structs import (
    AttestationConveyancePreference,
    UserVerificationRequirement,
    AuthenticationCredential,
    AuthenticatorAttachment,
    AuthenticatorSelectionCriteria,
    PublicKeyCredentialDescriptor,
    ResidentKeyRequirement,
    RegistrationCredential,
    PublicKeyCredentialType,
    AuthenticatorTransport
)

import secrets
import json
import base64
import os

RP_ID='f90a-2800-810-469-744-b890-f13-99c5-163.ngrok-free.app'
RP_NAME='UNGSNet'
UKEY_DEFAULT_BYTE_LEN = 20

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:labochatbot@localhost:3306/labochatbot'
app.config['SECRET_KEY'] = '123412az'
db = SQLAlchemy(app)

# Define la tabla 'users'
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email =  db.Column(db.String(45), unique=True, nullable=False)
    user_id = db.Column(db.LargeBinary, unique=True, nullable=False)
    credential_id = db.Column(db.LargeBinary, unique=True)
    public_key = db.Column(db.LargeBinary, unique=True)
    sign_count = db.Column(db.Integer)

@app.route('/chatbot')
def home():
    return send_from_directory('../frontend/', 'index.html')

@app.route('/')
def login_html():
    return send_from_directory('../frontend/', 'login.html')

def generate_challenge():
    return os.urandom(32)

# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'status': 'failed', 'message': 'El correo electrónico ya está registrado'}), 401

    challenge = generate_challenge()

    ukey_bytes = os.urandom(UKEY_DEFAULT_BYTE_LEN)
    ukey_base64 = base64.urlsafe_b64encode(ukey_bytes)	
    if not isinstance(ukey_base64, str):
        ukey_base64 = ukey_base64.decode('utf-8')
    ukey = ukey_base64

    new_user = User(email=email, user_id = ukey_bytes)
    db.session.add(new_user)
    db.session.commit()

    make_credential_options = generate_registration_options(
        rp_id=RP_ID,
        rp_name=RP_NAME,
        user_id=ukey_bytes,
        user_name=email,
        attestation=AttestationConveyancePreference.DIRECT,
        authenticator_selection=AuthenticatorSelectionCriteria(
            authenticator_attachment=AuthenticatorAttachment.PLATFORM,
            resident_key=ResidentKeyRequirement.DISCOURAGED,
        ),
        challenge=challenge,
        timeout=120000,
    )
    
    session['user_name'] = email

    return options_to_json(options=make_credential_options), 200


@app.route('/verify_registration', methods=['POST'])
def verify_registration():
    client_response = request.json.get('response')

    inner_response = client_response.get('response')
    client_data_json = inner_response.get('clientDataJSON')
    attestation_object = inner_response.get('attestationObject')
    expected_rp_id = client_response.get('rpId')
    expected_origin = client_response.get('origin')
    

    client_data_json_b64 = client_response.get('response').get('clientDataJSON')
    client_data_json_str = base64.urlsafe_b64decode(client_data_json_b64 + '==').decode()

    client_data_json_obj = json.loads(client_data_json_str)



    expected_challenge = base64url_to_bytes(client_data_json_obj.get('challenge'))
    expected_origin = client_data_json_obj.get('origin')

    credential = {
        'id': client_response.get('id'),
        'rawId': client_response.get('rawId'),
        'response': {
            'clientDataJSON': client_data_json,
            'attestationObject': attestation_object,
        },
        'type': "public-key"
    }
    
    webauthn_response = verify_registration_response(
        credential=credential,
        expected_challenge=expected_challenge,
        expected_rp_id='f90a-2800-810-469-744-b890-f13-99c5-163.ngrok-free.app',
        expected_origin=expected_origin,
        require_user_verification=True
    )

    user_name = session.get('user_name')

    user = User.query.filter_by(email=user_name).first()
    if user is None:
        return jsonify({'status': 'failed', 'message': 'User not found'})

    user.credential_id = webauthn_response.credential_id
    user.public_key = webauthn_response.credential_public_key
    user.sign_count = webauthn_response.sign_count

    db.session.commit()

    return jsonify({'status': 'ok'})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    challenge = generate_challenge()
    print(user.email)
    print(user.credential_id)

    if user:
            allow_credentials = [PublicKeyCredentialDescriptor(
                id=user.credential_id,
                type=PublicKeyCredentialType.PUBLIC_KEY,
                transports=[AuthenticatorTransport.USB, AuthenticatorTransport.NFC, 
                            AuthenticatorTransport.BLE, AuthenticatorTransport.INTERNAL,
                            AuthenticatorTransport.HYBRID],
            )]
            options = generate_authentication_options(
                    rp_id='f90a-2800-810-469-744-b890-f13-99c5-163.ngrok-free.app',
                    challenge=challenge,  
                    timeout=60000,
                    allow_credentials=allow_credentials,
                )
            return options_to_json(options=options), 200
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401



@app.route('/verify_authentication', methods=['POST'])
def verify_authentication():
   
    client_response = request.json.get('response')
    print(client_response)
  
    client_data_json_b64 = client_response.get('response').get('clientDataJSON')
    client_data_json_str = base64.urlsafe_b64decode(client_data_json_b64 + '==').decode()

    client_data_json_obj = json.loads(client_data_json_str)

    expected_challenge = base64url_to_bytes(client_data_json_obj.get('challenge'))
    expected_origin = client_data_json_obj.get('origin')

  
    credential = {
        'id': client_response.get('id'),
        'rawId': client_response.get('rawId'),
        'response': {
            'clientDataJSON': client_response.get('response').get('clientDataJSON'),
            'authenticatorData': client_response.get('response').get('authenticatorData'),
            'signature': client_response.get('response').get('signature'),
            'userHandle': client_response.get('response').get('userHandle'),
        },
        'type': "public-key"
    }

    user_name = session.get('user_name')

    user = User.query.filter_by(email=user_name).first()
    print(user_name)

    if user is None:
        return jsonify({'status': 'failed', 'message': 'User not found'})


    webauthn_response = verify_authentication_response(
        credential=credential,
        expected_challenge=expected_challenge,
        expected_rp_id='f90a-2800-810-469-744-b890-f13-99c5-163.ngrok-free.app',
        expected_origin=expected_origin,
        credential_public_key=user.public_key,
        credential_current_sign_count=user.sign_count,
        require_user_verification=False
    )

    user.sign_count = webauthn_response.new_sign_count
    db.session.commit()

    return jsonify({'status': 'ok'})


@app.route('/generate-random-string', methods=['GET'])
def generate_random_string():
    random_string = secrets.token_urlsafe(32)  
    return jsonify({'randomString': random_string}), 200


@app.route('/get_id', methods=['GET'])
def get_id():
    data = request.args.get()
    email = data.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'user_id': user.id}), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

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

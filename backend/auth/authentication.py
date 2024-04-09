
from flask import jsonify, session, make_response
from utils.database import db, User
from webauthn import options_to_json, generate_authentication_options, verify_authentication_response, base64url_to_bytes
from webauthn.helpers.structs import (
    PublicKeyCredentialDescriptor,
    PublicKeyCredentialType,
    AuthenticatorTransport,
)
from utils.utils import generate_challenge, RP_ID
import base64
import json


def login_user(data):
    email = data.get('email')

    user = User.query.filter_by(email=email).first()

    session['user_id'] = user.id

    if not user:
         return jsonify({'message': 'Credenciales inválidas'}), 401

    challenge = generate_challenge()

    if user:
            allow_credentials = [PublicKeyCredentialDescriptor(
                id=user.credential_id,
                type=PublicKeyCredentialType.PUBLIC_KEY,
                transports=[AuthenticatorTransport.USB, AuthenticatorTransport.NFC,
                            AuthenticatorTransport.BLE, AuthenticatorTransport.INTERNAL,
                            AuthenticatorTransport.HYBRID],
            )]
            options = generate_authentication_options(
                    rp_id=RP_ID,
                    challenge=challenge,
                    timeout=60000,
                    allow_credentials=allow_credentials,
                )
            resp = make_response(options_to_json(options=options))
            resp.set_cookie('user_id', str(user.id))
            return resp, 200
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401

def verify_authentication(client_response):
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

    if user is None:
        return jsonify({'status': 'failed', 'message': 'User not found'})

    webauthn_response = verify_authentication_response(
        credential=credential,
        expected_challenge=expected_challenge,
        expected_rp_id=RP_ID,
        expected_origin=expected_origin,
        credential_public_key=user.public_key,
        credential_current_sign_count=user.sign_count,
        require_user_verification=False
    )

    user.sign_count = webauthn_response.new_sign_count
    db.session.commit()

    return jsonify({'status': 'ok'})
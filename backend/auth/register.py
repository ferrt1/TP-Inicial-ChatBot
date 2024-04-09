import os
import base64
import json
from flask import jsonify, request, session
from utils.database import db, User
from utils.utils import RP_ID, RP_NAME, UKEY_DEFAULT_BYTE_LEN, generate_challenge
from webauthn import generate_registration_options, options_to_json, verify_registration_response, generate_authentication_options, base64url_to_bytes
from webauthn.helpers.structs import (
    AttestationConveyancePreference,
    AuthenticatorAttachment,
    AuthenticatorSelectionCriteria,
    ResidentKeyRequirement
)

def register_user(email):
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'status': 'failed', 'message': 'El correo electrónico ya está registrado'}), 401

    challenge = generate_challenge()

    ukey_bytes = os.urandom(UKEY_DEFAULT_BYTE_LEN)
    ukey_base64 = base64.urlsafe_b64encode(ukey_bytes)
    if not isinstance(ukey_base64, str):
        ukey_base64 = ukey_base64.decode('utf-8')

    # No creamos el usuario aquí, solo guardamos la información necesaria en la sesión
    session['registration'] = {
        'email': email,
        'user_id': ukey_bytes,
    }

    make_credential_options = generate_registration_options(
        rp_id=RP_ID,
        rp_name=RP_NAME,
        user_id=ukey_bytes,
        user_name=email,
        attestation=AttestationConveyancePreference.DIRECT,
        authenticator_selection=AuthenticatorSelectionCriteria(
            authenticator_attachment=AuthenticatorAttachment.PLATFORM,
            resident_key=ResidentKeyRequirement.PREFERRED,
        ),
        challenge=challenge,
        timeout=120000,
    )

    session['user_name'] = email

    return options_to_json(options=make_credential_options), 200

def verify_registration(email, user_id, client_response):
    # Aquí es donde creamos el usuario, después de que la autenticación ha sido verificada con éxito
    registration = session.get('registration')
    if registration is None:
        return jsonify({'status': 'failed', 'message': 'No registration in progress'}), 400

    new_user = User(email=email, user_id=user_id)
    db.session.add(new_user)
    db.session.commit()

    client_response = request.json.get('response')
    inner_response = client_response.get('response')
    client_data_json = inner_response.get('clientDataJSON')
    attestation_object = inner_response.get('attestationObject')

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
        expected_rp_id=RP_ID,
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

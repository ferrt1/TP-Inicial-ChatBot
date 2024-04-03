const userEmail = document.getElementById('registerEmail')

var base64url = {
    encode: function (data) {
        var b64 = btoa(data);
        return b64.replace('+', '-').replace('/', '_').replace(/=+$/, '');
    },
    decode: function (data) {
        data += '=='.slice(2 - (data.length & 3));
        return atob(data.replace('-', '+').replace('_', '/'));
    }
};

function publicKeyCredentialToJSON(pubKeyCred) {
    if (pubKeyCred instanceof Array) {
        let arr = [];
        for (let i of pubKeyCred)
            arr.push(publicKeyCredentialToJSON(i));

        return arr
    }

    if (pubKeyCred instanceof ArrayBuffer) {
        return base64url.encode(String.fromCharCode.apply(null, new Uint8Array(pubKeyCred)));
    }

    if (pubKeyCred instanceof Object) {
        let obj = {};

        for (let key in pubKeyCred) {
            obj[key] = publicKeyCredentialToJSON(pubKeyCred[key]);
        }

        return obj
    }

    return pubKeyCred;
}


function base64urlToBuffer(base64url) {
    let base64 = base64url.replace(/-/g, '+').replace(/_/g, '/');
    let rawData = window.atob(base64);
    let outputArray = new Uint8Array(rawData.length);
    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray.buffer;
}

function showAlert(message) {
    var customAlert = document.getElementById('customAlert');
    var customAlertMessage = document.getElementById('customAlertMessage');

    customAlertMessage.innerText = message;
    customAlert.style.display = 'block';

    var customAlertClose = document.getElementById('customAlertClose');
    customAlertClose.addEventListener('click', function () {
        customAlert.style.display = 'none';
    });
}



// Función para registrar un nuevo usuario
async function registerUser(email) {
    try {
        
        const optionsResponse = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email })
        });

        const responseData = await optionsResponse.json();
        
        if (optionsResponse.ok) {
            const options = responseData;
            options.challenge = base64urlToBuffer(options.challenge);
            options.user.id = base64urlToBuffer(options.user.id);
            
            const credential = await navigator.credentials.create({
                publicKey: options
            });

            //console.log(credential);
            
            let sendCredential = publicKeyCredentialToJSON(credential);

            
            const verifyResponse = await fetch('/verify_registration', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ response: sendCredential })
            });
            
            if (!verifyResponse.ok) {
                throw new Error('Error al verificar el registro');
            }

            showAlert('Registrado exitosamente! Prueba iniciando sesión');
            document.getElementById('registerForm').reset();
        } else {
            
            showAlert('El correo ya se encuentra registrado.');
        }
    } catch (error) {
        console.error('Error de red:', error);
    }
}

// Función para autenticar al usuario
async function authenticateUser(email) {
    try {
        
        const optionsResponse = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email })
        });

        if (!optionsResponse.ok) {
            throw new Error('Error al obtener las opciones de autenticación');
        }

        const options = await optionsResponse.json();
        console.log(options);
        options.challenge = base64urlToBuffer(options.challenge);
        options.allowCredentials.forEach(cred => cred.id = base64urlToBuffer(cred.id));

        
        const credential = await navigator.credentials.get({
            publicKey: options
        });

        let sendCredential = publicKeyCredentialToJSON(credential);

        
        const verifyResponse = await fetch('/verify_authentication', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ response: sendCredential })
        });

        if (!verifyResponse.ok) {
            throw new Error('Error al verificar la autenticación');
        }

        window.location.href = '/chatbot';
    } catch (error) {
        console.error('Error de red:', error);
    }
}
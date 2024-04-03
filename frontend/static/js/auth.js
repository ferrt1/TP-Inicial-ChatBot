function generateRandomChallenge() {
    var challenge = new Uint8Array(16);
    window.crypto.getRandomValues(challenge);
    return challenge;
}

function addBiometric(user_id){
    navigator.credentials.create({
        publicKey: {
            challenge: generateRandomChallenge(),
            rp: { name: "example" },
            user: {
                id: generateRandomChallenge(),
                name: "username",
                displayName: "User Name",
            },
            pubKeyCredParams: [
                {alg: -7, type: 'public-key'},  // ES256
                {alg: -257, type: 'public-key'} // RS256
            ]
        },
    })
    .then(function (newCredentialInfo) {
        let fingerprint = btoa(String.fromCharCode.apply(null, new Uint8Array(newCredentialInfo.response.attestationObject)));
        let publicKey = btoa(String.fromCharCode.apply(null, new Uint8Array(newCredentialInfo.rawId)));
        localStorage.setItem('userId', user_id);
        
        fetch('/register_fingerprint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                userId: user_id,
                fingerprint: fingerprint,
                publicKey: publicKey  
            })
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            //manejar la respuesta 
        });
    })

    .catch(function (error) {
        // Error en el registro
        console.error("Error en el registro con huella digital:", error);
    });
}

function isMobileDevice() {
    const mobileRegex = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i;
    return mobileRegex.test(navigator.userAgent) && window.innerWidth <= 768; // Añadimos una condición para el ancho de la ventana
}

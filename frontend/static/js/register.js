// funcion para registrar un nuevo usuario
async function registerUser(username, mail, password) {
    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username, mail, password })
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message); 
        } else {
            console.error('Error al registrar el usuario');
        }
    } catch (error) {
        console.error('Error de red:', error);
    }
}

// funcion para autenticar al usuario
async function authenticateUser(mail, password) {
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ mail, password })
        });

        if (response.ok) {
            window.location.href = '/chatbot'; 
        } else {
            console.error('Credenciales inválidas');
        }
    } catch (error) {
        console.error('Error de red:', error);
    }
}

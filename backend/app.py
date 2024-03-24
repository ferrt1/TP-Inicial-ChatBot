from flask import Flask, request, send_from_directory
from bot_logic import get_bot_response

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('../frontend/', 'index.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('../frontend/static/css', path)


@app.route("/bot", methods=["POST"])
def bot_response():
    user_message = request.form["user_message"]
    bot_message = get_bot_response(user_message)
    return bot_message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify, render_template
from nlp_model import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message field is required"}), 400

    user_message = data["message"]
    bot_reply = get_response(user_message)

    return jsonify({
        "user": user_message,
        "bot": bot_reply
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)

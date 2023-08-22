import flask
from chatbot_ import chatbot_

app = flask.Flask(__name__, template_folder="html", static_folder='static')


@app.route("/")
def index():
    return flask.render_template("index.html", intro_message=intro_message)


intro_message = ("Hello! I am the Qatar Expo 2023 chatbot. Try asking me about  the venue, schedule, or participating "
                 "countries.")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    if flask.request.method == "POST":
        user_input = flask.request.json["user_input"]
        print(user_input)
        resp = chatbot_.respond(user_input)
        if not resp:
            resp = "Sorry, I don't understand. Please try again."
        return {'status': 'ok', 'response': resp}
    else:
        return {'status': 'error', 'response': '405 Method Not Allowed'}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

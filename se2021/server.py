from flask import Flask, jsonify

app = Flask(__name__)

MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def encode_morse(phrase):
    return " ".join([MORSE[symbol.lower()] for symbol in phrase])


@app.route("/")
def hello():
    payload = {"message": "Hello, world"}
    return jsonify(payload)


@app.route("/morse/<phrase>")
def morse(phrase):
    payload = {"result": encode_morse(phrase)}
    return jsonify(payload)


if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    payload = {'message': 'Hello, world'}
    return jsonify(payload)

if __name__ == '__main__':
    app.run()

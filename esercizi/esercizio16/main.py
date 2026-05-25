import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/api')
def api_giver():
    ris = richiesta_api_fox()
    return jsonify(ris)

def richiesta_api_fox():
    resp = requests.get("https://randomfox.ca/floof/", timeout=5)
    if resp.status_code == 200:
        return resp.json()
    else:
        return {"Error":resp.status_code}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
import requests
from flask import Flask, jsonify, request

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

@app.route('/somma', methods=['GET'])
def somma():
    parm1 = request.args.get('primo_n, type=int')
    parm2 = request.args.get('secondo_n, type=int')
    #usando in questo modo devo mettere i 2 parametri nel mio url
    #dopo il mio url base metto ? in modo da indicare divisione percorso - parametri
    #i parametri si scrivono con nome parametro = parametro
    #fra i vari parametri devo mettere & in modo da dividerli
    if parm1 is not None or parm2 is not None:
        ris = parm1 + parm2
    return jsonify(ris)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
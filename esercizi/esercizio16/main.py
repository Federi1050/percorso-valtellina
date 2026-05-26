import requests
from flask import Flask, jsonify, request
import pandas as pd
from pandas_generator import Pandas_generator

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
    ris = 0
    parm1 = request.args.get('primo_n', type=int)
    parm2 = request.args.get('secondo_n', type=int)
    #usando in questo modo devo mettere i 2 parametri nel mio url
    #dopo il mio url base metto ? in modo da indicare divisione percorso - parametri
    #i parametri si scrivono con nome parametro = parametro
    #fra i vari parametri devo mettere & in modo da dividerli
    if parm1 is not None and parm2 is not None:
        ris = parm1 + parm2
    return jsonify(ris)

@app.route('/pandas/series' , methods=['GET'])
def pd_random_series():
    n = request.args.get('n', type=int)
    pdGen = Pandas_generator()
    r = pdGen.generate_r_series(n).to_list()
    return jsonify(r)

@app.route('/pandas/dataFrame' , methods=['GET'])
def pd_dataFrame():
    n = request.args.get('n', type=int)
    pdGen = Pandas_generator()
    r = pdGen.generate_r_dataFrame(n)
    return jsonify(r.to_dict(orient='records'))

@app.route('/test-post', methods=['POST'])
def test_post():
    data = request.json
    return jsonify({"message":"Dati ricevuti","data":data})

# crea una rotta che utilizzi metodo post. input json {n1 --> 30,n2-->40,op --> *}
# output json che corrisponde calcolo
# ese n1 30 n2 40 op * ->> {risultato:1200}
@app.route('/mat_op', methods=['POST'])
def mat_op():
    data = request.json
    n1 = data.get("n1")
    n2 = data.get("n2")
    op = data.get("op")
    #controllo n1 e n2 sono numeri
    if not isinstance(n1, int) or not isinstance(n2, int):
        return jsonify({"mess":"non hai messo dei numeri"})
    if op == '*':
        pass
        obj = {"risultato": data.get("n1") * data.get("n2")}
    elif op == '/':
        pass
        obj = {"risultato": data.get("n1") / data.get("n2")}
    elif op == '+':
        pass
        obj = {"risultato": data.get("n1") + data.get("n2")}
    elif op == '-':
        pass
        obj = {"risultato": data.get("n1") - data.get("n2")}
    else:
        pass
        obj = {"mess": "impossibile trovare operatore"}
    return jsonify(obj)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
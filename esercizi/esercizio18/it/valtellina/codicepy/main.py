'''
in flask che poi devi mettere su docker
dato in pasto un CSV deve leggerlo usando pandas
retituisce in forma json
più file
una classe CSV manager (legge csv e lo manipola) csv passato da flask
ogni funzione di eploraioni dati deve dare una risposta con flask
head 5 top -
tail 5 ult -
dimensioni -
info colonne e tipo dati -
ricerca con filtro
usa pure i package it.valtellina.nomepackage
'''
from flask import Flask, request, jsonify

from it.valtellina.codicepy.CSV_manager import CSV_manager

app = Flask(__name__)
csv_manager = CSV_manager()

@app.route('/')
def home():
    return "Ciao dal container"

@app.route('/inserire-csv', methods=['POST'])
def inserire_csv():
    csv_testo = request.json["csv"]

    result = csv_manager.convert_csv_str_in_json(csv_testo)
    csv_manager.set_csv(result)
    return jsonify(result)

@app.route('/head')
def head():
    risposta = csv_manager.get_head()
    return jsonify(risposta)

@app.route('/tail')
def tail():
    risposta = csv_manager.get_tail()
    return jsonify(risposta)

@app.route('/dimensioni')
def dimensioni():
    risposta = csv_manager.get_dimensioni()
    return jsonify(risposta)

@app.route('/info')
def info():
    risposta = csv_manager.get_info()
    return jsonify(risposta)

@app.route('/ricerca', methods=['POST'])
def ricerca():
    risposta = request.get_json()
    risposta = csv_manager.ricerca(risposta.get("attributo"), risposta.get("filtro"))
    return jsonify(risposta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
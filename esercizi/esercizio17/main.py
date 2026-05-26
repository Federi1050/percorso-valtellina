'''
costruire applicativo che dialoga con il container docker in mysql
(se non funziona docker sqlite)
serve indirizzo ip macchina locale (192.168.1.14)

ID | IMAGE
1     img.jpg
2     img.jpg
3     img.jpg

ID -> primarykey --> auto increment

utilizzare un ORM
creare seguenti api:
    - mostra tutto contenuto database (get)
    - inserire un nuovo elemento no doppioni --> https://randomfox.ca/floof
            solo img ogni volta che chiami
    - inserire un elemento manualmente -- > {"image","immagine.jpg"}
    - cancellare elemento --> {"img.jpg"} --> T/F
'''
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.1.14:3306/foxdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Fox(db.Model):
    __tablename__ = 'foxes'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/mostra_floof')
def mostra_floof():
    results = db.session.query(Fox).all()

    return jsonify([
        {
            "id":f.id,
            "image":f.image
        }
        for f in results
    ])

@app.route('/aggiungi_random')
def aggiungi_random():
    pass
    random = richiesta_api_fox()
    if random.get("Error"):
        return jsonify({"Error":True, "Error_code":random.get("Error")})

    existing = db.session.query(Fox).filter_by(image=random.get("image")).first()
    if existing:
        return jsonify({"messaggio":"fox gia' esistente", "id":existing.id, "image":existing.image})

    fox = Fox(
        image=random.get("image")
    )

    db.session.add(fox)
    db.session.commit()
    return jsonify({"id": fox.id, "image": fox.image})

@app.route('/aggiungi_specifico', methods=['POST'])
def aggiungi_specifico():
    data = request.get_json()

    if not data or "image" not in data:
        return jsonify({"Error":True, "Error_message":"Image is required"})

    fox = Fox(
        image = data.get("image")
    )
    db.session.add(fox)
    db.session.commit()
    return jsonify({"id":fox.id,"image":fox.image})

@app.route('/rimuovi_floof', methods=['DELETE'])
def rimuovi_floof():
    data = request.get_json()
    if not data or "image" not in data:
        return jsonify({"Error":True, "Error_message":"Image is required"})

    existing = db.session.query(Fox).filter_by(image=data.get("image")).first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        return jsonify({"messaggio": "fox eliminata", "id": existing.id, "image": existing.image})

    return jsonify({"Error":True, "messaggio":"volpe inserita non esistente"})

def richiesta_api_fox():
    ris = requests.get('https://randomfox.ca/floof', timeout=5)
    if ris.status_code == 200:
        return ris.json()
    else:
        return {"Error":True, "Error_code":ris.status_code}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

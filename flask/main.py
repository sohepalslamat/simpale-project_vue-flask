from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arzaq.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def serialize(context):
        all =[]
        for data in context:
            all.append({'id': data.id, 'name': data.name, 'age': data.age})
        all = jsonify(all)
        return all

db.create_all()


@app.route('/users', methods= ["GET","POST"])
def add_user():
    if request.method == "POST":
        req = request.get_json(force=True)
                
        name = req['name']
        age = req['age']
        user = Users(name, age)

        db.session.add(user)
        db.session.commit()
        
        return 'created', 201

    elif request.method == "GET":
        users = Users.query.all()
        users = Users.serialize(users)
        return users

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    Users.query.filter_by(id=id).delete()

    db.session.commit()

    return 'deleted', 200

        
if __name__ == '__main__':
    app.run(debug=True)
    
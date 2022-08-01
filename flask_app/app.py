'''Simple GET/POST(get user / add user) app.'''
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rajsingh@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    '''create user DB'''
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(80), unique=True, nullable=False)
    country = db.Column(db.String(120), nullable=False)

    def __init__(self, uname, country):
        self.uname = uname
        self.country = country

@app.route('/')
def home():
    '''home page'''
    return 'Welcome to my site!'

@app.route('/getuser', methods = ['GET'])
def getuser():
    '''Get user details'''
    all_users = []
    users = User.query.all()
    for user in users:
        results = {
            "ID ":user.id,
            "Name ":user.uname,
            "Country ":user.country,
        }
        all_users.append(results)

    return jsonify(
        {
            "success": True,
            "users": all_users,
        }
    )

@app.route('/adduser', methods=['POST'])
def adduser():
    '''Add user'''
    user_data = request.json

    uname = user_data['uname']
    country = user_data['country']

    user = User(uname=uname, country=country)
    db.session.add(user)
    db.session.commit()

    return jsonify(
        {
            "success": True,
            "response": "User added.",
        }
    )

if __name__ == '__main__':
    db.create_all()
    app.run()

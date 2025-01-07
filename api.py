from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,reqparse,fields,marshal_with,abort

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db=SQLAlchemy(app)
api=Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False,unique=True)
    email = db.Column(db.String(100), nullable=False,unique=True)

    def __repr__(self):
        return f"User(name={self.name},email={self.email})"

user_args=reqparse.RequestParser()
user_args.add_argument("name",type=str,required=True,help="name is required")
user_args.add_argument("email",type=str,required=True,help="email is required")
# class Users(Resource):

@app.route('/')
def home():
    return "<h1>Flask REST API</h1>"

if __name__=='__main__':
       app.run(debug=True)

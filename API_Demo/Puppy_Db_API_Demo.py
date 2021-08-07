from flask_jwt import JWT, jwt_required
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from security_methods import authenticate, identity
from flask_restful import Resource, Api

import os
from flask_migrate import Migrate
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)

Migrate(app, db)


# our Model Class
class Puppy(db.Model):
    __tablename__ = 'puppy_api'
    name = db.Column(db.String(80), primary_key = True)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name": self.name}

    def __str__(self):
        return f"{self.name} "

class Puppies(Resource):
    # all the get/post/delete method should be having same signature if they're in same class
    # GET
    def get(self, name):
        puppy = Puppy.query.filter_by(name=name).first()
        if puppy:
            print(puppy)
            return puppy.json()
        else:
            return {'name' : 'Not Found' }, 404

    # POST
    def post(self, name):
        pupp_add = Puppy(name=name)
        db.session.add(pupp_add)  # append the name value pair to our puppies list
        db.session.commit()
        print(pupp_add)
        return {'note':'Puppy Added'}

    # DELETE
    def delete(self, name):
       pupp_del = Puppy.query.filter_by(name=name).first()
       if name:
           db.session.delete(pupp_del)
           print(pupp_del)
           db.session.commit()
           return {'Deleted' : 'Deleted Puppy'}
       else:
           return {'Puppy':'Not Found to be deleted'}

class AllPuppies(Resource):
    # GET All Puppies
    # @jwt_required()  # it requires authentication to see all puppies.
    def get(self):
        puppies = Puppy.query.all()
        print(puppies)
        return [pupp.json() for pupp in puppies]

api.add_resource(Puppies, '/puppy/<string:name>')
api.add_resource(AllPuppies, '/puppy/all')


if __name__ == '__main__':
    app.run(debug=True)
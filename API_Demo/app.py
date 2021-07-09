from flask import Flask
from flask_restful import Resource, Api
from Model import User  # importing our User class

app = Flask(__name__)
api = Api(app)  # make the API wrapper available for our app

class HelloWorld(Resource):  # our class inheriting Resource class.
    def get(self):
        return {'Hell' : 'World'}

api.add_resource(HelloWorld, '/')  # from postman we can make get req to home page and it will return the dict
if __name__ =='__main__':  # run the app and then make get req from postman on the (http://127.0.0.1:5000/)
    app.run(debug=True)
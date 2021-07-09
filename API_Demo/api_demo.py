from flask_restful import Resource, Api
from flask import Flask
from security_methods import authenticate, identity  # getting our defined methods from other py module
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
api = Api(app)  #Creates API wrapper for our application

jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)  # signate of JWT needs two args

# Define Resource(Class on which GET/POST/DELETE) request will be made
puppies = []  # it is list of dictionaries : name value pair
class Puppies(Resource):
    # all the get/post/delete method should be having same signature if they're in same class
    # GET
    def get(self, name):
        for pupp in puppies:
            if pupp['name'] == name:
                print(puppies)
                return pupp
        print(puppies)
        return {'name' : None }

    # POST
    def post(self, name):
        puppies.append({'name':name})  # append the name value pair to our puppies list
        print(puppies)
        return {'note':'Puppy Added'}

    # DELETE
    def delete(self, name):
        for index, pupp in enumerate(puppies):
            if pupp['name'] == name:
                puppies.pop(index)
                print(puppies)
                return {'note': 'Delete Success'}
        return {'Failed' : 'Not Found so not deleted'}

class AllPuppies(Resource):
    # GET All Puppies
    @jwt_required()  # it requires authentication to see all puppies.
    def get(self):
        print(puppies)
        return puppies

api.add_resource(AllPuppies, '/puppy/allpuppies')
api.add_resource(Puppies, '/puppy/<string:name>') #values inside<> this indicate the variable of string type which will be dynamic

if __name__=='__main__':
    app.run(debug=True)
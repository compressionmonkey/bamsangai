from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        if request.files:
            print('here i am')
            return request.files
        return { 'about': 'Hello' }
    def post(self):
        return "Ayyyy"
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
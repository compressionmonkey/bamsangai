from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return { 'about': 'Hello' }
    def post(self):
        print(request.files)
        if request.files:
            print('here i am')
            image = request.files["image"]
            print(image)
            return image
        return "Ayyyy"
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
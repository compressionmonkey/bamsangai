from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

MYDIR = os.path.dirname(__file__)
app.config["IMAGE_UPLOADS"] = "Uploads"
api = Api(app)

class FaceDetection(Resource):
    def get(self):
        return { 'about': 'Hello' }
    def post(self):
        if request.files:
            image = request.files["images"]
            image.save(os.path.join(MYDIR + "/" + app.config["IMAGE_UPLOADS"], image.filename))
            return "Image Uploaded successfully"
        else:
            return "Error uploading File"
api.add_resource(FaceDetection, '/')

if __name__ == '__main__':
    app.run(debug=True)
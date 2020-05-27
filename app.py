from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('./Uploads/blob')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
            # image.save(os.path.join(MYDIR + "/" + app.config["IMAGE_UPLOADS"], image.filename))
            image.save(MYDIR + "/" + app.config["IMAGE_UPLOADS"])
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            if faces is not '':
                print(True)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

            cv2.waitKey()
            return "Image Uploaded successfully"
        else:
            return "Error uploading File"
api.add_resource(FaceDetection, '/')

if __name__ == '__main__':
    app.run(debug=True)
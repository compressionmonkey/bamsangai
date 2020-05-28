from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os
# from cv2 import CascadeClassifier, imread, cvtColor, COLOR_BGR2GRAY, rectangle, waitKey
from pathlib import Path


app = Flask(__name__)
CORS(app)

api = Api(app)

MYDIR = os.path.dirname(__file__)
app.config["IMAGE_UPLOADS"] = MYDIR+"/Uploads"

# face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')


class FaceDetection(Resource):
    def get(self):
        return { 'about': 'Hello' }
    def post(self):
        if request.files:
            image = request.files["images"]
            print("opopopop",image)
            image.save("/Uploads/"+ image.filename)
            #image.save(MYDIR + "/" + app.config["IMAGE_UPLOADS"],image.filename)
            # entries = Path(MYDIR + "/" + app.config["IMAGE_UPLOADS"] + "/")
            # for entry in entries.iterdir():
            #     print(entry.name)
            # with os.scandir(MYDIR + "/" + app.config["IMAGE_UPLOADS"] + "/") as entries:
            #     for entry in entries:
            #         print("here is ",entry.name)
            # img = imread(MYDIR + "/" + app.config["IMAGE_UPLOADS"] + image.filename)
            # gray = cvtColor(img, COLOR_BGR2GRAY)
            # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            # if faces is not '':
            #     print(True)
            #
            # for (x, y, w, h) in faces:
            #     rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            #
            # waitKey()
            return "Image Uploaded successfully"
        else:
            return "Error uploading File"
api.add_resource(FaceDetection, '/')

if __name__ == '__main__':
    app.run(debug=True)
import cv2 as cv
from PIL import Image
import numpy as np
import os


class FaceTrainer:
    """This class can train a human face and save it in a yml file.
    """
    def __init__(self, xml_file):
        self.detector = cv.CascadeClassifier(cv.data.haarcascades + xml_file)
        self.recognizer = cv.face.LBPHFaceRecognizer_create()

    def face_trainer(self):
        img_faces = []
        img_ids = []
        os.chdir("data/images_db")
        img_paths = [os.path.join(os.getcwd(), files) for files in os.listdir(os.getcwd())]
        for img_path in img_paths:
            img_face_pil = Image.open(img_path).convert('L')
            img_face_np = np.array(img_face_pil, dtype="uint8")
            img_id = int(os.path.split(img_path)[-1].split(".")[1])
            faces = self.detector.detectMultiScale(img_face_np)
            for (x, y, w, h) in faces:
                img_faces.append(img_face_np[y:y+h, x:x+w])
                img_ids.append(img_id)
        self.recognizer.train(img_faces, np.array(img_ids))
        os.chdir("../../training_data")
        self.recognizer.write('training_data.yml')

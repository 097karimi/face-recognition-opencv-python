from detection.detection import FaceDetector
from training.training import FaceTrainer
from prediction.prediction import Predictor
import os

get_cwd = os.getcwd()

while True:
    os.chdir(get_cwd)
    var_input = input(
                  "\n"
                  "******* Face Rcognition ******* \n\n"
                  "This program has tree parts:\n\n"
                  "  1- Press '1' to take some photos from the face.\n"
                  "  2- Press '2' to train and generate 'yml'.\n"
                  "  3- Press '3' to predict.\n\n"
                  "Finally press '0' to exit !\n --> : \t")
                  
    if (str(var_input) == '1'):
        id_num = input("Enter an ID")
        face_detector = FaceDetector('haarcascade_frontalface_default.xml', id_num)
        face_detector.face_detector()

    elif (str(var_input) == '2'):
        face_trainer = FaceTrainer('haarcascade_frontalface_default.xml')
        face_trainer.face_trainer()
        break

    elif (str(var_input) == '3'):
        face_predictor = Predictor('haarcascade_frontalface_default.xml')
        face_predictor.face_predictor()

    elif (str(var_input) == '0'):
        exit(0)

    else:
        print("-------------------"
              "\nChoose a number range from 0 to 3!")

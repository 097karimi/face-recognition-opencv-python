import cv2 as cv


class Predictor:
    """This class can predict a human face which it has been already trained."""

    def __init__(self, xml_file):
        self.recognizer = cv.face.LBPHFaceRecognizer_create()
        self.detector = cv.CascadeClassifier(cv.data.haarcascades + xml_file)

    def face_predictor(self):
        self.recognizer.read('training_data/training_data.yml')
        cap = cv.VideoCapture(0)
        font = cv.FONT_HERSHEY_SIMPLEX
        font_color = (255, 255, 255)

        while True:
            ret, frame = cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                id_num, conf = self.recognizer.predict(gray[y:y + h, x:x + w])
                if conf < 50:
                    cv.putText(frame, str(id_num), (x, y + h), font, 1, font_color)
                else:
                    cv.putText(frame, "Unknown", (x, y + h), font, 1, font_color)
            cv.namedWindow("Face Recognition", cv.WINDOW_GUI_NORMAL)
            cv.imshow('Face Recognition', frame)
            if cv.waitKey(10) & 0xFF == ord('q'):
                break
        cv.destroyAllWindows()

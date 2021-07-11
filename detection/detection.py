import cv2 as cv


class FaceDetector:
    
    """The class can detect human face in the pictures or videos and save them
       as a picture in a folder which name is 'imagesdb'."""

    def __init__(self, xml_file, idnum):
        self.detector = cv.CascadeClassifier(cv.data.haarcascades + xml_file)
        self.id_num = idnum

    def face_detector(self):
        counter = 0
        cap = cv.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 200), 2)
                counter = counter + 1
                cv.imwrite(
                    'data/images_db/image.' + str(self.id_num) + '.' + str(counter) + ".jpg",
                    gray[y:y + h, x:x + w])
                cv.namedWindow("Face Recognition", cv.WINDOW_GUI_NORMAL)
                cv.imshow("Face Recognition", frame)
            if cv.waitKey(100) & 0xFF == ord('q'):
                break
            elif counter > 25:
                break
        else:
            print("\n\t\t-Turn the camera on!")
        cap.release()
        cv.destroyAllWindows()

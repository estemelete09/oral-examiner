import cv2,os,urllib.request
import numpy as np
from django.conf import settings
#install openCV using the command: pip install opencv-python

face_detection_videocam = cv2.CascadeClassifier(os.path.join(
            settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
eye_detection_videocam = cv2.CascadeClassifier(os.path.join(
          settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_eye_tree_eyeglasses.xml'))

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
#for face and eye detection
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)

            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
            eyes = eye_detection_videocam.detectMultiScale(roi_gray)
            for (ex, ey ,ew, eh) in eyes:
                cv2.rectangle(roi_color, pt1=(ex,ey), pt2=(ex+ew, ey+eh), color=(0, 255, 0), thickness= 1)
                
        frame_flip = cv2.flip(image,1)
        ret, jpeg = cv2.imencode('.jpg', frame_flip)
        return jpeg.tobytes()

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
        gray = cv2.bilateralFilter(gray,5,1,1) 
        faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(image, pt1=(x, y), 
                pt2=(x + w, y + h), 
                color=(255, 0, 0), 
                thickness=2) #displays the box detecting the face

            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
            eyes = eye_detection_videocam.detectMultiScale(roi_gray)
            for (ex, ey ,ew, eh) in eyes:
                cv2.rectangle(roi_color, pt1=(ex,ey), 
                    pt2=(ex+ew, ey+eh), 
                    color=(0, 255, 0), 
                    thickness= 1) #displays the boxes detecting the eyes

            #text displays if eyes is detected or not
            if(len(eyes)>=2):   
                cv2.putText(image,  
                "Eyes detected!", (70,70),  
                cv2.FONT_HERSHEY_PLAIN, 2, 
                (255,255,255),2) 
            else: 
                cv2.putText(image,  
                "No eyes detected", (70,70), 
                cv2.FONT_HERSHEY_PLAIN, 3, 
                (0,0,255),2) 
                
        # frame_flip = cv2.flip(image,1)
        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()

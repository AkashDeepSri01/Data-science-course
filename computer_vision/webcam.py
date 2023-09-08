import cv2
import numpy as np
 
#create a videocapture object
WEBCAM_IDX = 0
cam = cv2.VideoCapture(WEBCAM_IDX) 
while cam.isOpened():
     #capture image from camera
     state,image =cam.read()
     if not state:break
     cv2.imshow('image',image)
     key = cv2.waitKey(10)

     if key ==27:a
          break
#release camera
cam.release()
cv2.destroyAllWindows()
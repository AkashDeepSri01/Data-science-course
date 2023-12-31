import cv2
import numpy as np

file=r'C:\Users\NEW PC\Desktop\DSC_6960.MOV'
vid = cv2.VideoCapture(file)
while True:
    state,image = vid.read()
    if not state: break
    #resize to 400x500
    sm_image_1 = cv2.resize(image,(500,500))
    sm_image_2 = cv2.resize(image,None,fx=.25,fy=.25)
    bw_image = cv2.cvtColor(sm_image_1,cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(sm_image_2,cv2.COLOR_BGR2RGB)
    edge_image = cv2.Canny(rgb_image,100,200)
    cv2.imshow('video 1',sm_image_1)
    cv2.imshow('video 2',sm_image_2)
    cv2.imshow('bw',bw_image)
    cv2.imshow('rgb',rgb_image)
    cv2.imshow('edge',edge_image)
    key=cv2.waitKey(10)
    if key ==27:break
cv2.destroyAllWindows()
vid.release()    
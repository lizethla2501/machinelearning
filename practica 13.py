# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:02:11 2026

@author: lizal
"""

import cv2
import numpy as np
import imutils
from datetime import datetime
camara= cv2.VideoCapture("video.mp4")
camara.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
camara.set(cv2.CAP_PROP_FRAME_HEIGHT , 300)

while(True):
    f,frame = camara.read()
    if f == False:
        break
    else:
        tiempo= datetime.now()
        frame= imutils.resize(frame,width=400)
        framegris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rojo1 = np.array([0,100,20])
        rojo2 = np.array([5,255,255])
        rojo3 = np.array([175,100,20])
        rojo4 = np.array([179,255,255])
        kernel = np.ones((7,7),np.uint8)
        mascara1= cv2.inRange(hsv, rojo1, rojo2)
        mascara2 = cv2.inRange(hsv, rojo3, rojo4)
        mascara = cv2.add(mascara1, mascara2)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
        resultado = cv2.bitwise_and(frame, frame, mask=mascara)
        resultado[mascara>0]=(255,0,0)
        
        framegris= cv2.cvtColor(framegris, cv2.COLOR_GRAY2BGR)
        framegris= cv2.add(framegris,resultado)
        #frame= cv2.add(frame,resultado)
        
        cv2.namedWindow("Video",cv2.WINDOW_NORMAL)
        cv2.imshow("Video", frame)
        cv2.namedWindow("VideoGris",cv2.WINDOW_NORMAL)
        cv2.imshow("VideoGris", framegris)
        key = cv2.waitKey(1)
        if key == ord('g'):
            nombre= "archivo"+str(tiempo.second)+".jpg"
            cv2.imwrite(nombre, framegris)
            print("imagen guardada")
    key = cv2.waitKey(1)
    if key == ord('a'):
        break
     
camara.release()
cv2.destroyAllWindows()

















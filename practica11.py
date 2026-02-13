# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 09:50:06 2026

@author: lizal
"""

import cv2
import numpy as np
videoReal = "video.mp4"

video = cv2.VideoCapture(videoReal)
fps = video.get(cv2.CAP_PROP_FPS)
print(fps)
tiempo = int(500/fps)

while(True):
    f,frame = video.read()
    if f == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rojo1 = np.array([0,100,20])
        rojo2 = np.array([5,255,255])
        rojo3 = np.array([175,100,20])
        rojo4 = np.array([179,255,255])
        kernel = np.ones((7,7),np.uint8)
        mascara1 = cv2.inRange(hsv, rojo1, rojo2)
        mascara2 = cv2.inRange(hsv, rojo3, rojo4)
        mascara = cv2.add(mascara1, mascara2)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
        resultado = cv2.bitwise_and(frame, frame, mask=mascara)
        resultado[mascara>0]=(10,155,25)
        cv2.namedWindow("NuevoFrame",cv2.WINDOW_NORMAL)
        cv2.imshow("NuevoFrame", resultado)
        cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(tiempo) & 0xFF == ord('a'):
           
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
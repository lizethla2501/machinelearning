# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 10:30:12 2026

@author: lizal
"""

import cv2
import numpy as np
camara= cv2.VideoCapture(0)
while(camara.isOpened()):
    f,frame = camara.read()
    if f== True:
        frame= cv2.flip(frame, 1)
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
        resultado[mascara>0]=(10,155,25)
        nuevo = cv2.add(frame, resultado)
        cv2.imshow("Resultado", resultado)
        cv2.imshow("Nuevo", nuevo)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == ord('a'):
            break
    else:
        break

camara.release()
cv2.destroyAllWindows()
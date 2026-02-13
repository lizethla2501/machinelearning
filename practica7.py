# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:11:41 2026

@author: lizal
"""
#rangos de vaslores
#Verde
#verde claro: 25,20,20
#verde oscuro: 100,255,255
#Azul
#Azul claro: 100,100,20
#Azul oscuro:125,255,255
#Rojo
#rojo claro1: 0,100,20
#rojo oscuro1: 5,255,255
#rojo claro2: 179,255,255
#amarillo
#amarillo claro: 15,100,20
#amarillo oscuro: 45,255,255
#blanco
#blanco claro: 220,220,220
#blanco oscuro: 255,255,255
  

import numpy as np
import cv2

img = cv2.imread("1.jpg")

cv2.putText(img, "colores a cambiar", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

verde1 = np.array([25, 20, 20])
verde2 = np.array([100, 255, 255])
kernel1 = np.ones((7, 7), np.uint8)

mascara = cv2.inRange(hsv, verde1, verde2)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel1)
mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel1)

resultado = cv2.bitwise_and(img, img, mask=mascara)
contorno, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i in contorno:
    area = cv2.contourArea(i)
    if area > 500:
        cv2.drawContours(resultado, [i], -1, (255, 0, 0), 3)
        x, y, w, h = cv2.boundingRect(i)
        areas = f"area:{int(area)}"
        cv2.putText(resultado, areas, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL)
cv2.namedWindow("mascara", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen1", cv2.WINDOW_NORMAL)
cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)

cv2.imshow("Resultado", resultado)
cv2.imshow("mascara", mascara)
cv2.imshow("Imagen1", img)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()






















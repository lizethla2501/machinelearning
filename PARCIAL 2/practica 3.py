# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 10:32:08 2026

@author: lizal
"""

#deteccion de objetos mediante su centro
#objetos de diferentes contornos
import cv2
import easygui as vent
import numpy as np

imagen = vent.fileopenbox(msg="Abrir Imagen",title="Abrir",
                          default="",filetypes=[".jpeg",".png","*.jpg"])

img = cv2.imread(imagen)
img = cv2.resize(img, (600, 600))
copia = img.copy()
copia = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)
_, valor = cv2.threshold(copia, 240, 255, cv2.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
contornos, _ = cv2.findContours(figura,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)

lista = []
for i in range(len(contornos)):
    area = cv2.contourArea(contornos[i])
    if area > 1000 and area < 308801:
        lista.append(area)
        print(f'Area: {area}')
        cv2.drawContours(img, contornos, i, (255, 0, 0), 10)
        objeto = contornos[i]
        M = cv2.moments(objeto)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            img = cv2.circle(img, (cx, cy), radius=1, color=(0, 255, 0), thickness=1)
            cv2.drawContours(img, contornos, i, (0, 0, 255), 10)
            img = cv2.putText(img, "Centro:" + str(area), (cx, cy),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.putText(img, "Cantidad: " + str(len(lista)), (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.namedWindow("copia", cv2.WINDOW_NORMAL)
cv2.imshow("copia", figura)
cv2.namedWindow("Ventana", cv2.WINDOW_NORMAL)
cv2.imshow("Ventana", img)
cv2.waitKey()
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 08:12:48 2026

@author: lizal
"""
#Azul
#Azul claro: 100,100,20
#Azul oscuro: 125,255,255
import cv2
import numpy as np
img = cv2.imread("colores.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
verde1 = np.array([25,20,20])
verde2 = np.array([100, 255,255])
azul1 = np.array([100,100,20])
azul2 = np.array([125,255,255])
rojo1 = np.array([0,100,20])
rojo2 = np.array([5,255,255])
rojo3 = np.array([175,100,20])
rojo4 = np.array([179,255,255])
mascara1 = cv2.inRange(hsv, rojo1, rojo2)
mascara2 = cv2.inRange(hsv, rojo3, rojo4)
mascararojo = cv2.add(mascara1, mascara2)
kernel = np.ones((7,7),np.uint8)
#azul
mascarazul = cv2.inRange(hsv, azul1, azul2)
mascararojo = cv2.add(mascara1, mascara2)
mascararojoazul= cv2.add(mascararojo, mascarazul)
#verde
mascaraverde = cv2.inRange(hsv, verde1, verde2)
#union de mascaras
mascara = cv2.add(mascaraverde, mascararojoazul)
print(len(mascara))
#morfologia de mascaras
#mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
#mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
resultado = cv2.bitwise_and(img, img, mask=mascara)
resultado[mascara>0]=(10,155,25)
cv2.imwrite("mascara.jpg", resultado)
alpha = 0.9 #influencia de la primera imagen
beta = 0.9 #peso de influencia de la segunda imagen
gamma = 0 # Valor de compensación
union = cv2.addWeighted(img, alpha, resultado, beta, gamma)
cv2.imshow("Conca", union)
cv2.imshow("Mascara", resultado)
cv2.imshow("Imagen1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
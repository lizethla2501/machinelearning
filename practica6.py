# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 08:11:46 2026

@author: lizal
"""

import cv2
img= cv2.imread("imagenes.png")
img1= cv2.imread("imagenes.png")
alto,ancho,_=img.shape
alto1,ancho1,_=img1.shape

if(alto+ancho)>(alto1+ancho1):
    img=cv2.resize(img, (ancho1,alto1))
else:
    img1=cv2.resize(img1, (ancho,alto))
alpha=1#INFLUENCIA DE LA PRIMERA IMAGEN
beta= 0.5#peso de influencia de la 2da imagen
gamma=0 #valor de compensacion

resultado= cv2.addWeighted(img, alpha, img1, beta, gamma)
cv2.imwrite("resultado.jpg", resultado)
resultado= cv2.imread("resultado.jpg")
cv2.imshow("Resultado", resultado)
cv2.imshow("Imagen", img)
cv2.imshow("Imagen1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 10:37:19 2026

@author: lizal
"""
import cv2 
import easygui as vent
import numpy as np
def encontrarContorno (img):
    img = cv2.imread(img)
    img = cv2.resize(img, (600, 600))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, valor = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)
    contornos, _ = cv2.findContours(figura,
                                    cv2.RETR_EXTERNAL,
                                    #cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)
    if len(contornos) == 0:
        return None,img
    contornoprincipal = max(contornos, key=cv2.contourArea)
    return contornoprincipal,img, figura    

imagen1 = vent.fileopenbox(msg='Abrir imagen', title='Abrir imagen', default='', filetypes=['*.png'])
contorno1 , img1 , figura1 = encontrarContorno(imagen1)

imagen2 = vent.fileopenbox(msg='Abrir imagen', title='Abrir imagen', default='', filetypes=['*.png'])
contorno2 , img2 , figura2 = encontrarContorno(imagen2)

if contorno1 is None and contorno2 is None:
    print('Alguna imagen no tiene contorno')
else:
    similitud = cv2.matchShapes(contorno1, contorno2, cv2.CONTOURS_MATCH_I1, 0)

    if similitud < 0.01:
        print('Las imagenes son iguales')
    else:
        print('Las imagenes no son iguales')
        

cv2.namedWindow('Imagen', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen', img1)

cv2.namedWindow('Imagen 1', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen 1', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

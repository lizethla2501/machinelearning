# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:17:57 2026

@author: lizal
"""

import cv2 
import easygui as vent
import numpy as np
import pyttsx3

voz = pyttsx3.init()
voces = voz.getProperty('voices')
velocidad = voz.setProperty('rate', 150)
volumen = voz.setProperty('volume', 1.0)
voz.setProperty('voice', voces[0].id)


def extraerCaracteristicas(imagen):
    img = cv2.imread(imagen)
    img = cv2.resize(img, (600, 600))
    copia = img.copy()
    copia = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create(nfeatures=150)
    pr, d = sift.detectAndCompute(copia, None)
    return img, pr, d
    
def compararimgenes(pr,d,pr2,d2):
    bf = cv2.BFMatcher()
    concidencias = bf.knnMatch(d, d2, k=2)
    caracteristicas = []
    for a in concidencias:
        if len(a) == 2:
            c, b = a
            if c.distance < 0.6 * b.distance:
                caracteristicas.append(c)

    if max(len(pr), len(pr2)) > 0:
        similitud = len(caracteristicas) / min(len(pr), len(pr2))
    else:
        similitud = 0
        
    return similitud, caracteristicas
                

imagen1 = vent.fileopenbox(msg='Abrir imagen', title='Abrir imagen', default='', filetypes=['*.png'])
img, pr, d = extraerCaracteristicas(imagen1)


 
imagen2 = vent.fileopenbox(msg='Abrir imagen', title='Abrir imagen', default='', filetypes=['*.png'])
img2, pr2, d2 = extraerCaracteristicas(imagen2)



if img is None or img2 is None:
    print("Error al Cargar")
else:
    similitud,caracteristicas = compararimgenes(pr,d,pr2,d2)
    print("Puntos de referencia de la imagen 1", len(pr))
    print("Puntos de referencia de la imagen 2", len(pr2))
    print("Caracteristicas encontradas", len(caracteristicas))
    print("Similitud", similitud)
    voz.say("Los objetos tienen")
    sim= round(similitud,2)
    voz.say(sim)
    voz.say(" % de similitud")
    

    resultado = cv2.drawMatches(img, pr, img2, pr2, caracteristicas, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    if similitud > 0.5 and len(caracteristicas) > 30:
        print("es la misma imagen")
        voz.say("es la misma imagen")
        
    else:
        print("no es la misma imagen")
        voz.say("no es la misma imagen")
        
    



cv2.namedWindow('Imagen1', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen1', img)

cv2.namedWindow('Imagen2', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen2', img2)

cv2.namedWindow('Resultado', cv2.WINDOW_NORMAL)
cv2.imshow('Resultado', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
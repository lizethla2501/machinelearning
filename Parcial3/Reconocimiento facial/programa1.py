# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:30:57 2026

@author: lizal
"""

import cv2
import pytesseract
import pyttsx3 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

texto= cv2.imread("texto.png")
gris= cv2.cvtColor(texto, cv2.COLOR_BGR2GRAY)
salida= pytesseract.image_to_string(gris)
print(salida)
voz = pyttsx3.init()
voces = voz.getProperty('voices')
voz.setProperty('rate',150)
voz.setProperty('volumen', 1)
voz.setProperty('voice',voces[0].id)
voz.say(salida)
voz.runAndWait()


# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:52:08 2026

@author: lizal
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 

texto= cv2.imread("texto.png")
texto= cv2.resize(texto, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) #hacer interpolacion para el texto.
gris= cv2.cvtColor(texto, cv2.COLOR_BGR2GRAY)
gris= cv2.GaussianBlur(gris, (5,5), 0)

_,resp= cv2.threshold(gris, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

config= '--psm 6'
salida= pytesseract.image_to_string(gris,lang='spa', config=config)
print(salida)  
cv2.imshow("Imagen en gris", gris)

cv2.waitKey(0)
cv2.destroyAllWindows()
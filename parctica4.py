# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 10:44:41 2026

@author: lizal
"""

import cv2
import numpy as np

# 1. Cargar la imagen original
img = cv2.imread("1.jpg")

alto, ancho, _ = img.shape

print(alto,ancho)

# 2. Realizar los recortes (Slicing)
parte1 = img[0:, 0:480]    # Mitad izquierda
parte2 = img[0:, 480:960]  # Mitad derecha

# 3. Crear una línea negra de separación (10 píxeles de ancho)
alto, ancho, canales = parte1.shape
separador = np.zeros((alto, 10, canales), dtype=np.uint8)

# 4. Unir las partes con la línea en medio
unidas = cv2.hconcat([parte1, separador, parte2])

# --- MOSTRAR TODAS LAS VENTANAS ---

# Ventana 1: La imagen completa original
cv2.namedWindow("1. Original", cv2.WINDOW_NORMAL)
cv2.imshow("1. Original", img)

# Ventana 2: Solo la mitad izquierda
cv2.namedWindow("2. Mitad Izquierda", cv2.WINDOW_NORMAL)
cv2.imshow("2. Mitad Izquierda", parte1)

# Ventana 3: Solo la mitad derecha
cv2.namedWindow("3. Mitad Derecha", cv2.WINDOW_NORMAL)
cv2.imshow("3. Mitad Derecha", parte2)

# Ventana 4: Las dos mitades juntas con la separación
cv2.namedWindow("4. Concatenadas con Separador", cv2.WINDOW_NORMAL)
cv2.imshow("4. Concatenadas con Separador", unidas)

cv2.waitKey(0)
cv2.destroyAllWindows()
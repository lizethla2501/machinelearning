# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 09:21:06 2026

@author: lizal
"""

# Importación de librerías
import cv2
import easygui as vent
import numpy as np

# Abrir ventana para seleccionar una imagen
imagen = vent.fileopenbox(msg="Abrir Imagen", title="Abrir",
                          default="", filetypes=["*.jpg"])

# Leer la imagen seleccionada
img = cv2.imread(imagen)

# Crear una copia de la imagen original para procesarla
copia = img.copy()

# Convertir la copia a escala de grises
copia = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)

# Aplicar filtro Gaussian Blur para reducir ruido
copia = cv2.GaussianBlur(copia, (5,5), 0)

# Aplicar threshold (umbralización)
# Los valores mayores a 200 se vuelven blancos y los menores negros
_, valor = cv2.threshold(copia, 200, 255, cv2.THRESH_BINARY)

# Crear kernel de 5x5 para operaciones morfológicas
kernel = np.ones((5,5), np.uint8)

# Aplicar operación morfológica de cierre (closing)
# Sirve para cerrar pequeños huecos en los objetos
figura = cv2.morphologyEx(valor, cv2.MORPH_CLOSE, kernel)

# Detectar bordes usando el algoritmo Canny
bordes = cv2.Canny(figura, 3, 3)

# Encontrar contornos de las figuras detectadas
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos sobre la imagen original
cv2.drawContours(img, contornos, -1, (0,255,0), 2)

# Mostrar la imagen con bordes detectados
cv2.namedWindow("Canny", cv2.WINDOW_NORMAL)
cv2.imshow("Canny", bordes)

# Mostrar la imagen en escala de grises procesada
cv2.namedWindow("VentanaGris", cv2.WINDOW_NORMAL)
cv2.imshow("VentanaGris", copia)

# Mostrar la imagen original con los contornos dibujados
cv2.namedWindow("Ventana", cv2.WINDOW_NORMAL)
cv2.imshow("Ventana", img)

# Esperar a que el usuario presione una tecla
cv2.waitKey()

# Cerrar todas las ventanas
cv2.destroyAllWindows()

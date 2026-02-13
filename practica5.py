# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 07:29:23 2026

@author: lizal
"""

import cv2
img1= cv2.imread("1.jpg")
img= img1.copy()
roi= cv2.selectROI("ROI",img)
nuevaImagen= img[int(roi[1]):int(roi[1]+roi[3]),#posicion x
                 int(roi[0]):int(roi[0]+roi[2])]#posicion y
alto,ancho,_=nuevaImagen.shape
nuevaImagen=cv2.resize(nuevaImagen,(alto,ancho))

cv2.imwrite("recorte.jpg", nuevaImagen)
recorte= cv2.imread("recorte.jpg")
cv2.imshow("Recorte", recorte)
R,G,B= cv2.split(recorte)

while(True):
    if cv2.waitKey(1) & 0xFF == ord('a'):
        print("Presionaste la letra A")
        cv2.imshow("R", R)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("Presionaste la letra S")
        cv2.imshow("G", G)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        print("Presionaste la letra D")
        cv2.imshow("B", B)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("SALIR")
        break
#cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
# bcv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
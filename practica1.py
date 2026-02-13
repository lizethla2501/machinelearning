# -*- coding: utf-8 -*-


import cv2
from tkinter import messagebox
import easygui as ventana
extension = ["*.jpg","*.png","*.gif"]
imagen = ventana.fileopenbox(msg="Abrir archivo",
                          title="Buscador de Imagenes", 
                          default="",
                          filetypes=extension)

print(imagen[len(imagen)-3:])
ext = imagen[len(imagen)-3:]
if ext in ["jpg","png","gif"]:
    print("Correcto")
    img=cv2.imread(imagen)
    alto,ancho,_= img.shape
    print(alto,ancho)
    copia = img.copy()
    copia = cv2.resize(copia, (0,0),fx = 0.5,fy = 0.5)
    alto2, ancho2,_=copia.shape
    cv2.imwrite("Copia.jpg", copia)
    #cv2.namedWindow("Imagen", cv2.WINDOW_NORMAL)
    cv2.imshow("Imagencopia", copia)
    cv2.imshow("Imagen", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")
    messagebox.showinfo("Error","Imagen incorrecta")
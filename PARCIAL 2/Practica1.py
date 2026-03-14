# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 07:31:43 2026
@author: lizal
"""
import cv2
import easygui as vent
ib=False
ig= False
im= False
iq= False
imagen = vent.fileopenbox(msg="Abrir Imagen", title="Abrie",
                           default="",filetypes=["*.jpg"])
img= cv2.imread("images.jpg")
cv2.namedWindow("Ventana",cv2.WINDOW_NORMAL)
cv2.imshow("Ventana",img)
# Aplicar filtro Blur (suavizado simple)
# Este filtro reduce el ruido promediando los píxeles vecinos
imgblur = cv2.blur(img, (8,8))

# Crear una ventana redimensionable para mostrar la imagen con Blur
cv2.namedWindow("VentanaBlur", cv2.WINDOW_NORMAL)

# Mostrar la imagen suavizada con el filtro Blur
cv2.imshow("VentanaBlur", imgblur)


# Aplicar filtro Gaussian Blur
# Este filtro suaviza la imagen usando una distribución gaussiana
# Ayuda a reducir ruido pero mantiene mejor los bordes
imgGauss = cv2.GaussianBlur(img, (5,5), 6)

# Crear una ventana para mostrar el resultado del filtro Gaussiano
cv2.namedWindow("Ventana Gaus", cv2.WINDOW_NORMAL)

# Mostrar la imagen con el filtro Gaussian Blur
cv2.imshow("Ventana Gaus", imgGauss)


# -----------------------------

# Aplicar filtro Median Blur
# Este filtro elimina ruido fuerte como el ruido "sal y pimienta"
# Reemplaza cada píxel por la mediana de sus vecinos
imgMedian = cv2.medianBlur(img, 5)

# Crear ventana para mostrar el resultado
cv2.namedWindow("Ventana Median", cv2.WINDOW_NORMAL)

# Mostrar la imagen con el filtro Median Blur
cv2.imshow("Ventana Median", imgMedian)


# -----------------------------

# Convertir la imagen a escala de grises
# Esto elimina los colores y deja solo niveles de intensidad
imgris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar ecualización de histograma
# Sirve para mejorar el contraste de la imagen
imgequa = cv2.equalizeHist(imgris)

# Crear ventana para mostrar la imagen con contraste mejorado
cv2.namedWindow("Ventana Equa", cv2.WINDOW_NORMAL)

# Mostrar la imagen ecualizada
cv2.imshow("Ventana Equa", imgequa)
while(True):
    key= cv2.waitKey()
    if key== ord("b") and ib== False:
        ib=True
        archivo= vent.filesavebox(msg="Guardar Imagen Blur",title="GuardarBlur",
                                  default="",filetypes=["*.jpg*"])
        cv2.imwrite(archivo, imgblur)
    elif key== ord("b") and ib== True:
        vent.msgbox(msg="Imagen Guardada",title="Correcto")
    
    if key== ord("g") and ig== False:
       
        archivo= vent.filesavebox(msg="Guardar Imagen Gauss",title="GuardarGauss",
                                  default="",filetypes=["*.jpg*"])
       
        cv2.imwrite(archivo, imgGauss)
        ig=True
    elif key== ord("g") and ig== True:
         vent.msgbox(msg="Imagen Guardada",title="Correcto")
         
    if key== ord("m") and im== False:
        archivo= vent.filesavebox(msg="Guardar Imagen Median",title="GuardarMedian",
                                  default="",filetypes=["*.jpg*"])
        cv2.imwrite(archivo, imgMedian)
        im=True
    elif key== ord("m") and im== True:
         #messagebox.showerror("La imagen ya se guardo","Error")
         vent.msgbox(msg="Imagen Guardada",title="Correcto")
    
    if key== ord("e") and iq== False:
      
        archivo= vent.filesavebox(msg="Guardar Imagen Equa",title="GuardarEqua",
                                  default="",filetypes=["*.jpg*"])
        cv2.imwrite(archivo, imgequa)
        iq=True
    elif key== ord("e") and iq== True:
         vent.msgbox(msg="Imagen Guardada",title="Correcto")
         
    if key== ord('q'):
        vent.msgbox("Salir")
    break        


cv2.waitKey()
cv2.destroyAllWindows()
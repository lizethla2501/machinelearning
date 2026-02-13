# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 11:29:41 2026

@author: lizal
"""




import numpy as np
import cv2
img= cv2.imread("colores.jpg")
cv2.putText(img,"colores a cambiar",
            (10,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0,0,255),
            2)
hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Rojo
#rojo claro1: 0,100,20
#rojo oscuro1: 5,255,255
#rojo claro2: 175,100,20
#rojo esocuro2: 179,255,255


rojo1= np.array([0,100,20])
rojo2= np.array([5,255,255])
rojo3= np.array([175,100,20])
rojo4= np.array([179,255,255])
kernel1= np.ones((7,7),np.uint8)

mascara1= cv2.inRange(hsv,rojo1, rojo2)
mascara2= cv2.inRange(hsv,rojo3, rojo4)
mascara=cv2.add(mascara1,mascara2 )
mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel1)
mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN , kernel1)


resultado= cv2.bitwise_and(img, img, mask=mascara)
contorno,_= cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for i in contorno:
    area= cv2.contourArea(i)
    if area >500:
        cv2.drawContours(resultado, [i], -1, (255,0,0),3)
        print(area)
        x,y,w,h= cv2.boundingRect(i)
        areas= f"area:{int(area)}"
        cv2.putText(resultado, areas,(x,y),cv2.FONT_HERSHEY_SIMPLEX,
                1,(255,0,0), 2)
        
        
        
        

cv2.imshow("Resultado", resultado)
cv2.imshow("mascara", mascara)
cv2.imshow("Imagen1", img)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

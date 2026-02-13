# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 10:26:50 2026

@author: lizal
"""

import cv2
img= cv2.imread("1.jpg")
img2= img.copy()
img2= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Gris.jpg", img2)
img2 =cv2.imread("Gris.jpg")
#cv2.namedWindow("Gris",cv2.WINDOW_NORMAL)
#cv2.imshow("Gris", img2)

dosimagenes = cv2.hconcat([img,img2])
cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
cv2.imshow("Imagen", dosimagenes)

cv2.waitKey(0)
cv2.destroyAllWindows()
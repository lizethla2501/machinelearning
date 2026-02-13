# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 09:36:48 2026

@author: lizal
"""

import cv2
img= cv2.imread("1.jpg")
copia= img.copy()
img2=cv2.cvtColor(copia,cv2.COLOR_BGR2HSV)
H,S,V=cv2.split(img2)
cv2.namedWindow("H",cv2.WINDOW_NORMAL)
cv2.imshow("H", H)
cv2.imwrite("H.jpg", copia)
 
cv2.namedWindow("S",cv2.WINDOW_NORMAL)
cv2.imshow("S", S)
cv2.imwrite("S.jpg", copia)

cv2.namedWindow("V",cv2.WINDOW_NORMAL)
cv2.imshow("V", V)
cv2.imwrite("V.jpg", copia)
R,G,B= cv2.split(img)

cv2.namedWindow("R",cv2.WINDOW_NORMAL)
cv2.imshow("R", R)
cv2.imwrite("R.jpg", copia)

cv2.namedWindow("G",cv2.WINDOW_NORMAL)
cv2.imshow("G", G)
cv2.imwrite("G.jpg", copia)

cv2.namedWindow("B",cv2.WINDOW_NORMAL)
cv2.imshow("B", B)
cv2.imwrite("B.jpg", copia)
cv2.waitKey(0)
cv2.destroyAllWindows()
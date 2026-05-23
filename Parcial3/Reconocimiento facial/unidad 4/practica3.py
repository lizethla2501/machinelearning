# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:04:42 2026

@author: lizal
"""

import cv2
import mediapipe as mp
import numpy as np

img = cv2.imread("lentes.png", cv2.IMREAD_UNCHANGED)
mp_face_mesh = mp.solutions.face_mesh
face_ojos = mp_face_mesh.FaceMesh(refine_landmarks = True)
camara = cv2.VideoCapture(0)

while True:
    r, frame = camara.read()
    if not r:
        break
    frame = cv2.flip(frame, 1)
    alto, ancho, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = face_ojos.process(frame_rgb)
    if resultados.multi_face_landmarks:
        for rostros in resultados.multi_face_landmarks:
            ojo_izquierdo = rostros.landmark[33]
            ojo_derecho = rostros.landmark[263]
            x_izquierdo = int(ojo_izquierdo.x * ancho)
            y_izquierdo = int(ojo_izquierdo.y * alto)
            x_derecho = int(ojo_derecho.x * ancho)
            y_derecho = int(ojo_derecho.y * alto)
            
            distancia = int (np.sqrt((x_derecho - x_izquierdo)**2 + (y_derecho - y_izquierdo)**2))
            ancho_lente = int(distancia*2)
            
            alto_lente = int(
                ancho_lente * img.shape[0] / img.shape[1]
            )
            lentes_ajustar = cv2.resize(img, (ancho_lente, alto_lente))
            x_lente = int((x_izquierdo + x_derecho) // 2 - ancho_lente // 2)
            y_lente = int((y_izquierdo + y_derecho) // 2 - alto_lente // 2)
            if x_lente < 0:
                x_lente = 0
            if y_lente < 0:
                y_lente = 0
            if lentes_ajustar.shape[2] == 4:
                imgT = lentes_ajustar[:,:,:3]
                mascara = lentes_ajustar[:,:,3] / 255.0
                h, w, _= imgT.shape
                if y_lente + h <alto and x_lente + w < ancho:
                    roi = frame[y_lente:y_lente + h, x_lente:x_lente + w]
                    for c in range(3):
                        roi[:, :, c] = imgT[:, :, c] * mascara + roi[:, :, c] * (1 - mascara)
                    frame[y_lente:y_lente + h, x_lente:x_lente + w] = roi
            

    cv2.imshow("imagen", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
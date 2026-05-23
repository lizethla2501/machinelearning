# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:22:19 2026

@author: lizal
"""

import cv2
import mediapipe as mp
import numpy as np
import math

mp_olistico = mp.solutions.holistic
mp_trazo = mp.solutions.drawing_utils
mp_trazo_estilo = mp.solutions.drawing_styles
def contar_dedos():
    camara = cv2.VideoCapture(0)
    camara.set(3, 640)
    camara.set(4, 480) 
    holistic = mp_olistico.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    while True:
        r, frame = camara.read()
        if not r:
            break
        frame = cv2.flip(frame, 1)
        rbg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultados = holistic.process(rbg)
        #mano izquierda
        mp_trazo.draw_landmarks(frame, resultados.left_hand_landmarks,
                                mp_olistico.HAND_CONNECTIONS)
        mp_trazo.draw_landmarks(frame, resultados.right_hand_landmarks,
                                mp_olistico.HAND_CONNECTIONS)
        if resultados.left_hand_landmarks and resultados.right_hand_landmarks:
            dedos = 0
            if resultados.left_hand_landmarks.landmark:
                    dedos += contar(resultados.left_hand_landmarks)

            if resultados.right_hand_landmarks.landmark:
                 dedos += contar(resultados.right_hand_landmarks)
        
            cv2.putText(frame, f"Dedos: {dedos}", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                            3, (0, 255, 0), 3)

        cv2.imshow("Contar dedos", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    camara.release()
    cv2.destroyAllWindows()

def contar(hand_landmarks):
    dedos_indices = [8, 12, 16, 20]  # puntas de dedos
    dedos_contados = 0

    # dedos (índice, medio, anular, meñique)
    for i in dedos_indices:
        if hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y:
            dedos_contados += 1

    # pulgar (se mide horizontalmente)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        dedos_contados += 1

    return dedos_contados


def calcular_distancia(puntoDedo , puntoMuñeca):
    x1 , y1 , z1 = puntoDedo.x, puntoDedo.y, puntoDedo.z
    x2 , y2 , z2 = puntoMuñeca.x, puntoMuñeca.y, puntoMuñeca.z
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distancia
   


if __name__ == "__main__":
    contar_dedos()
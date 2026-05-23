# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:40:06 2026

@author: lizal
"""

import cv2 
import face_recognition
import pyttsx3

def HablarIA(texto):
    hablar = pyttsx3.init()
    voces = hablar.getProperty('voices')
    hablar.setProperty('voice', voces[0].id)
    velocidadVoz = hablar.getProperty('rate')
    hablar.setProperty('rate', velocidadVoz-800)
    hablar.say(texto)
    hablar.runAndWait()

caras = []
nombres = []

persona1 = face_recognition.load_image_file('liz.jpg')
persona2 = face_recognition.load_image_file('cazzu.jpg')

if face_recognition.face_encodings(persona1):
    persona1encontrada = face_recognition.face_encodings(persona1)[0]
    caras.append(persona1encontrada)
    nombres.append('Liz Lopez')
if face_recognition.face_encodings(persona2):
    persona2encontrada = face_recognition.face_encodings(persona2)[0]
    caras.append(persona2encontrada)
    nombres.append('Cazzu Baby')

camara = cv2.VideoCapture(0)
camara.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camara.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("frame", 640, 480)
while True:
    r, frame = camara.read()
    if not r:
        break
    
    carasEncontradas = face_recognition.face_locations(frame)
    caras_codes_frame = face_recognition.face_encodings(frame, carasEncontradas)
    for (arriba, derecha, abajo, izquierda), caras_codes in zip(carasEncontradas, caras_codes_frame):
        puntos = face_recognition.compare_faces(caras, caras_codes)
        nombre = "sin nombre"
        if True in puntos:
            primerPunto = puntos.index(True)
            nombre = nombres[primerPunto]
            print(nombre)
        cv2.rectangle(frame,(izquierda, arriba),(derecha, abajo), (0,255,0), 2)
        HablarIA(f'El nombre de la persona encontrada es {nombre}')
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
camara.release()
cv2.destroyAllWindows()
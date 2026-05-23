# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:13:28 2026

@author: lizal
"""

import cv2 
import mediapipe as mp
 
mp_cara_mesh = mp.solutions.face_mesh
face_mesh = mp_cara_mesh.FaceMesh(max_num_faces=2 , refine_landmarks=True )
dibujo = mp.solutions.drawing_utils
aspecto = dibujo.DrawingSpec(thickness=1 , circle_radius=1 , color=(0,255,0))

camara = cv2.VideoCapture(0)
while True:
    r , frame = camara.read()
    if not r:
        break
    frame = cv2.flip(frame , 1)
    rgb_img = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    resultado = face_mesh.process(rgb_img)
    if resultado.multi_face_landmarks:
        for rostros in resultado.multi_face_landmarks:
            dibujo.draw_landmarks(image = frame , landmark_list = rostros ,
                                   connections = mp_cara_mesh.FACEMESH_TESSELATION , 
                                   landmark_drawing_spec = aspecto , connection_drawing_spec = aspecto)
            
    cv2.imshow('frame' , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camara.release()
cv2.destroyAllWindows()
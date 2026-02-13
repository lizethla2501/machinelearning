# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 08:37:05 2026

@author: lizal
"""

import cv2
from moviepy.editor import VideoFileClip
import pygame

# Cargar video con moviepy
videoReal = VideoFileClip("video.mp4")
audio = videoReal.audio

# Inicializar pygame
pygame.mixer.init()
audio.write_audiofile("temp_audio.wav")
pygame.mixer.music.load("temp_audio.wav")
pygame.mixer.music.play()

# Cargar video con OpenCV
video = cv2.VideoCapture("video.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
print(fps)
tiempo = int(1000 / fps)


while True:
    f, frame = video.read()
    if not f:
        break

    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(tiempo) & 0xFF == ord('a'):
        break

video.release() 
cv2.destroyAllWindows()
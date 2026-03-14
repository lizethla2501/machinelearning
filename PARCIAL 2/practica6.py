# -*- coding: utf-8 -*-
"""
Created on Thu Mar 5 07:56:42 2026
@author: lizal
"""

# Programa que usa la cámara web para grabar video
# También utiliza un sistema de voz que indica cuando
# inicia y termina la grabación.
import cv2              # Librería OpenCV para trabajar con video e imágenes
import pyttsx3          # Librería para convertir texto a voz
import datetime         # Librería para manejar fechas y horas

# Obtiene los segundos actuales del sistema
# Se usan para crear un nombre diferente para el archivo de video
hoy = datetime.datetime.second
# Inicializa el motor de voz
voz = pyttsx3.init()
# Obtiene la lista de voces disponibles en el sistema
voces = voz.getProperty('voices')
# Configura la velocidad de la voz
voz.setProperty('rate',150)
# Configura el volumen de la voz
voz.setProperty('volumen', 1)
# Selecciona una voz específica de la lista
voz.setProperty('voice',voces[2].id)
# Activa la cámara web (0 indica la cámara principal)
camara = cv2.VideoCapture(0)

# Configura el archivo donde se guardará el video
salida = cv2.VideoWriter(
    'video' + str(hoy) + '.avi',     # nombre del archivo de video
    cv2.VideoWriter_fourcc(*'XVID'), # formato de compresión del video
    20.0,                            # cuadros por segundo (FPS)
    (640,480)                        # resolución del video
)

# Mientras la cámara esté activa
while(camara.isOpened()):
    # Lee un frame (imagen) de la cámara
    f, frame = camara.read()

    # Si el frame se capturó correctamente
    if f == True:
        # El sistema de voz dice que la grabación inició
        voz.say("Grabacion iniciada")
        # Invierte la imagen horizontalmente (efecto espejo)
        frame = cv2.flip(frame, 1)
        # Muestra el frame en una ventana
        cv2.imshow("Frame", frame)
        # Guarda el frame en el archivo de video
        salida.write(frame)
        # Espera 1 milisegundo para detectar una tecla
        key = cv2.waitKey(1)
        # Si se presiona la tecla "a"
        if key == ord('a'):
            # El sistema de voz indica que la grabación terminó
            voz.say("Grabacion terminada")
            # Sale del ciclo
            break
    else:
        # Ejecuta el motor de voz
        voz.runAndWait()
        break
# Libera la cámara
camara.release()
# Libera el archivo de video
salida.release()
# Cierra todas las ventanas de OpenCV
cv2.destroyAllWindows()

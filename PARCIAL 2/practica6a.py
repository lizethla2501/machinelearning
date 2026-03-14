# -*- coding: utf-8 -*-
"""
Created on Thu Mar 5 08:20:34 2026
@author: lizal
"""

# Programa simple que convierte texto a voz
# El usuario escribe una palabra o frase y el programa la reproduce en audio

import pyttsx3   # Librería que permite convertir texto a voz

# Inicializa el motor de voz
voz = pyttsx3.init()

# Obtiene la lista de voces disponibles en el sistema
voces = voz.getProperty('voices')

# Configura la velocidad con la que hablará la voz
# (150 es una velocidad normal)
voz.setProperty('rate',150)

# Configura el volumen de la voz
# El rango va de 0 a 1
voz.setProperty('volumen', 1)

# Selecciona una voz específica de la lista
# voces[0] normalmente es la primera voz disponible
voz.setProperty('voice',voces[0].id)

# Pide al usuario que escriba una palabra o frase
hablar = input("Escribe la palabra o frase a decir")

# El motor de voz reproduce el texto que escribió el usuario
voz.say(hablar)

# Ejecuta el motor de voz para que el sonido se reproduzca
voz.runAndWait()

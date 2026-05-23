 # -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 07:42:40 2026

@author: lizal
"""

import speech_recognition as sr
import pyttsx3
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
from datetime import datetime
import cv2
import  os
import numpy as np
import json
import subprocess


listener= sr.Recognizer()
def escucharIA():
    while True: 
        with sr.Microphone()as source:
            print("Escuchando....")
            audio= listener.listen(source, phrase_time_limit=5)
            try:
                print("Reconociendo....")
                text= listener.recognize_google(audio, language='es-US').lower()
                print(text)
                break
            except Exception:
                print("No te entendi")
                HablarIA("No te entiendo")
    return text
  
def HablarIA(texto):
    hablar= pyttsx3.init()
    voces= hablar.getProperty('voices')
    hablar.setProperty('voice', voces[0].id)
    velocidadVoz= hablar.getProperty('rate')
    hablar.setProperty('rate', velocidadVoz-500)
    hablar.say(texto)
    hablar.runAndWait()
    
def DecirChiste():
    chiste= pyjokes.get_joke(language='es',category='neutral')
    HablarIA(chiste)
    
def BuscarYoutube(comando):
    #buscar= comando.replace('buscar en youtube','').trip()
    op= comando.find('youtube')
    buscar = comando[op+8:]
    print(buscar)
    pywhatkit.search(buscar)

def BuscarGoogle(comando):
    buscar  = ''
    print('google')
    op= comando.find('google')
    buscar = comando[op+7:]
    print(buscar)
    pywhatkit.search(buscar)

def BuscarWiki(comando):
    wikipedia.set_lang('es')
    op= comando.find('wikipedia')
    buscar = comando[op+10:]
    print(buscar)
    resultado= wikipedia.summary(buscar, sentences=1)
    HablarIA(resultado)

def DecirHora(comando):
    print(f"La hora es {datetime.datetime.now().strftime('%H:%M')}")
    HablarIA(f"La hora es {datetime.datetime.now().strftime('%H:%M')}")

def DecirFecha(comando):
    print(f"La fecha es {datetime.now().date()}")
    HablarIA(f"La fecha es {datetime.now().date()}")

def CapturarPantalla(comando):
    HablarIA('pantalla')
    captura = pyautogui.screenshot()
    carpeta = r'C:\Users\lizal\OneDrive\Imágenes\Screenshots'
    archivo = datetime.now().strftime('%H-%M') + '.jpg'
    nombre = os.path.join(carpeta, archivo)
    captura.save(nombre)
    img_array = np.fromfile(nombre, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    if img is not None:
        cv2.namedWindow("Captura", cv2.WINDOW_NORMAL)
        cv2.imshow("Captura", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: No se pudo cargar la imagen para mostrarla.") 
def ComandosJson(comando):
    with open("comando.json","r",encoding="utf-8")as archivo:
        datos= json.load(archivo)
        
    if 'abre' in comando or 'abrir' in comando:
        for index in datos["abre"]:
            if index in comando:
                programa= datos['abre'][index]
                subprocess.Popen(programa)
HablarIA('Hola, en que te ayudo bebe')
while True:
    comando= None
    comando= escucharIA()
    print(comando)
    if 'chiste' in comando:
        DecirChiste()
    if 'youtube' in comando:
        BuscarYoutube(comando)
    if 'google' in comando:
        BuscarGoogle(comando)
    if 'wikipedia' in comando:
        BuscarWiki(comando)
    if 'La hora' in comando:
        DecirHora(comando)
    if 'La fecha' in comando:
        DecirFecha(comando)
    if 'pantalla' in comando:
        CapturarPantalla(comando)
    if 'abrir' in comando or 'abre' in comando:
        ComandosJson(comando)
        break
    if 'salir' in comando:
        HablarIA('camara')
        break































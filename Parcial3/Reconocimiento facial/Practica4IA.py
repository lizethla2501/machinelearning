# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 08:24:58 2026

@author: lizal
"""
import speech_recognition as sr
import pyttsx3
import pyjokes
#import cv2
from openai import OpenAI
listener = sr.Recognizer()
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
def DecirChiste():
    chiste= pyjokes.get_joke(language='es',category='neutral')
    HablarIA(chiste)
    
client= OpenAI(api_key="API-KEY-CHAT")

def buscarIA(comando):
    respuesta= client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role":"user","content":comando}
             ]
        )
    return respuesta.choices[0].message.content
def HablarIA(texto):
    hablar= pyttsx3.init()
    voces= hablar.getProperty('voices')
    hablar.setProperty('voice', voces[0].id)
    velocidadVoz= hablar.getProperty('rate')
    hablar.setProperty('rate', velocidadVoz-500)
    hablar.say(texto)
    hablar.runAndWait()

#HablarIA('Hola')
while True:
    print('primer ciclo')
    comando= None
    comando= escucharIA()
    if "luna" in comando:
        HablarIA('Hola guapa en que te ayudo')
        while True:
            print('segundo ciclo')
            comando= None
            comando= escucharIA()
            if "chiste" in comando:
                DecirChiste()
                break
            if "buscar" in comando or "busca" in comando:
                respuesta= buscarIA(comando)
                HablarIA(respuesta)
                break
            else:
                respuesta= buscarIA(comando)
                HablarIA(respuesta)
                break  
    break
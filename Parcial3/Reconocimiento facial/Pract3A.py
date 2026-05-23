
"""
Created on Fri Apr 24 10:26:20 2026

@author: lizal
"""

import json

datos = {
    "abre": {
        "calculadora": "calc.exe",
        "bloc de notas": "notepad.exe",
        "paint": "mspaint.exe",
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    },

    "chistes": {
        "cuenta un chiste": [
            "¿Por qué la computadora fue al doctor? Porque tenía un virus.",
            "¿Qué hace una abeja en el gimnasio? Zum-ba.",
            "¿Por qué los programadores confunden Halloween y Navidad? Porque OCT 31 = DEC 25."
        ]
    },

    "respuestas": {
        "hola": "Hola bebe, ¿en qué te ayudo?",
        "como estas": "Estoy muy bien",
        "adios": "Hasta luego"
    },

    "wikipedia": {
        "wikipedia": "buscar informacion"
    },

    "hora": {
        "hora": "decir hora actual"
    },

    "fecha": {
        "fecha": "decir fecha actual"
    }
}

with open("comando.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)

print("Archivo JSON creado correctamente")
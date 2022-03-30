# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:48:13 2021

@author: Jcc (Julio César Calderaro)

"""


from tkinter.messagebox import showinfo


def ayuda():
       showinfo('Encriptar archivos', '=== Instrucciones de uso ===''\n'
                '\nCon la opción Encriptar, se escoge el archivo a encriptar,''\n'
                'se presiona el botón Open y se confirman los mensajes''\n'
                'de información.''\n'
                'Para desencriptar un archivo, el procedimiento''\n'
                'es el mismo que para encriptar, seleccionando \n'
                'la opción correspondiente.')

    
def notas_adicionales():
        showinfo('Encriptar archivos', '=== Notas adicionales ===''\n'
             '\nEl archivo encriptado queda en la misma ubicación y con las mismas\n'
             'características (nombre y extensión).\n'
             '\nNo debe crearse una clave para encriptar y otra para desencriptar,''\n'
             'porque las claves son aleatorias e indistintas, es decir, si se''\n'
             'encripta con una clave, no se puede desencriptar con otra, porque''\n'
             'no tendrían relación alguna y se perdería el archivo.''\n'
             '\nSi un archivo no ha sido encriptado y trata de desencriptarse, la''\n'
             'aplicación dará un aviso, notificándolo.''\n'
             '\nSi se desea encriptar un archivo, con una nueva clave, primero''\n'
             'debe crearse la clave y luego encriptarlo.''\n'
             '\nSe recomienda, siempre tener una copia del archivo original.')
        
        

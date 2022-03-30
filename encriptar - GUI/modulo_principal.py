# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:17:27 2021

@author: Jcc (Julio César Calderaro)

"""

from cryptography.fernet import Fernet
      
        
def encriptar(nombre_archivo, clave):
    f = Fernet(clave)
    with open(nombre_archivo, 'rb') as file:
        archivo_info = file.read()
    data_encriptada = f.encrypt(archivo_info)
    with open(nombre_archivo, 'wb') as file:
        file.write(data_encriptada)

        
def desencriptar(nombre_archivo, clave):
    f = Fernet(clave)
    with open(nombre_archivo, 'rb') as file:
        archivo_info = file.read()
    data_desencriptada = f.decrypt(archivo_info)
    with open(nombre_archivo, 'wb') as file:
        file.write(data_desencriptada)

        
def generar_clave():
    clave = Fernet.generate_key()
    with open ('clave.key', 'wb') as archivo_clave:
        archivo_clave.write(clave)


def cargar_clave():
    return open('clave.key', 'rb').read()




    
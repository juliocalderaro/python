# -*- coding: utf-8 -*-
"""
Módulo principal para encriptación/desencriptación
@author: Jcc (Julio César Calderaro)
Actualizado: 2024
"""

from cryptography.fernet import Fernet
import os


def encriptar(nombre_archivo, clave):
    """Encripta un archivo usando la clave proporcionada"""
    try:
        f = Fernet(clave)
        with open(nombre_archivo, 'rb') as file:
            archivo_info = file.read()
        data_encriptada = f.encrypt(archivo_info)
        with open(nombre_archivo, 'wb') as file:
            file.write(data_encriptada)
        return True
    except Exception as e:
        raise Exception(f"Error al encriptar: {str(e)}")


def desencriptar(nombre_archivo, clave):
    """Desencripta un archivo usando la clave proporcionada"""
    try:
        f = Fernet(clave)
        with open(nombre_archivo, 'rb') as file:
            archivo_info = file.read()
        data_desencriptada = f.decrypt(archivo_info)
        with open(nombre_archivo, 'wb') as file:
            file.write(data_desencriptada)
        return True
    except Exception as e:
        raise Exception(f"Error al desencriptar: {str(e)}")


def generar_clave():
    """Genera una nueva clave de encriptación"""
    clave = Fernet.generate_key()
    with open('clave.key', 'wb') as archivo_clave:
        archivo_clave.write(clave)
    return clave


def cargar_clave():
    """Carga la clave de encriptación desde el archivo"""
    if not os.path.exists('clave.key'):
        raise FileNotFoundError("No existe el archivo de clave")
    with open('clave.key', 'rb') as file:
        return file.read()


def verificar_clave_existe():
    """Verifica si existe el archivo de clave"""
    return os.path.exists('clave.key')
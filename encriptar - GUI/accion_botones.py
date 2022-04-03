# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:35:03 2021

@author: Jcc (Julio César Calderaro)

"""

from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile
import os.path as path
from modulo_principal import encriptar, generar_clave, cargar_clave, desencriptar 
import time


def encriptar_archivos():
        try:
            generar_clave()
            clave = cargar_clave()
            nombre_archivo = askopenfile (filetypes = [('todos file', '*.*'), ('word file', '*.doc*'), ('excel file', '*.xls*')]) 
            nombre_archivo = nombre_archivo.name
            if nombre_archivo:
                verificar_clavekey()
                encriptar(nombre_archivo, clave)
                time.sleep(3)
                showinfo('Encriptar archivos', 'Finalizó encriptación')
        except:
            showinfo('Encriptar archivos', 'Cancelaste la operación.\nInténtalo de nuevo.')
            
            
def desencriptar_archivos():
        try:
            clave = cargar_clave()
            nombre_archivo = askopenfile (filetypes = [('todos file', '*.*'), ('word file', '*.doc*'), ('excel file', '*.xls*')]) 
            nombre_archivo = nombre_archivo.name
            if nombre_archivo:
                verificar_clavekey()
                desencriptar(nombre_archivo, clave)
                time.sleep(3)
                showinfo('Encriptar archivos', 'Finalizó desencriptación')
        except AttributeError:
            showinfo('Encriptar archivos', 'Cancelaste la operación.\nInténtalo de nuevo.')
        except:
            showinfo('Encriptar archivos', 'El archivo seleccionado no ha sido encriptado.\nInténtalo de nuevo.')
            
            
def crear_clave():
    generar_clave()
    showinfo('Encriptar archivos', 'Clave nueva creada')
  
    
def verificar_clavekey():
        if path.exists('clave.key'):
            showinfo('Encriptar archivos', 'Va a iniciarse el proceso')
        else:
            showinfo('Encriptar archivos', 'Debe generarse una clave')
            generar_clave()
        
        

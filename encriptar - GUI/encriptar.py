# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:23:09 2021

@author: Jcc (Julio César Calderaro)

"""

from tkinter import *
from tkinter import ttk
from accion_botones import *
from tkinter.messagebox import showinfo
from ayuda_notas import *
import os


class Principal:
    
    def __init__(self, master):
        # Inicializando
        self.master = master
        master.title('Encriptar')
        master.geometry('270x180')
        master.resizable(0, 0)
        
        # Titulo principal
        label = Label(master, text = 'Encriptar Archivos', fg = "blue", font = "Verdana 13")
        label.pack(side = 'top')

        # Frame principal
        marco = LabelFrame(master, text = 'Opciones', bd = 2, font = 'verdana 8 bold')
        marco.pack(expand = 'yes', fill = 'both')
        
        # Botones de accion
        boton = Button(marco, text = 'Encriptar', font = 'Verdana 9', 
                          width = 10, command = lambda:encriptar_archivos())
        boton.place(x=25, y=10)
        
        boton = Button(marco, text = 'Desencriptar', font = 'Verdana 9', 
                          width = 10, command = lambda:desencriptar_archivos())
        boton.place(x=25, y=40)
        
        boton = Button(marco, text = 'Crear nueva\nclave', font = 'Verdana 9', 
                          width = 10, command = lambda:crear_clave())
        boton.place(x=25, y=70)
        
        boton = Button(marco, text = 'Instrucciones', font = 'Verdana 9', 
                          width = 10, command = ayuda)
        boton.place(x=150, y=10)
        
        boton = Button(marco, text = 'Notas\n adicionales', font = 'Verdana 9', 
                          width = 10, command = notas_adicionales)
        boton.place(x=150, y=40)
        
        boton = Button(marco, text='Salir', font = 'Verdana 9 bold ', 
                          width = 10, command = master.destroy)
        boton.place(x=150, y=85)


if __name__=='__main__':
    master = Tk()
    application = Principal(master)
    master.mainloop()

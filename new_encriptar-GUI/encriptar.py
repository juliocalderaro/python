# -*- coding: utf-8 -*-
"""
Encriptador de Archivos - Interfaz Gráfica Principal
@author: Jcc (Julio César Calderaro)
Actualizado: 2024
"""

from tkinter import Tk, Label, LabelFrame, Button, Frame, Menu
from tkinter import PhotoImage
from accion_botones import (encriptar_archivos, desencriptar_archivos, 
                             crear_clave, exportar_clave, importar_clave)
from ayuda_notas import ayuda, notas_adicionales, acerca_de
import os
import sys


class EncriptadorApp:
    """Clase principal de la aplicación"""
    
    def __init__(self, master):
        self.master = master
        self.configurar_ventana()
        self.crear_menu()
        self.crear_interfaz()
        
    def configurar_ventana(self):
        """Configura la ventana principal"""
        self.master.title('Encriptador de Archivos v2.0')
        self.master.geometry('400x350')
        self.master.resizable(False, False)
        
        # Centrar ventana
        self.centrar_ventana(400, 350)
        
        # Configurar icono si existe
        try:
            self.master.iconbitmap('icono.ico')
        except:
            pass
    
    def centrar_ventana(self, ancho, alto):
        """Centra la ventana en la pantalla"""
        ancho_pantalla = self.master.winfo_screenwidth()
        alto_pantalla = self.master.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        self.master.geometry(f'{ancho}x{alto}+{x}+{y}')
    
    def crear_menu(self):
        """Crea la barra de menú"""
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        
        # Menú Archivo
        menu_archivo = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Encriptar archivo", command=encriptar_archivos)
        menu_archivo.add_command(label="Desencriptar archivo", command=desencriptar_archivos)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.master.quit)
        
        # Menú Herramientas
        menu_herramientas = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Herramientas", menu=menu_herramientas)
        menu_herramientas.add_command(label="Crear nueva clave", command=crear_clave)
        menu_herramientas.add_command(label="Exportar clave", command=exportar_clave)
        menu_herramientas.add_command(label="Importar clave", command=importar_clave)
        
        # Menú Ayuda
        menu_ayuda = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Instrucciones", command=ayuda)
        menu_ayuda.add_command(label="Notas adicionales", command=notas_adicionales)
        menu_ayuda.add_separator()
        menu_ayuda.add_command(label="Acerca de", command=acerca_de)
    
    def crear_interfaz(self):
        """Crea la interfaz gráfica"""
        # Frame del título
        frame_titulo = Frame(self.master, bg='#2c3e50', height=60)
        frame_titulo.pack(fill='x')
        frame_titulo.pack_propagate(False)
        
        # Título
        label_titulo = Label(
            frame_titulo,
            text='🔒 Encriptador de Archivos',
            fg='white',
            bg='#2c3e50',
            font=('Arial', 16, 'bold')
        )
        label_titulo.pack(expand=True)
        
        # Subtítulo
        label_subtitulo = Label(
            self.master,
            text='Protege tus archivos con encriptación segura',
            font=('Arial', 9),
            fg='#7f8c8d'
        )
        label_subtitulo.pack(pady=(10, 0))
        
        # Frame principal de botones
        frame_principal = LabelFrame(
            self.master,
            text=' Opciones Principales ',
            font=('Arial', 10, 'bold'),
            padx=20,
            pady=15
        )
        frame_principal.pack(padx=20, pady=15, fill='both', expand=True)
        
        # Botón Encriptar
        btn_encriptar = Button(
            frame_principal,
            text='🔐 Encriptar Archivo',
            font=('Arial', 11),
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            padx=20,
            pady=10,
            command=encriptar_archivos
        )
        btn_encriptar.pack(fill='x', pady=5)
        
        # Botón Desencriptar
        btn_desencriptar = Button(
            frame_principal,
            text='🔓 Desencriptar Archivo',
            font=('Arial', 11),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            padx=20,
            pady=10,
            command=desencriptar_archivos
        )
        btn_desencriptar.pack(fill='x', pady=5)
        
        # Frame de gestión de claves
        frame_claves = LabelFrame(
            self.master,
            text=' Gestión de Claves ',
            font=('Arial', 10, 'bold'),
            padx=20,
            pady=10
        )
        frame_claves.pack(padx=20, pady=(0, 15), fill='both')
        
        # Botones de claves en fila
        btn_crear = Button(
            frame_claves,
            text='Nueva\nClave',
            font=('Arial', 9),
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            width=10,
            command=crear_clave
        )
        btn_crear.grid(row=0, column=0, padx=3, pady=3)
        
        btn_exportar = Button(
            frame_claves,
            text='Exportar\nClave',
            font=('Arial', 9),
            bg='#f39c12',
            fg='white',
            activebackground='#d68910',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            width=10,
            command=exportar_clave
        )
        btn_exportar.grid(row=0, column=1, padx=5, pady=5)
        
        btn_importar = Button(
            frame_claves,
            text='Importar\nClave',
            font=('Arial', 9),
            bg='#9b59b6',
            fg='white',
            activebackground='#8e44ad',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            width=10,
            command=importar_clave
        )
        btn_importar.grid(row=0, column=2, padx=5, pady=5)
        
        # Footer
        label_footer = Label(
            self.master,
            text='© 2024 Jcc - Todos los derechos reservados',
            font=('Arial', 8),
            fg='#95a5a6'
        )
        label_footer.pack(side='bottom', pady=5)


def main():
    """Función principal"""
    root = Tk()
    app = EncriptadorApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
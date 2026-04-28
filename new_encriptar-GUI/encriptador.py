# -*- coding: utf-8 -*-
"""
Encriptador de Archivos v2.0 - Ejecutable GUI
@author: Jcc (Julio César Calderaro)
Actualizado: 2024

Archivo único consolidado que incluye:
- Módulo de encriptación/desencriptación
- Interfaz gráfica principal
- Acciones de botones
- Ventanas de ayuda e información
"""

import os
import sys
import shutil
from tkinter import (Tk, Label, LabelFrame, Button, Frame, Menu,
                     Toplevel, Text, Scrollbar, END, WORD)
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.filedialog import askopenfilename, asksaveasfilename
from cryptography.fernet import Fernet


# ╔══════════════════════════════════════════════════════════════════╗
# ║              MÓDULO DE ENCRIPTACIÓN / DESENCRIPTACIÓN            ║
# ╚══════════════════════════════════════════════════════════════════╝

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
    ruta_clave = obtener_ruta_clave()
    with open(ruta_clave, 'wb') as archivo_clave:
        archivo_clave.write(clave)
    return clave


def cargar_clave():
    """Carga la clave de encriptación desde el archivo"""
    ruta_clave = obtener_ruta_clave()
    if not os.path.exists(ruta_clave):
        raise FileNotFoundError("No existe el archivo de clave")
    with open(ruta_clave, 'rb') as file:
        return file.read()


def verificar_clave_existe():
    """Verifica si existe el archivo de clave"""
    return os.path.exists(obtener_ruta_clave())


def obtener_ruta_clave():
    """Obtiene la ruta del archivo de clave junto al ejecutable"""
    if getattr(sys, 'frozen', False):
        directorio = os.path.dirname(sys.executable)
    else:
        directorio = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(directorio, 'clave.key')


# ╔══════════════════════════════════════════════════════════════════╗
# ║                    ACCIONES DE BOTONES                           ║
# ╚══════════════════════════════════════════════════════════════════╝

FILTROS_ARCHIVO = [
    ('Todos los archivos', '*.*'),
    ('Documentos Word', '*.doc*'),
    ('Hojas Excel', '*.xls*'),
    ('PDFs', '*.pdf'),
    ('Imágenes', '*.jpg *.png *.gif'),
    ('Texto', '*.txt')
]


def encriptar_archivos():
    """Maneja el proceso de encriptación de archivos"""
    try:
        if not verificar_clave_existe():
            respuesta = askyesno(
                'Clave no encontrada',
                'No existe una clave de encriptación.\n'
                '¿Deseas crear una nueva?'
            )
            if respuesta:
                generar_clave()
                showinfo('Clave creada',
                         'Se ha generado una nueva clave de encriptación')
            else:
                return

        nombre_archivo = askopenfilename(
            title="Seleccionar archivo para encriptar",
            filetypes=FILTROS_ARCHIVO
        )

        if not nombre_archivo:
            return

        if askyesno('Confirmar encriptación',
                    f'¿Estás seguro de encriptar este archivo?\n\n'
                    f'{os.path.basename(nombre_archivo)}'):
            clave = cargar_clave()
            encriptar(nombre_archivo, clave)
            showinfo('Éxito',
                     f'El archivo fue encriptado correctamente:\n'
                     f'{os.path.basename(nombre_archivo)}')

    except FileNotFoundError:
        showerror('Error', 'Archivo no encontrado')
    except Exception as e:
        showerror('Error', f'Error al encriptar el archivo:\n{str(e)}')


def desencriptar_archivos():
    """Maneja el proceso de desencriptación de archivos"""
    try:
        if not verificar_clave_existe():
            showerror('Error',
                      'No existe una clave de encriptación.\n'
                      'No se puede desencriptar sin la clave correcta.')
            return

        nombre_archivo = askopenfilename(
            title="Seleccionar archivo para desencriptar",
            filetypes=FILTROS_ARCHIVO
        )

        if not nombre_archivo:
            return

        if askyesno('Confirmar desencriptación',
                    f'¿Estás seguro de desencriptar este archivo?\n\n'
                    f'{os.path.basename(nombre_archivo)}'):
            clave = cargar_clave()
            desencriptar(nombre_archivo, clave)
            showinfo('Éxito',
                     f'El archivo fue desencriptado correctamente:\n'
                     f'{os.path.basename(nombre_archivo)}')

    except FileNotFoundError:
        showerror('Error', 'Archivo no encontrado')
    except Exception as e:
        showerror('Error',
                  f'Error al desencriptar:\n{str(e)}\n\n'
                  f'Posiblemente el archivo no fue encriptado '
                  f'o se usó otra clave.')


def crear_clave():
    """Crea una nueva clave de encriptación"""
    try:
        if verificar_clave_existe():
            respuesta = askyesno(
                'Advertencia',
                '¡ATENCIÓN!\n\n'
                'Ya existe una clave.\n'
                'Si creas una nueva, NO podrás desencriptar\n'
                'archivos encriptados con la clave anterior.\n\n'
                '¿Estás seguro de continuar?'
            )
            if not respuesta:
                return

        generar_clave()
        showinfo('Clave creada',
                 'Se ha generado una nueva clave de encriptación exitosamente')

    except Exception as e:
        showerror('Error', f'Error al crear la clave:\n{str(e)}')


def exportar_clave():
    """Permite exportar la clave a una ubicación segura"""
    try:
        if not verificar_clave_existe():
            showerror('Error', 'No existe una clave para exportar')
            return

        destino = asksaveasfilename(
            title="Guardar copia de la clave",
            defaultextension=".key",
            filetypes=[('Archivo de clave', '*.key')]
        )

        if destino:
            shutil.copy(obtener_ruta_clave(), destino)
            showinfo('Éxito',
                     f'Clave exportada correctamente a:\n{destino}')

    except Exception as e:
        showerror('Error', f'Error al exportar la clave:\n{str(e)}')


def importar_clave():
    """Permite importar una clave desde otra ubicación"""
    try:
        origen = askopenfilename(
            title="Seleccionar archivo de clave",
            filetypes=[
                ('Archivo de clave', '*.key'),
                ('Todos los archivos', '*.*')
            ]
        )

        if origen:
            if verificar_clave_existe():
                if not askyesno('Confirmar',
                               '¿Reemplazar la clave actual?'):
                    return
            shutil.copy(origen, obtener_ruta_clave())
            showinfo('Éxito', 'Clave importada correctamente')

    except Exception as e:
        showerror('Error', f'Error al importar la clave:\n{str(e)}')


# ╔══════════════════════════════════════════════════════════════════╗
# ║                  VENTANAS DE AYUDA E INFORMACIÓN                 ║
# ╚══════════════════════════════════════════════════════════════════╝

def crear_ventana_texto(titulo, contenido, ancho=600, alto=400):
    """Crea una ventana con texto scrollable"""
    ventana = Toplevel()
    ventana.title(titulo)
    ventana.geometry(f"{ancho}x{alto}")
    ventana.resizable(True, True)

    frame = Frame(ventana)
    frame.pack(fill='both', expand=True, padx=10, pady=10)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side='right', fill='y')

    texto = Text(frame, wrap=WORD, yscrollcommand=scrollbar.set,
                 font=('Arial', 10), padx=10, pady=10)
    texto.pack(side='left', fill='both', expand=True)
    scrollbar.config(command=texto.yview)

    texto.insert(END, contenido)
    texto.config(state='disabled')

    btn_cerrar = Button(ventana, text="Cerrar",
                        command=ventana.destroy,
                        font=('Arial', 10, 'bold'))
    btn_cerrar.pack(pady=5)

    ventana.transient()
    ventana.grab_set()


def ayuda():
    """Muestra la ventana de instrucciones"""
    contenido = """
╔════════════════════════════════════════════════════╗
║          INSTRUCCIONES DE USO                      ║
╚════════════════════════════════════════════════════╝

CLAVE DE ENCRIPTACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Para encriptar o desencriptar archivos, necesitas una CLAVE de
encriptación. Si no existe, debes crearla primero usando el botón
"Crear nueva clave".

IMPORTANTE: La misma clave que usas para encriptar debe usarse
para desencriptar. Si pierdes la clave o creas una nueva, NO
podrás recuperar los archivos encriptados con la clave anterior.


CÓMO ENCRIPTAR UN ARCHIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Haz clic en el botón "Encriptar"
2. Selecciona el archivo que deseas proteger
3. Confirma la operación
4. ¡Listo! Tu archivo ahora está encriptado y protegido

Tip: Después de encriptar, el archivo original será reemplazado
por su versión encriptada. Asegúrate de tener copias de seguridad.


CÓMO DESENCRIPTAR UN ARCHIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Haz clic en el botón "Desencriptar"
2. Selecciona el archivo encriptado
3. Confirma la operación
4. El archivo volverá a su estado original

ADVERTENCIA: Solo puedes desencriptar archivos que fueron
encriptados con la clave actual. Si usas una clave diferente,
el proceso fallará.


GESTIÓN DE CLAVES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Crear nueva clave: Genera una nueva clave de encriptación
- Exportar clave: Guarda una copia de tu clave en lugar seguro
- Importar clave: Carga una clave previamente exportada

Recomendación: Exporta y guarda tu clave en un lugar seguro
(USB, nube, etc.) para no perderla.


RESOLUCIÓN DE PROBLEMAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- "Error al desencriptar": El archivo no fue encriptado o se
  está usando una clave diferente.

- "Archivo no encontrado": Verifica que el archivo existe y
  tienes permisos para acceder a él.

- "Clave no encontrada": Crea una nueva clave o importa una
  clave previamente exportada.
"""
    crear_ventana_texto("Instrucciones de Uso", contenido)


def notas_adicionales():
    """Muestra notas y advertencias adicionales"""
    contenido = """
╔════════════════════════════════════════════════════╗
║          NOTAS ADICIONALES                         ║
╚════════════════════════════════════════════════════╝

SOBRE LA SEGURIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Esta aplicación utiliza el algoritmo Fernet (criptografía simétrica)
que es parte de la biblioteca 'cryptography' de Python. Fernet
garantiza que los datos encriptados no pueden ser manipulados o
leídos sin la clave.

- Nivel de seguridad: Alto (AES 128 bits en modo CBC)
- Autenticación: Sí (HMAC)
- Protección contra manipulación: Sí


ADVERTENCIAS IMPORTANTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. RESPALDO DE CLAVE
   ¡MUY IMPORTANTE! Si pierdes el archivo 'clave.key', NO podrás
   recuperar tus archivos encriptados. Realiza copias de seguridad
   de tu clave.

2. NO MEZCLAR CLAVES
   Cada clave es única. Un archivo encriptado con la Clave A solo
   puede desencriptarse con la Clave A. Si creas una nueva clave
   (Clave B), los archivos de la Clave A quedarán inaccesibles.

3. ARCHIVOS ORIGINALES
   Cuando encriptas un archivo, el original es REEMPLAZADO por su
   versión encriptada. Si quieres conservar el original, haz una
   copia antes de encriptar.

4. ARCHIVOS DEL SISTEMA
   NO encriptes archivos críticos del sistema operativo o programas
   instalados. Solo usa esta herramienta para tus documentos
   personales.


MEJORES PRÁCTICAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Exporta tu clave inmediatamente después de crearla
- Guarda copias de la clave en múltiples ubicaciones seguras
- No compartas tu clave por correo o mensajes no seguros
- Haz pruebas con archivos no importantes primero
- Mantén backups de archivos importantes antes de encriptar


UBICACIÓN DE ARCHIVOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
La clave de encriptación (clave.key) se guarda en el mismo
directorio donde se ejecuta la aplicación.

Puedes encriptar/desencriptar archivos de cualquier ubicación
en tu computadora.


COMPATIBILIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Tipos de archivo: Cualquiera (documentos, imágenes, videos, etc.)
- Tamaño: Sin límite teórico (limitado por espacio en disco)
- Sistema operativo: Windows, Linux, macOS


RESPONSABILIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Esta herramienta es para uso personal y educativo. El autor no
se hace responsable por pérdida de datos debido a mal uso, pérdida
de claves, o cualquier otro problema derivado del uso de esta
aplicación.

Siempre mantén copias de seguridad de tus archivos importantes.
"""
    crear_ventana_texto("Notas Adicionales", contenido, 650, 500)


def acerca_de():
    """Muestra información sobre la aplicación"""
    contenido = """
╔════════════════════════════════════════════════════╗
║    ENCRIPTADOR DE ARCHIVOS v2.0                    ║
╚════════════════════════════════════════════════════╝

AUTOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Jcc (Julio César Calderaro)
Versión original: 2021
Versión actualizada: 2024


TECNOLOGÍAS UTILIZADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Python 3.x
- Tkinter (Interfaz gráfica)
- Cryptography (Encriptación Fernet)


LICENCIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Software de uso libre para fines personales y educativos.


CARACTERÍSTICAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Encriptación segura con Fernet (AES 128)
- Interfaz gráfica intuitiva
- Soporte para múltiples tipos de archivo
- Exportación e importación de claves
- Confirmaciones de seguridad


CONTACTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Para reportar problemas o sugerencias, contacta al autor.


AGRADECIMIENTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gracias por usar esta aplicación. Si te ha sido útil,
compártela con otros que puedan necesitarla.

¡Mantén tus archivos seguros!
"""
    crear_ventana_texto("Acerca de", contenido, 600, 450)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                   INTERFAZ GRÁFICA PRINCIPAL                     ║
# ╚══════════════════════════════════════════════════════════════════╝

class EncriptadorApp:
    """Clase principal de la aplicación"""

    # --- Dimensiones de la ventana ---
    ANCHO = 420
    ALTO = 430

    def __init__(self, master):
        self.master = master
        self.configurar_ventana()
        self.crear_menu()
        self.crear_interfaz()

    def configurar_ventana(self):
        """Configura la ventana principal"""
        self.master.title('Encriptador de Archivos v2.0')
        self.master.resizable(False, False)
        self.centrar_ventana(self.ANCHO, self.ALTO)

        # Configurar icono si existe
        try:
            if getattr(sys, 'frozen', False):
                base = os.path.dirname(sys.executable)
            else:
                base = os.path.dirname(os.path.abspath(__file__))
            icono = os.path.join(base, 'icono.ico')
            if os.path.exists(icono):
                self.master.iconbitmap(icono)
        except Exception:
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
        menu_archivo.add_command(label="Encriptar archivo",
                                 command=encriptar_archivos)
        menu_archivo.add_command(label="Desencriptar archivo",
                                 command=desencriptar_archivos)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir",
                                 command=self.master.quit)

        # Menú Herramientas
        menu_herramientas = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Herramientas",
                            menu=menu_herramientas)
        menu_herramientas.add_command(label="Crear nueva clave",
                                      command=crear_clave)
        menu_herramientas.add_command(label="Exportar clave",
                                      command=exportar_clave)
        menu_herramientas.add_command(label="Importar clave",
                                      command=importar_clave)

        # Menú Ayuda
        menu_ayuda = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Instrucciones",
                               command=ayuda)
        menu_ayuda.add_command(label="Notas adicionales",
                               command=notas_adicionales)
        menu_ayuda.add_separator()
        menu_ayuda.add_command(label="Acerca de",
                               command=acerca_de)

    def crear_interfaz(self):
        """Crea la interfaz gráfica"""

        # ── Barra de título ──
        frame_titulo = Frame(self.master, bg='#2c3e50', height=50)
        frame_titulo.pack(fill='x')
        frame_titulo.pack_propagate(False)

        Label(
            frame_titulo,
            text='Encriptador de Archivos',
            fg='white',
            bg='#2c3e50',
            font=('Arial', 16, 'bold')
        ).pack(expand=True)

        # ── Subtítulo ──
        Label(
            self.master,
            text='Protege tus archivos con encriptación segura',
            font=('Arial', 9),
            fg='#7f8c8d'
        ).pack(pady=(8, 0))

        # ── Opciones Principales ──
        frame_principal = LabelFrame(
            self.master,
            text=' Opciones Principales ',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=10
        )
        frame_principal.pack(padx=20, pady=(10, 8), fill='x')

        Button(
            frame_principal,
            text='Encriptar Archivo',
            font=('Arial', 11),
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            pady=8,
            command=encriptar_archivos
        ).pack(fill='x', pady=(0, 5))

        Button(
            frame_principal,
            text='Desencriptar Archivo',
            font=('Arial', 11),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            pady=8,
            command=desencriptar_archivos
        ).pack(fill='x', pady=(0, 2))

        # ── Gestión de Claves ──
        frame_claves = LabelFrame(
            self.master,
            text=' Gestión de Claves ',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=10
        )
        frame_claves.pack(padx=20, pady=(0, 8), fill='x')

        # Columnas uniformes
        frame_claves.columnconfigure(0, weight=1)
        frame_claves.columnconfigure(1, weight=1)
        frame_claves.columnconfigure(2, weight=1)

        Button(
            frame_claves,
            text='Nueva\nClave',
            font=('Arial', 9),
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            command=crear_clave
        ).grid(row=0, column=0, padx=4, pady=2, sticky='ew')

        Button(
            frame_claves,
            text='Exportar\nClave',
            font=('Arial', 9),
            bg='#f39c12',
            fg='white',
            activebackground='#d68910',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            command=exportar_clave
        ).grid(row=0, column=1, padx=4, pady=2, sticky='ew')

        Button(
            frame_claves,
            text='Importar\nClave',
            font=('Arial', 9),
            bg='#9b59b6',
            fg='white',
            activebackground='#8e44ad',
            activeforeground='white',
            cursor='hand2',
            relief='flat',
            command=importar_clave
        ).grid(row=0, column=2, padx=4, pady=2, sticky='ew')

        # ── Footer ──
        Label(
            self.master,
            text='© 2024 Jcc - Todos los derechos reservados',
            font=('Arial', 8),
            fg='#95a5a6'
        ).pack(side='bottom', pady=5)


# ╔══════════════════════════════════════════════════════════════════╗
# ║                        PUNTO DE ENTRADA                          ║
# ╚══════════════════════════════════════════════════════════════════╝

def main():
    """Función principal"""
    root = Tk()
    app = EncriptadorApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
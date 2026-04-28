# -*- coding: utf-8 -*-
"""
Ventanas de ayuda e información
@author: Jcc (Julio César Calderaro)
Actualizado: 2024
"""

from tkinter import Toplevel, Text, Scrollbar, Button, Frame
from tkinter import END, WORD


def crear_ventana_texto(titulo, contenido, ancho=600, alto=400):
    """Crea una ventana con texto scrollable"""
    ventana = Toplevel()
    ventana.title(titulo)
    ventana.geometry(f"{ancho}x{alto}")
    ventana.resizable(True, True)
    
    # Frame principal
    frame = Frame(ventana)
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side='right', fill='y')
    
    # Texto
    texto = Text(frame, wrap=WORD, yscrollcommand=scrollbar.set, 
                 font=('Arial', 10), padx=10, pady=10)
    texto.pack(side='left', fill='both', expand=True)
    scrollbar.config(command=texto.yview)
    
    # Insertar contenido
    texto.insert(END, contenido)
    texto.config(state='disabled')  # Solo lectura
    
    # Botón cerrar
    btn_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy, 
                        font=('Arial', 10, 'bold'))
    btn_cerrar.pack(pady=5)
    
    ventana.transient()
    ventana.grab_set()


def ayuda():
    """Muestra la ventana de instrucciones"""
    contenido = """
╔═════════════════════════════════════════════════════════╗
║               INSTRUCCIONES DE USO                      ║
╚═════════════════════════════════════════════════════════╝

📌 CLAVE DE ENCRIPTACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━
Para encriptar o desencriptar archivos, necesitas una CLAVE de 
encriptación. Si no existe, debes crearla primero usando el botón 
"Crear nueva clave".

⚠️ IMPORTANTE: La misma clave que usas para encriptar debe usarse 
para desencriptar. Si pierdes la clave o creas una nueva, NO 
podrás recuperar los archivos encriptados con la clave anterior.


📝 CÓMO ENCRIPTAR UN ARCHIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Haz clic en el botón "Encriptar"
2. Selecciona el archivo que deseas proteger
3. Confirma la operación
4. ¡Listo! Tu archivo ahora está encriptado y protegido

💡 Tip: Después de encriptar, el archivo original será reemplazado 
por su versión encriptada. Asegúrate de tener copias de seguridad.


🔓 CÓMO DESENCRIPTAR UN ARCHIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Haz clic en el botón "Desencriptar"
2. Selecciona el archivo encriptado
3. Confirma la operación
4. El archivo volverá a su estado original

⚠️ ADVERTENCIA: Solo puedes desencriptar archivos que fueron 
encriptados con la clave actual. Si usas una clave diferente, 
el proceso fallará.


🔑 GESTIÓN DE CLAVES
━━━━━━━━━━━━━━━━━━━━━
• Crear nueva clave: Genera una nueva clave de encriptación
• Exportar clave: Guarda una copia de tu clave en lugar seguro
• Importar clave: Carga una clave previamente exportada

💡 Recomendación: Exporta y guarda tu clave en un lugar seguro 
(USB, nube, etc.) para no perderla.


❓ RESOLUCIÓN DE PROBLEMAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
• "Error al desencriptar": El archivo no fue encriptado o se 
  está usando una clave diferente.
  
• "Archivo no encontrado": Verifica que el archivo existe y 
  tienes permisos para acceder a él.
  
• "Clave no encontrada": Crea una nueva clave o importa una 
  clave previamente exportada.
"""
    crear_ventana_texto("Instrucciones de Uso", contenido)


def notas_adicionales():
    """Muestra notas y advertencias adicionales"""
    contenido = """
╔════════════════════════════════════════════════════╗
║          NOTAS ADICIONALES                         ║
╚════════════════════════════════════════════════════╝

🔐 SOBRE LA SEGURIDAD
━━━━━━━━━━━━━━━━━━━━━━
Esta aplicación utiliza el algoritmo Fernet (criptografía simétrica) 
que es parte de la biblioteca 'cryptography' de Python. Fernet 
garantiza que los datos encriptados no pueden ser manipulados o 
leídos sin la clave.

✓ Nivel de seguridad: Alto (AES 128 bits en modo CBC)
✓ Autenticación: Sí (HMAC)
✓ Protección contra manipulación: Sí


⚠️ ADVERTENCIAS IMPORTANTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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


📋 MEJORES PRÁCTICAS
━━━━━━━━━━━━━━━━━━━━━
✓ Exporta tu clave inmediatamente después de crearla
✓ Guarda copias de la clave en múltiples ubicaciones seguras
✓ No compartas tu clave por correo o mensajes no seguros
✓ Haz pruebas con archivos no importantes primero
✓ Mantén backups de archivos importantes antes de encriptar


💾 UBICACIÓN DE ARCHIVOS
━━━━━━━━━━━━━━━━━━━━━━━━━
La clave de encriptación (clave.key) se guarda en el mismo 
directorio donde se ejecuta la aplicación.

Puedes encriptar/desencriptar archivos de cualquier ubicación 
en tu computadora.


🔄 COMPATIBILIDAD
━━━━━━━━━━━━━━━━━━
✓ Tipos de archivo: Cualquiera (documentos, imágenes, videos, etc.)
✓ Tamaño: Sin límite teórico (limitado por espacio en disco)
✓ Sistema operativo: Windows, Linux, macOS


⚖️ RESPONSABILIDAD
━━━━━━━━━━━━━━━━━━━
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
╔══════════════════════════════════════════════════════════════╗
║              ENCRIPTADOR DE ARCHIVOS v2.0                    ║
╚══════════════════════════════════════════════════════════════╝

👨‍💻 AUTOR
━━━━━━━━━
Jcc (Julio César Calderaro)
Versión original: 2021
Versión actualizada: 2024


🛠️ TECNOLOGÍAS UTILIZADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━
• Python 3.x
• Tkinter (Interfaz gráfica)
• Cryptography (Encriptación Fernet)


📜 LICENCIA
━━━━━━━━━━━━
Software de uso libre para fines personales y educativos.


🌟 CARACTERÍSTICAS
━━━━━━━━━━━━━━━━━━━
✓ Encriptación segura con Fernet (AES 128)
✓ Interfaz gráfica intuitiva
✓ Soporte para múltiples tipos de archivo
✓ Exportación e importación de claves
✓ Confirmaciones de seguridad


📧 CONTACTO
━━━━━━━━━━━━
Para reportar problemas o sugerencias, contacta al autor.


⚡ AGRADECIMIENTOS
━━━━━━━━━━━━━━━━━━━
Gracias por usar esta aplicación. Si te ha sido útil, 
compártela con otros que puedan necesitarla.

¡Mantén tus archivos seguros! 🔒
"""
    crear_ventana_texto("Acerca de", contenido, 600, 450)
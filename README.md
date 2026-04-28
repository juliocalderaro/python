# 🔒 Encriptador de Archivos v2.0

Aplicación de escritorio para encriptar y desencriptar archivos
de forma segura, desarrollada en Python con interfaz gráfica.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=flat)
![Cryptography](https://img.shields.io/badge/Crypto-Fernet%20AES128-red?style=flat)
![License](https://img.shields.io/badge/Licencia-Libre-brightgreen?style=flat)

---

## 📋 Descripción

**Encriptador de Archivos** es una herramienta simple e intuitiva
que permite proteger cualquier tipo de archivo mediante el algoritmo
**Fernet (AES 128 bits)**, parte de la biblioteca `cryptography`
de Python.

Ideal para proteger documentos personales, imágenes, hojas de
cálculo y cualquier otro archivo sensible.

---

## ✨ Características

- 🔐 **Encriptación segura** con Fernet (AES 128 bits en modo CBC)
- 🔓 **Desencriptación** con la misma clave generada
- 🔑 **Gestión de claves**: crear, exportar e importar
- 🖥️ **Interfaz gráfica** intuitiva desarrollada con Tkinter
- 📂 **Compatible** con cualquier tipo de archivo
- ✅ **Confirmaciones de seguridad** antes de cada operación
- 📖 **Ventanas de ayuda** integradas
- 💻 **Multiplataforma**: Windows, Linux, macOS

---

## 🛡️ Seguridad

| Característica        | Detalle                     |
|-----------------------|-----------------------------|
| Algoritmo             | Fernet (AES 128 bits CBC)   |
| Autenticación         | HMAC-SHA256                 |
| Protección            | Contra manipulación de datos|
| Tipo de criptografía  | Simétrica                   |

---

## 🚀 Instalación y Uso

### Opción 1: Ejecutable (recomendado)

1. Descarga `Encriptador.exe` desde [Releases](../../releases)
2. Ejecuta `Encriptador.exe`
3. ¡Listo! No requiere instalación

## 📖 Cómo usar
### Encriptar un archivo
Clic en "Encriptar Archivo"
Selecciona el archivo a proteger
Confirma la operación
El archivo queda protegido ✅

### Desencriptar un archivo
Clic en "Desencriptar Archivo"
Selecciona el archivo encriptado
Confirma la operación
El archivo vuelve a su estado original ✅

### Gestión de claves
Acción	Descripción
Nueva Clave	Genera una nueva clave de encriptación
Exportar	Guarda una copia de la clave en lugar seguro
Importar	Carga una clave previamente exportada

## ⚠️ Advertencias importantes
### ¡CRÍTICO! Si pierdes el archivo clave.key, NO podrás
recuperar tus archivos encriptados. Realiza siempre copias
de seguridad de tu clave.

La misma clave usada para encriptar debe usarse para desencriptar
Al encriptar, el archivo original es reemplazado por su versión encriptada
No encriptes archivos críticos del sistema operativo
Guarda copias de tu clave en múltiples ubicaciones seguras

## 🛠️ Tecnologías
Tecnología	Uso	Versión
Python	Lenguaje base	3.x
Tkinter	Interfaz gráfica	Incluida
cryptography	Encriptación Fernet	Latest
PyInstaller	Generación de ejecutable	Latest

## 📝 Historial de versiones
Versión	Año	Cambios
v1.0	2021	Versión original
v2.0	2024	Refactorización, GUI mejorada, archivo único

## 👨‍💻 Autor
Jcc (Julio César Calderaro)
Versión original: 2021
Versión actualizada: 2024

## 📄 Licencia
Software de uso libre para fines personales y educativos.

El autor no se hace responsable por pérdida de datos debido
a mal uso, pérdida de claves, o cualquier problema derivado
del uso de esta aplicación.

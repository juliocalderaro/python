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

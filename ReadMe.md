# Ejercicios de Programación Orientada a Objetos (POO) en Python

Este repositorio contiene una colección de ejercicios desarrollados en Python para practicar los principales conceptos de **Programación Orientada a Objetos (POO)**.

Los ejercicios abarcan la creación de clases, objetos, encapsulamiento, herencia, composición, manejo de estructuras de datos y simulación de sistemas simples.

## Estructura del proyecto

Poo/
│
├── Ad_correo/              # Sistema de administración de correo
│   ├── mail.py
│   └── main.py
│
├── paciente_h/             # Gestión de pacientes mediante nodos
│   ├── Node.py
│   └── main.py
│
├── Playlist/               # Implementación de una playlist usando nodos
│   ├── node.py
│   └── main.py
│
├── sistemPay/              # Sistema de pagos con diferentes métodos
│   ├── pay.py
│   ├── card.py
│   ├── cash.py
│   ├── paypal.py
│   └── main.py
│
├── animal.py               # Ejercicio de clases relacionadas con animales
├── bank_account.py         # Simulación de una cuenta bancaria
├── Batalla_N.py            # Lógica del juego Batalla Naval
├── Juego_Batalla.py        # Ejecución del juego
├── concesionaria.py        # Sistema de concesionaria de vehículos
├── contactl.py             # Gestión de contactos
├── mylist.py               # Implementación de listas personalizadas
├── product.py              # Modelo de productos
├── taskmap.py              # Gestión de tareas
├── user.py                 # Modelo de usuarios
└── main.py                 # Archivo principal de ejecución

## Conceptos practicados

Los ejercicios implementan diferentes fundamentos de POO:

### Clases y objetos
- Creación de clases.
- Instanciación de objetos.
- Uso de atributos y métodos.

### Encapsulamiento
- Control del acceso a datos internos.
- Uso de métodos para modificar el estado de los objetos.

### Herencia
- Creación de clases derivadas.
- Reutilización y extensión de código.

### Polimorfismo
- Diferentes comportamientos mediante interfaces comunes.
- Implementación de métodos especializados.

### Composición
- Construcción de objetos complejos a partir de otros objetos.

### Estructuras de datos
- Implementación de listas enlazadas mediante nodos.
- Organización de colecciones personalizadas.

## Requisitos

- Python 3.12 o superior.

Verificar instalación:

```bash
python3 --version
Ejecución
Cada ejercicio puede ejecutarse desde su carpeta correspondiente:
Ejemplo:
python3 main.py
o directamente:
python3 archivo.py
Limpieza de archivos generados
Los archivos .pyc y carpetas __pycache__ son archivos generados automáticamente por Python y no son necesarios.
Para eliminarlos:
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
Objetivo
El objetivo de estos ejercicios es desarrollar una base sólida en Programación Orientada a Objetos utilizando Python, aplicando buenas prácticas de diseño y separación de responsabilidades en pequeños sistemas funcionales.
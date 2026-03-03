# Control Escolar CLI - ITM

Proyecto en Python para administrar una base de datos MySQL de control escolar.

## 📁 Estructura

```
control_escolar_cli/
  main.py
  conexiones.py
  db.py
  menu.py
  requirements.txt
  ops/
    carreras.py
    maestros.py
    alumnos.py
    cursos.py
```

---

## ⚙️ Requisitos

- Python 3.9 o superior
- MySQL Server
- Base de datos `control_escolar_itm` previamente creada

---

## 🛠 Instalación

1️⃣ Crear entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```

Activar entorno:

- Windows:
```bash
venv\Scripts\activate
```

- Mac/Linux:
```bash
source venv/bin/activate
```

2️⃣ Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🗄 Configuración

Editar el archivo:

```
conexiones.py
```

Configurar host, usuario y contraseña de MySQL.

---

## ▶️ Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

---

## 📌 Funcionalidades

- Agregar carreras
- Modificar maestros
- Borrar alumnos
- Consultar cursos (con filtro por carrera)

---

## 👨‍🏫 Proyecto Académico

Pensado para prácticas de:
- Programación en Python
- Bases de datos MySQL
- Arquitectura modular de software

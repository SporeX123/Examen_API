# Django API Project

Plantilla base para el desarrollo de APIs robustas utilizando Django y Django REST Framework (DRF).

---

## 🚀 Características Principales

* **Django REST Framework (DRF):** Framework potente y flexible para la construcción de Web APIs.
* **Autenticación y Permisos:** Sistema integrado de autenticación por Token / JWT y gestión de permisos granulares.

---

## 📋 Requisitos Previos

* Python 3.10 o superior
* pip (gestor de paquetes de Python)
* Virtualenv (recomendado)

---

## 🛠️ Instalación y Configuración

Sigue estos pasos para levantar el entorno de desarrollo local:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/rodrigomedrano-jpg/apis-a.git

2.  Crear y activar un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:

```bash
python manage.py migrate
```

5. Crear un superusuario, si lo necesitas:

```bash
python manage.py createsuperuser
```

## Ejecutar el proyecto

```bash
python manage.py runserver
```

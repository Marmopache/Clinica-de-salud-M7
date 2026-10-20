[Read in English](README-en.md)

# Sistema de Gestión de Clínica

Aplicación web desarrollada con **Django** y **PostgreSQL** para gestionar pacientes, médicos y horas médicas de una clínica en un solo sistema, reemplazando la agenda manual y los registros en papel.

> Proyecto en equipo desarrollado junto a Felipe Droguett y Rodrigo Villaroel en el programa Full Stack Python de Kibernum / SENCE.

## Funcionalidades

- **Autenticación:** inicio y cierre de sesión, con un panel de control como página de inicio tras ingresar
- **Gestión de pacientes:** crear, ver, editar y eliminar pacientes (CRUD)
- **Gestión de médicos:** crear, ver, editar y eliminar médicos (CRUD), incluyendo especialidad
- **Agenda de horas médicas:** crear horas seleccionando pacientes y médicos ya registrados, con fecha, hora y motivo
- **Filtros:** consultas y filtros con el ORM de Django
- **Eliminación segura:** página de confirmación antes de borrar cualquier registro
- **Avisos al usuario:** notificaciones emergentes (SweetAlert2) que confirman acciones como registrar una hora
- **Tests automatizados:** suite de pruebas ejecutable con `python manage.py test`
- **Configuración segura:** claves y credenciales de la base de datos cargadas desde variables de entorno (`python-decouple`) y contraseñas con hash bcrypt
- **Localización:** interfaz en español, zona horaria `America/Santiago`

## Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Python, Django 6 |
| Base de datos | PostgreSQL (`psycopg`) |
| Frontend | Templates de Django, HTML, CSS, Bootstrap 5, Font Awesome, SweetAlert2 |
| Configuración | python-decouple (`.env`) |
| Seguridad | Hash de contraseñas con bcrypt |

## Capturas de pantalla

| Inicio de sesión | Panel de control |
|---|---|
| ![Inicio de sesión](docs/login.png) | ![Panel de control](docs/panel.png) |

| Lista de pacientes | Lista de médicos |
|---|---|
| ![Lista de pacientes](docs/patients-list.png) | ![Lista de médicos](docs/doctors-list.png) |

| Lista de horas médicas | Formulario de hora médica |
|---|---|
| ![Lista de horas médicas](docs/appointments-list.png) | ![Formulario de hora médica](docs/appointments-form.png) |

*Formulario de hora médica: los pacientes y médicos ya registrados se seleccionan desde listas desplegables para crear la hora.*

| Página de confirmación al eliminar |
|---|
| ![Confirmación de eliminación](docs/delete-confirmation.png) |

## Estructura del proyecto

```
Clinica-de-salud-M7/
├── clinica_M7/        # Configuración del proyecto y URLs
├── gestion/           # App principal: modelos, vistas, formularios, tests
├── templates/         # Plantillas HTML
├── static/            # CSS, JS e imágenes
├── docs/              # Capturas del README
├── manage.py
├── requirements.txt
└── .env.example       # Plantilla de variables de entorno
```

## Requisitos

- Python 3.12 o superior
- PostgreSQL

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Marmopache/Clinica-de-salud-M7.git
   cd Clinica-de-salud-M7
   ```

2. **Crear y activar un entorno virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Crear la base de datos en PostgreSQL**, luego copiar `.env.example` como `.env` y completar los valores:
   ```
   SECRET_KEY=tu-clave-secreta
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_NAME=clinica
   DB_USER=postgres
   DB_PASSWORD=tu_contraseña
   DB_HOST=localhost
   DB_PORT=5432
   ```
   Para generar una clave secreta:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Crear un usuario administrador**
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```
   Luego abrir http://127.0.0.1:8000/

## Ejecutar los tests

```bash
python manage.py test
```

## Qué practiqué

- Diseño de modelos relacionales y sus relaciones en PostgreSQL
- Vistas y formularios CRUD con Django
- Consultas y filtros de datos con el ORM de Django
- Escritura de tests automatizados
- Manejo de secretos con variables de entorno y hash seguro de contraseñas
- Trabajo en equipo con Git y GitHub

## Autores

Proyecto en equipo de **Gabriela Alvarado Rosales**, Felipe Droguett O. y Rodrigo Villaroel U.
Desarrollado en el programa Full Stack Python de Kibernum / SENCE.

GitHub: [@Marmopache](https://github.com/Marmopache)

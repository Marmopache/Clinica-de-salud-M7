# ClinicaVitalCare

## Descripción

Aplicación web desarrollada con Django para la gestión de pacientes, médicos y horas médicas.

## Tecnologías

* Python
* Django
* PostgreSQL
* Bootstrap

## Funcionalidades

* CRUD de Pacientes
* CRUD de Médicos
* Asignación de Horas Médicas
* Filtros con ORM
* Tests automatizados

## Instalación

1. Clonar repositorio
2. Crear entorno virtual
3. Instalar dependencias:
   pip install -r requirements.txt
4. Configurar PostgreSQL en settings.py
5. Ejecutar migraciones:
   python manage.py migrate
6. Ejecutar servidor:
   python manage.py runserver

## Tests

python manage.py test

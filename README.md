SuperUser
# Usuario: admin
# Contraseña: admin
---------------------------------------------------
Evaluación N°1 - Taller Mecánico
I. Descripción del Proyecto
Aplicación web desarrollada en Django para la gestión de un taller mecánico. Permite administrar mecánicos, vehículos y procedimientos de mantenimiento.

II. Funcionalidades Implementadas
CRUD Completo para las entidades:

Mecánico (nombre, contacto, especialidad)

Vehículo (patente, modelo, año, dueño)

Procedimiento (nombre, descripción, mecánico, vehículo)

Panel de Administración Django configurado con filtros, búsquedas y visualización optimizada

Interfaz Web para gestión de datos

III. Tecnologías Utilizadas
Django 4.2+

Python 3.8+

SQLite

HTML5 + CSS básico

Bootstrap 5 (opcional)

IV. Instrucciones de Instalación y Ejecución
Prerrequisitos
Python 3.8 o superior instalado

pip (gestor de paquetes de Python)

Pasos para ejecutar el proyecto:
Clonar o descomprimir el proyecto

bash
cd ruta/del/proyecto
Crear y activar entorno virtual (recomendado)

bash
# En Windows
python -m venv venv
.\venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instalar dependencias

bash
pip install -r requirements.txt
Aplicar migraciones

bash
python manage.py migrate
Crear superusuario (si es necesario)

bash
python manage.py createsuperuser
# Usuario: admin
# Contraseña: admin
Ejecutar el servidor de desarrollo

bash
python manage.py runserver
Acceder a la aplicación

Sitio principal: http://127.0.0.1:8000/

Panel de administración: http://127.0.0.1:8000/admin/

Credenciales admin: usuario: admin, contraseña: admin

V. Estructura del Proyecto
text
taller_mecanico/
├── taller/              # Aplicación principal
│   ├── models.py       # Modelos de datos
│   ├── admin.py        # Configuración del admin
│   ├── views.py        # Vistas de la aplicación
│   ├── urls.py         # URLs de la aplicación
│   └── templates/      # Plantillas HTML
├── manage.py
└── requirements.txt    # Dependencias del proyecto
VI. Datos de Prueba
El sistema incluye datos de ejemplo para testing:

3 mecánicos con diferentes especialidades

5 vehículos de distintos modelos y años

8 procedimientos de mantenimiento asociados

VII. Características del Panel de Administración
Mecánicos: Búsqueda por nombre, filtro por especialidad

Vehículos: Búsqueda por patente o dueño, filtro por año

Procedimientos: Búsqueda por nombre, filtro por mecánico y vehículo

VIII. Consideraciones Técnicas
Base de datos SQLite para desarrollo

Diseño responsive básico

Validaciones de formularios integradas

Patentes de vehículos con restricción de unicidad

IX. Desarrollador
Nombre: [Tu Nombre]

Asignatura: Desarrollo de Aplicaciones Web

Fecha de entrega: 26 de agosto de 2024

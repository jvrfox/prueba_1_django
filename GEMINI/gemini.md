
# Resumen del Proyecto Django

Este es un proyecto de Django llamado `backend`. A continuación se resume el propósito de cada archivo y directorio importante.

## Archivos y Directorios Principales

- **`manage.py`**: Es un script de línea de comandos que permite interactuar con el proyecto Django. Se utiliza para tareas administrativas como ejecutar el servidor de desarrollo, crear migraciones de base de datos y más.

- **`db.sqlite3`**: Es el archivo de la base de datos. Django está configurado para usar SQLite, una base de datos ligera basada en archivos, ideal para desarrollo y pruebas.

- **`EVA-1 .pdf`**: Un archivo PDF, probablemente con especificaciones o requerimientos para el proyecto.

- **`venv/`**: Directorio que contiene el entorno virtual de Python. Esto aísla las dependencias del proyecto (como Django) de otros proyectos en el sistema.

## Proyecto `backend`

Este es el directorio principal del proyecto Django.

- **`backend/settings.py`**: Contiene toda la configuración del proyecto, como la configuración de la base de datos, las aplicaciones instaladas (`INSTALLED_APPS`), las plantillas, la zona horaria y mucho más.

- **`backend/urls.py`**: Define las rutas URL principales del proyecto. Aquí es donde se mapean las URLs a las vistas o se incluyen los archivos de URLs de las aplicaciones. Actualmente, solo define la ruta para el panel de administración (`/admin/`).

- **`backend/wsgi.py`** y **`backend/asgi.py`**: Son archivos de configuración para desplegar el proyecto en servidores web compatibles con los estándares WSGI (para servidores síncronos) y ASGI (para servidores asíncronos).

## Aplicaciones Django

El proyecto tiene tres aplicaciones: `mecanico`, `procedimiento` y `vehiculo`. La estructura de cada una es la misma:

- **`mecanico/`**, **`procedimiento/`**, **`vehiculo/`**: Son "aplicaciones" de Django. En Django, un proyecto se compone de una o más aplicaciones, cada una de las cuales se encarga de una funcionalidad específica.

### Archivos dentro de cada aplicación

- **`__init__.py`**: Un archivo vacío que le indica a Python que este directorio debe ser considerado un paquete de Python.

- **`admin.py`**: En este archivo se registran los modelos de la aplicación para que aparezcan y se puedan gestionar a través del panel de administración de Django. Actualmente están vacíos.

- **`apps.py`**: Contiene la configuración específica de la aplicación.

- **`models.py`**: Aquí es donde se definen los modelos de datos de la aplicación utilizando el ORM (Mapeo Objeto-Relacional) de Django. Cada modelo corresponde a una tabla en la base de datos. Actualmente están vacíos.

- **`tests.py`**: Para escribir pruebas unitarias y de integración para la aplicación.

- **`views.py`**: Contiene la lógica que maneja las solicitudes web y devuelve las respuestas. Una vista es una función o clase que toma una solicitud y devuelve una respuesta (como una página HTML o una redirección). Actualmente están vacíos.

- **`migrations/`**: Este directorio almacena los archivos de migración de la base de datos. Las migraciones son la forma en que Django maneja los cambios en el esquema de la base de datos (por ejemplo, cuando se agregan, eliminan o modifican modelos).

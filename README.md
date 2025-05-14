# Task Management API

API REST para gestión de tareas implementada con Django y arquitectura hexagonal.

## Requisitos

- Python 3.8+
- PostgreSQL
- pip

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
Crear un archivo `.env` en la raíz del proyecto con:
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

5. Aplicar migraciones:
```bash
python manage.py migrate
```

6. Iniciar el servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

El proyecto sigue la arquitectura hexagonal (puertos y adaptadores):

```
task_management/
├── domain/           # Capa de dominio
│   ├── entities/     # Entidades del dominio
│   └── ports/        # Puertos (interfaces)
├── application/      # Capa de aplicación
│   └── use_cases/    # Casos de uso
├── infrastructure/   # Capa de infraestructura
│   ├── adapters/     # Adaptadores
│   └── repositories/ # Implementaciones de repositorios
└── interfaces/       # Capa de interfaces
    └── api/          # Adaptadores HTTP
```

## Endpoints

- POST /tasks - Crear una nueva tarea
- GET /tasks - Listar todas las tareas
- PUT /tasks/{id} - Actualizar una tarea
- DELETE /tasks/{id} - Eliminar una tarea

## Documentación API

La documentación de la API está disponible en:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/ 
# Technical Test API - Sistema de Gestión de Tareas

API REST desarrollada en Python con FastAPI y PostgreSQL para la gestión de tareas (TODO) como parte de una prueba técnica backend. La aplicación incluye autenticación JWT, operaciones CRUD completas y está containerizada con Docker.

## Características Principales

### Funcionalidades Básicas
- **Autenticación JWT** - Registro y login seguro de usuarios
- **Operaciones CRUD de Tareas** - Crear, leer, actualizar y eliminar tareas
- **Base de Datos PostgreSQL** - Persistencia robusta de datos
- **Validación de Datos** - Con Pydantic y SQLModel
- **Seguridad** - Contraseñas encriptadas con hashing seguro y verificación de propiedad

### Características Avanzadas
- **Dockerizado** - Despliegue simplificado con Docker Compose
- **Tests Automatizados** - Suite de pruebas con pytest
- **Logging** - Sistema de registro de eventos y errores
- **Documentación Automática** - Swagger/OpenAPI integrado

## Tecnologías Utilizadas

- **Framework**: FastAPI 0.104.1
- **Base de Datos**: PostgreSQL 13
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Autenticación**: JWT con Python-JOSE
- **Contenedores**: Docker + Docker Compose
- **Testing**: pytest + pytest-asyncio
- **Variables de Entorno**: python-dotenv

## Instalación y Despliegue

### Prerrequisitos
- Docker y Docker Compose instalados
- Python 3.11+ (para desarrollo local)

### Despliegue con Docker (Recomendado)

1. **Clonar el repositorio**:
```bash
git clone <url-del-repositorio>
cd technical-test-app
```

2. **Configurar variables de entorno**:
cp .env.example .env
Editar `.env` para ajustar configuraciones si es necesario.

3. **Construir y levantar los contenedores**:
docker compose up --build

### Instalación Local

1. **Crear y activar un entorno virtual**:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

2. **Instalar dependencias**:
pip install -r requirements.txt

3. **Configurar base de datos**:
Asegurarse de tener PostgreSQL corriendo y crear la base de datos especificada en la variable POSTGRES_DB del archivo .env

4. **Ejecutar la aplicación**:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## Configuración

### Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
```bash
# Database
POSTGRES_DB=technicaltestapp
POSTGRES_USER=techuser
POSTGRES_PASSWORD=techpass123
DATABASE_URL=postgresql://techuser:techpass123@localhost:5433/technicaltestapp

# JWT
SECRET_KEY=tu_clave_super_secreta_unica_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# App
ENVIRONMENT=development
```

## Puertos
- API: http://localhost:8000
- PostgreSQL: localhost:5433 (ajustable en .env se usa 5433 en lugar del 5432 por defecto para evitar conflictos)
- Documentación API: http://localhost:8000/docs

## Uso de la API
- **Registro**: POST /auth/register
- **Login**: POST /auth/login
- **Crear Tarea**: POST /tasks/
- **Listar Tareas**: GET /tasks/
- **Actualizar Tarea**: PUT /tasks/{task_id}
- **Eliminar Tarea**: DELETE /tasks/{task_id}
- **Ejecutar Tests**: ENVIRONMENT=test pytest -v

## Estructura del Proyecto
```bash
technical-test-app/
├── app/                    # Código de la aplicación
│   ├── __init__.py
│   ├── main.py            # Punto de entrada de FastAPI
│   ├── models.py          # Modelos de base de datos
│   ├── schemas.py         # Esquemas Pydantic
│   ├── database.py        # Configuración de base de datos
│   ├── auth.py            # Autenticación y JWT
│   ├── dependencies.py    # Dependencias de FastAPI
│   └── routers/           # Routers de la API
│       ├── __init__.py
│       ├── auth.py        # Endpoints de autenticación
│       └── tasks.py       # Endpoints de tareas
├── tests/                 # Tests automatizados
│   ├── __init__.py
│   ├── conftest.py        # Configuración de pytest
│   ├── test_auth.py       # Tests de autenticación
│   └── test_tasks.py      # Tests de tareas
├── requirements.txt       # Dependencias de Python
├── Dockerfile            # Configuración de Docker
├── docker-compose.yml    # Orquestación de contenedores
├── .env.example          # Variables de entorno de ejemplo
└── README.md             # Este archivo
```

## Solución de Problemas Comunes
**Error de conexión a la base de datos**
- Verificar que PostgreSQL esté ejecutándose
- Comprobar las variables de entorno en .env

**Error de puertos ocupados**
- Cambiar los puertos en docker-compose.yml

**Error de dependencias**
- Ejecutar docker compose build --no-cache

**Error en tests**
- Asegurarse de ejecutar los tests con ENVIRONMENT=test pytest -v

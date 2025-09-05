from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routers import auth, tasks

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Crear tablas al iniciar
    create_db_and_tables()
    yield

app = FastAPI(
    title="Todo API",
    description="API para gestión de tareas - Prueba Técnica",
    version="1.0.0",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la Todo API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
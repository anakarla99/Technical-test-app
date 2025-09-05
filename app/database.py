from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv


ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

if ENVIRONMENT == "test":
    # Base de datos en memoria solo para tests
    DATABASE_URL = "sqlite:///:memory:"
else:
    DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
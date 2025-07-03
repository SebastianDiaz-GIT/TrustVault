from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import os
from dotenv import load_dotenv
from app.models.passEntry import Base

# Cargar variables desde el archivo .env
load_dotenv()

# 📌 Configurar la URL de conexión a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:admin@localhost:5432/password_manager")

# Crear el motor de base de datos
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear el manejador de sesiones
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


# Función para obtener una sesión de base de datos
async def get_db():
    async with SessionLocal() as session:
        yield session

# Función para inicializar la base de datos (crear tablas si no existen)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

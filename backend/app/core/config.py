import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class Settings:
    # Configuración de la base de datos
    DATABASE_URL: str = os.getenv("DATABASE_URL")


# Instancia global de configuración
settings = Settings()

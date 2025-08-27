# backend/app/db/engine.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define la URL de la base de datos para MySQL
# Asegúrate de reemplazar los valores con los de tu propia base de datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/mi_proyecto"


# Crea la instancia del motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
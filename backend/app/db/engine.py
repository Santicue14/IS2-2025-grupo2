
from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///mi_base.db"

engine = create_engine(
    DATABASE_URL,
    echo=True 
    future=True
)

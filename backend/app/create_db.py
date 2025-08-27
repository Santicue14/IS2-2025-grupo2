from app.db.base import Base 
from app.db.engine import engine

Base.metadata.create_all(bind=engine)
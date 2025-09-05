from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class UsuarioORM(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password=Column(String)
    is_active=Column(Boolean)
    
    # Relaciones
    roles = relationship("UsuarioRolORM", back_populates="usuario")
    movimientos=relationship("MovimientoORM",back_populates="usuario")
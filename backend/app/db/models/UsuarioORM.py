from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class UsuarioORM(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    is_active=Column(Boolean)
    hashed_password=Column(String)
    
    # Relaciones
    rol = relationship("RolORM", back_populates="usuario")
    movimientos=relationship("MovimientoORM",back_populates="usuario")
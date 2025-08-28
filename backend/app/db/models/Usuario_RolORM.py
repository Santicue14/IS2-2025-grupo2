from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class UsuarioRolORM(Base):
    __tablename__ = "usuario_rol"

    usuario_id = Column(Integer, ForeignKey("usuario.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("rol.id"), primary_key=True)

    # Relaciones
    usuario = relationship("UsuarioORM", back_populates="roles")
    rol = relationship("RolORM", back_populates="usuarios_roles")
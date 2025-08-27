from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class UsuarioORM(Base):
    __tablename__="usuarios"

    id = Column(Integer,primary_key=True, index=True)
    nombre_usuario = Column(String(255), unique=True, index=True)
    rol_id = Column(Integer,ForeignKey("roles.id"))

    rol = relationship("RolORM")
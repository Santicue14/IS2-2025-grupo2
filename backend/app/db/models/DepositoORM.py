from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class DepositoORM(Base):
    __tablename__ = "deposito"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    ubicacion = Column(String, unique=True, nullable=False)
    # Relación con movimientos
    movimientos = relationship("MovimientoORM", back_populates="deposito")

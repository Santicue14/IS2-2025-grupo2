from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class DepositoORM(Base):
    __tablename__ = "deposito"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    ubicacion = Column(String, unique=True, nullable=False)
    
    # Relaciones con movimientos 
    movimientos_origen = relationship("MovimientoORM", foreign_keys="[MovimientoORM.deposito_origen_id]", back_populates="deposito_origen")
    movimientos_destino = relationship("MovimientoORM", foreign_keys="[MovimientoORM.deposito_destino_id]", back_populates="deposito_destino")

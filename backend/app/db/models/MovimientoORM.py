from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class MovimientoORM(Base):
    __tablename__ = "movimiento"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"), nullable=False)
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id"), nullable=False)
    usuario_id=Column(Integer,ForeignKey("usuario_id"),nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    tipo=Column(Integer)

    # Relaciones
    producto = relationship("ProductoORM", back_populates="movimiento")
    deposito = relationship("DepositoORM", back_populates="movimiento")
    usuario = relationship("UsuarioORM",back_populates="movimiento")
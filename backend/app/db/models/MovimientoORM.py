from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class MovimientoORM(Base):
    __tablename__ = "movimiento"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=False)
    deposito_origen_id = Column(Integer, ForeignKey("deposito.id"), nullable=False)
    deposito_destino_id = Column(Integer, ForeignKey("deposito.id"), nullable=False)
    usuario_id=Column(Integer,ForeignKey("usuario.id"),nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    tipo=Column(Integer)

    # Relaciones
    producto = relationship("ProductoORM", back_populates="movimientos")
    deposito_origen = relationship("DepositoORM", foreign_keys=[deposito_origen_id], back_populates="movimientos_origen")
    deposito_destino = relationship("DepositoORM", foreign_keys=[deposito_destino_id], back_populates="movimientos_destino")
    usuario = relationship("UsuarioORM", back_populates="movimientos")
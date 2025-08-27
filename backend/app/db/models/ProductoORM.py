from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class ProductoORM(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=True)
    stock=Column(Integer)
    stock_minimo=Column(Integer)


    # Relación con movimientos
    movimientos = relationship("MovimientoORM", back_populates="producto")

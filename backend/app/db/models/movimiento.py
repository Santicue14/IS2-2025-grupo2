from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base
class MovimientoORM(Base):
    __tablename__ = "movimientos"

    id = Column(Integer,primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    origen_deposito_id = Column(Integer, ForeignKey("depositos.id"))
    # Corrige esta línea para que apunte a la tabla 'depositos'
    destino_deposito_id = Column(Integer, ForeignKey("depositos.id")) 
    cantidad = Column(Integer)
# ... (resto del código)
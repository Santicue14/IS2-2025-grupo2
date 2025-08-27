from sqlalchemy import Column, Integer, String
from ..base import Base

class DepositoORM(Base):
    __tablename__= "depositos"

    id = Column(Integer,primary_key=True, index=True)
    nombre = Column(String(255), index=True)
    ubicacion = Column(String(255))
    
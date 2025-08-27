from sqlalchemy import Column, Integer, String
from ..base import Base

class RolORM(Base):
    __tablename__="roles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), unique=True, index=True)
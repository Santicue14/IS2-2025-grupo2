from pydantic import BaseModel

class ProductoResponse(BaseModel):
    id: int
    nombre: str
    sku: str
    descripcion: str
    stock: int
    stock_minimo: int
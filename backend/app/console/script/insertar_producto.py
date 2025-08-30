from app.db.models.ProductoORM import ProductoORM
from app.db.session import SessionLocal

db = SessionLocal()

nuevo_producto= ProductoORM(nombre="Producto de Prueba", sku="1234567890", stock=50, stock_minimo=10, descripcion="Producto de prueba")

db.add(nuevo_producto)
db.commit()

db.close()

print("Producto insertado correctamente")


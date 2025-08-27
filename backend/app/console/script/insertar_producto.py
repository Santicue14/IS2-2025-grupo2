from app.db.models.producto import ProductoORM
from app.db.session import SessionLocal

db = SessionLocal()

nuevo_producto= ProductoORM(nombre="Producto de Prueba", precio=100.0, stock=50)

db.add(nuevo_producto)
db.commit()

db.close()

print("Producto insertado correctamente")

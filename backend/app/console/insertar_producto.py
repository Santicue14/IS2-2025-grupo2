from app.db.engine import SessionLocal
from app.db.models.producto import ProductoORM

def insertar_producto():
    db = SessionLocal()
    try:
        # Crea una nueva instancia del modelo
        nuevo_producto = ProductoORM(
            nombre="Producto de Prueba",
            precio=100.0,
            stock=50
        )
        # Agrega el objeto a la sesión
        db.add(nuevo_producto)
        # Confirma la transacción
        db.commit()
        print("¡Producto agregado con éxito!")
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    insertar_producto()
from app.domain.models.Producto import Producto
from app.db.models.ProductoORM import ProductoORM
from app.db.session import SessionLocal
from app.domain.mappers.ProductoMapper import producto_orm_a_producto, producto_a_producto_orm

from app.domain.models.Tipo import TipoMovimiento
db = SessionLocal()

def insertar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    sku = input("Ingrese el SKU del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    stock = input("Ingrese el stock del producto: ")
    stock_minimo = input("Ingrese el stock mínimo del producto: ")
    producto = Producto(nombre, sku, descripcion, stock, stock_minimo)
    producto = producto_a_producto_orm(producto)
    db.add(producto)
    db.commit()
    print("Producto insertado correctamente")

def ver_productos():
    try:
        productos = db.query(ProductoORM).all()
        productos = [producto_orm_a_producto(producto) for producto in productos]
        for producto in productos:
            print("Hola")
            print(producto)
    except Exception as e:
        print(f"Error al obtener los productos: {e}")

def listar_movimientos():
    print(TipoMovimiento.SALIDA.value)
    
def menu_producto():
    while True:
        print("1. Insertar producto")
        print("2. Ver productos")
        print("3. Listar movimientos")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                insertar_producto()
            case "2":
                ver_productos()
            case "3":
                listar_movimientos()
            case "5":
                break


menu_producto()

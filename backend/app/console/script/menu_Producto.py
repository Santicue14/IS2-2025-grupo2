from app.db.models.ProductoORM import ProductoORM
from app.db.session import SessionLocal
from app.domain.mappers.ProductoMapper import producto_orm_a_producto, producto_a_producto_orm
from app.domain.mappers.UsuarioMapper import usuario_a_usuario_orm
from app.security.jwt_handler import hashear_password
from app.domain.models.Tipo import TipoMovimiento

from app.schemas.producto import ProductoCreate, ProductoResponse
from app.schemas.usuario import UsuarioCreate
from pydantic import ValidationError

db = SessionLocal()

def insertar_producto():
    try:
        nombre = input("Ingrese el nombre del producto: ")
        sku = input("Ingrese el SKU del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        stock = input("Ingrese el stock del producto: ")
        stock_minimo = input("Ingrese el stock mínimo del producto: ")
        
        # Crear el schema ProductoCreate directamente con los datos de entrada
        productoCreate = ProductoCreate(
            nombre=nombre,
            sku=sku,
            descripcion=descripcion,
            stock=stock,
            stock_minimo=stock_minimo
        )
        
        #Mapeo de producto create a producto orm
        productoORM = producto_a_producto_orm(productoCreate)
        #Insertar producto en la base de datos
        db.add(productoORM)
        db.commit()
        print("Producto insertado correctamente")
    except ValidationError as ve:
        errores = [] #Declaramos la lista antes del bucle
        for error in ve.errors():
            # Extraer solo el mensaje personalizado del error
            if 'ctx' in error and 'error' in error['ctx']:
                message = str(error['ctx']['error'])
            else:
                # Para otros tipos de errores, usar el mensaje directo
                message = error['msg']
            #Guardamos el mensaje del error en la lista
            errores.append(message)
        
        print("Errores de validación:")
        for error in errores:
            print(f"- {error}")
        #Fakear API
        print({"success": False, "errors": errores})
        return {"success": False, "errors": errores}
    except Exception as e:
        #Manejar cualquier error no contemplado y fakear API
        print({"success": False, "errors": [e]})
        return {"success": False, "errors": [e]}
def ver_productos():
    try:
        productos_orm = db.query(ProductoORM).all()
        if len(productos_orm) == 0:
            print("No hay productos")
            return {"success": False, "errors": ["No hay productos"]}
        
        for producto_orm in productos_orm:

            # Crear ProductoResponse directamente desde el ORM
            producto_response = ProductoResponse(
                id=producto_orm.id,
                nombre=producto_orm.nombre,
                sku=producto_orm.sku,
                descripcion=producto_orm.descripcion,
                stock=producto_orm.stock,
                stock_minimo=producto_orm.stock_minimo
            )
            print(producto_response)
    except Exception as e:
        print(f"Error al obtener los productos: {e}")

def listar_movimientos():
    #No implementada solo test para ENUM
    print(TipoMovimiento.SALIDA.value)

def insertar_usuario():
    try:
        username = input("Ingrese el nombre del usuario: ")
        email = input("Ingrese el email del usuario: ")
        password = input("Ingrese la contraseña del usuario: ")

        try:
            password_hashed = hashear_password(password)
        except Exception as e:
            print(f"Error al hashear la contraseña: {e}")
            return {"success": False, "errors": [e]}

        usuarioCreate = UsuarioCreate(
            username=username,
            email=email,
            hashed_password=password_hashed,
            is_active=True
        )
        usuarioORM = usuario_a_usuario_orm(usuarioCreate)
        db.add(usuarioORM)
        db.commit()
        print("Usuario insertado correctamente")

    except ValidationError as ve:
        errores = [] #Declaramos la lista antes del bucle
        for error in ve.errors():
            # Extraer solo el mensaje personalizado del error
            if 'ctx' in error and 'error' in error['ctx']:
                message = str(error['ctx']['error'])
            else:
                # Para otros tipos de errores, usar el mensaje directo
                message = error['msg']
            #Guardamos el mensaje del error en la lista
            errores.append(message)
        print("Errores de validación:")
        for error in errores:
            print(f"- {error}")
        return {"success": False, "errors": errores}
    except Exception as e:
        print(f"Error al insertar el usuario: {e}")

def menu_producto():
    while True:
        print("1. Insertar producto")
        print("2. Ver productos")
        print("3. Listar movimientos")
        print("4. Insertar usuario")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                insertar_producto()
            case "2":
                ver_productos()
            case "3":
                listar_movimientos()
            case "4":
                insertar_usuario()
            case "5":
                break


menu_producto()

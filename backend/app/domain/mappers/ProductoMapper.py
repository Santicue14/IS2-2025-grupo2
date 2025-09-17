from app.domain.models.Producto import Producto
from app.db.models.ProductoORM import ProductoORM
from app.schemas.ProductoCreate import ProductoCreate
from pydantic import ValidationError

#Mapper de ProductoCreate a ProductoORM
def producto_a_producto_orm(producto_create: ProductoCreate) -> ProductoORM:
    try:
        return ProductoORM(
            nombre=producto_create.nombre,
            sku=producto_create.sku,
            descripcion=producto_create.descripcion,
            stock=producto_create.stock,
            stock_minimo=producto_create.stock_minimo
        )
    except Exception as e:
        raise ValueError(f"Error al convertir ProductoCreate a ProductoORM: {e}")

#Mapper de ProductoORM a producto
def producto_orm_a_producto(producto_orm: ProductoORM) -> Producto:
    try:
        return Producto(
            nombre=producto_orm.nombre,
            sku=producto_orm.sku,
            descripcion=producto_orm.descripcion,
            stock=producto_orm.stock,
            stock_minimo=producto_orm.stock_minimo
        )
    except Exception as e:
        raise ValueError(f"Error al convertir ProductoORM a Producto: {e}")

#Mapper de ProductoCreate a ProductoORM
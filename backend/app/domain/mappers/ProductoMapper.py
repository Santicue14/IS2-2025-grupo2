from app.domain.models.Producto import Producto
from app.db.models.ProductoORM import ProductoORM

#Mapper de producto a ProductoORM
def producto_a_producto_orm(producto: Producto) -> ProductoORM:
    return ProductoORM(
        nombre=producto.nombre,
        sku=producto.sku,
        descripcion=producto.descripcion,
        stock=producto.stock,
        stock_minimo=producto.stock_minimo
    )

#Mapper de ProductoORM a producto
def producto_orm_a_producto(producto_orm: ProductoORM) -> Producto:
    return Producto(
        nombre=producto_orm.nombre,
        sku=producto_orm.sku,
        descripcion=producto_orm.descripcion,
        stock=producto_orm.stock,
        stock_minimo=producto_orm.stock_minimo
    )

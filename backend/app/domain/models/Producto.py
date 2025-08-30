class Producto():
    def __init__(self,id,nombre,precio,cantidadStock, stockMinimo):
        self.id = id
        self.nombre= nombre
        self.precio= precio
        self.cantidadStock = cantidadStock
        self.stockMinimo = stockMinimo

    def alerta_minimo(self):
        if self.cantidadStock <= self.stockMinimo:
            print(f"Alerta: el producto {self.id}, {self.nombre}, tiene stock bajo ({self.cantidadStock})")
        


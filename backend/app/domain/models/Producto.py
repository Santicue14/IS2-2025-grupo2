class Producto():
    nombre: str
    sku: str
    descripcion: str
    stock: int
    stock_minimo: int


    def __init__(self,nombre,sku,descripcion,stock, stock_minimo):
        self.nombre: str = nombre
        self.sku: str = sku
        self.descripcion: str = descripcion
        self.stock: int = stock
        self.stock_minimo: int = stock_minimo

    def __str__(self):
        return f"""
        Producto: {self.nombre}
        SKU: {self.sku}
        Stock: {self.stock} 
        Stock mínimo: {self.stock_minimo}
        """

    def alerta_minimo(self):
        if self.stock <= self.stock_minimo:
            print(f"Alerta: el producto {self.nombre}, tiene stock bajo ({self.stock})")
        


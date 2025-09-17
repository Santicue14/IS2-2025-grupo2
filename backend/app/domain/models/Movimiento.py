from app.domain.models.Producto import Producto
from app.domain.models.Deposito import Deposito
from app.domain.models.Usuario import Usuario
from app.domain.models.Tipo import TipoMovimiento
from datetime import datetime

class Movimiento:
    producto: Producto
    producto_id: int
    deposito_origen: Deposito
    deposito_origen_id: int
    deposito_destino: Deposito
    deposito_destino_id: int
    usuario: Usuario
    usuario_id: int
    cantidad: int
    fecha: datetime
    tipo: TipoMovimiento

    def __init__(self,producto,producto_id,deposito_origen,deposito_origen_id,deposito_destino,deposito_destino_id,usuario,usuario_id,cantidad,fecha,tipo):
        self.producto: Producto = producto
        self.producto_id: int = producto_id
        self.deposito_origen: Deposito = deposito_origen
        self.deposito_origen_id: int = deposito_origen_id
        self.deposito_destino: Deposito = deposito_destino
        self.deposito_destino_id: int = deposito_destino_id
        self.usuario: Usuario = usuario
        self.usuario_id: int = usuario_id
        self.cantidad: int = cantidad
        self.fecha: datetime = fecha
        self.tipo: TipoMovimiento = tipo

    def __str__(self):
        return f"""
        Movimiento: {self.producto}
        Producto ID: {self.producto_id}
        Deposito Origen: {self.deposito_origen}
        Deposito Origen ID: {self.deposito_origen_id}
        Deposito Destino: {self.deposito_destino}
        Deposito Destino ID: {self.deposito_destino_id}
        Usuario: {self.usuario}
        Usuario ID: {self.usuario_id}
        """

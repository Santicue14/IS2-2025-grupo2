from app.domain.models.Rol import Rol
from app.domain.models.Movimiento import Movimiento

class Usuario:
    username: str
    email: str
    hashed_password: str
    is_active: bool
    roles: list[Rol] | None
    movimientos: list[Movimiento] | None

    def __init__(self,username,email,hashed_password,is_active,roles,movimientos):
        self.username: str = username
        self.email: str = email
        self.hashed_password: str = hashed_password
        self.is_active: bool = is_active
        self.roles: list[Rol] = roles

    def __str__(self):
        return f"""
        Usuario: {self.username}
        Email: {self.email}
        Activo: {self.is_active}
        Roles: {self.roles}
        Movimientos: {self.movimientos}
        """
        
        
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.models.Usuario import Usuario

class Rol:
    nombre: str
    usuarios: list[Usuario] | None

    def __init__(self,nombre):
        self.nombre: str = nombre
    
    def __str__(self):
        return f"""
        Rol: {self.nombre}
        Usuarios: {self.usuarios}
        """

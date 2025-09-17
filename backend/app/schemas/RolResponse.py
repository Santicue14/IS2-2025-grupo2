from pydantic import BaseModel

class RolResponse(BaseModel):
    nombre: str
    usuarios: list[UsuarioCreate] | None
    
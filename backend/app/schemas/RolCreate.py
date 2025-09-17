from pydantic import BaseModel, Field, field_validator
from app.schemas import UsuarioCreate

class RolCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del rol")
    usuarios: list[UsuarioCreate] | None = Field(None, description="Lista de usuarios asociados al rol")
    
    #Validaciones
    @field_validator('nombre')
    def validar_nombre(cls, v):
        if not v.strip(): #Valida que no esté vacío
            raise ValueError('El nombre no puede estar vacío')
        if len(v.strip()) < 2: #Valida que tenga al menos 2 caracteres
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        if len(v.strip()) > 100: #Valida que no exceda 100 caracteres
            raise ValueError('El nombre no puede exceder 100 caracteres')
        return v.strip()
    
    @field_validator('usuarios')
    def validar_usuarios(cls, v):
        if v is not None and len(v) == 0: #Valida que si la lista no es None, no esté vacía
            raise ValueError('La lista de usuarios no puede estar vacía')
        
    

   
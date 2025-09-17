from pydantic import BaseModel, Field, field_validator


class RolCreate(BaseModel):
    nombre: str = Field(..., description="Nombre del rol")
    

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
    
class RolResponse(BaseModel):
    nombre: str
    
    
    
from pydantic import BaseModel, Field, field_validator
import re

class UsuarioCreate(BaseModel):
    username: str = Field(..., description="Nombre de usuario")
    email: str = Field(..., description="Email del usuario")
    hashed_password: str = Field(..., description="Contraseña hasheada")
    is_active: bool = Field(..., description="Estado activo del usuario")
    
    # Validaciones de campos y mensajes de error
    @field_validator('username')
    def validar_username(cls, v):
        if not v.strip(): #Valida que no esté vacío
            raise ValueError('El username no puede estar vacío')
        if len(v.strip()) < 2: #Valida que tenga al menos 2 caracteres
            raise ValueError('El username debe tener al menos 2 caracteres')
        if len(v.strip()) > 50: #Valida que no exceda 50 caracteres
            raise ValueError('El username no puede exceder 50 caracteres')
        return v.strip()
    
    @field_validator('email')
    def validar_email(cls, v):
        if not v.strip(): #Valida que no esté vacío
            raise ValueError("El email no puede estar vacío")
        if len(v.strip()) < 5: #Valida que tenga al menos 5 caracteres
            raise ValueError('El email debe tener al menos 5 caracteres')
        if len(v.strip()) > 100: #Valida que no exceda 100 caracteres
            raise ValueError('El email no puede exceder 100 caracteres')
        # Validación básica de formato de email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, v.strip()):
            raise ValueError('El email debe tener un formato válido')
        return v.strip()
    
    @field_validator('hashed_password')
    def validar_hashed_password(cls, v):
        if not v.strip(): #Valida que no esté vacío
            raise ValueError('La contraseña hasheada no puede estar vacía')
        if len(v.strip()) < 10: #Valida que tenga al menos 10 caracteres (hash mínimo)
            raise ValueError('La contraseña hasheada debe tener al menos 10 caracteres')
        return v.strip()

class UsuarioResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
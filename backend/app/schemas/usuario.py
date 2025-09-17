from pydantic import BaseModel, Field, field_validator

class UsuarioCreate(BaseModel):
    username: str = Field(..., description="Nombre del producto")
    email: str = Field(..., description="Código SKU único")
    hashed_password: str = Field(..., description="Contraseña hashed")
    is_active: bool = Field(..., description="Activo")
    
    # Validaciones de campos y mensajes de error
    @field_validator('username')
    def validar_nombre(cls, v):
        if not v.strip(): #Valida que no esté vacío
            raise ValueError('El username no puede estar vacío')
        if len(v.strip()) < 2: #Valida que tenga al menos 2 caracteres
            raise ValueError('El username debe tener al menos 2 caracteres')
        if len(v.strip()) > 100: #Valida que no exceda 100 caracteres
            raise ValueError('El username no puede exceder 100 caracteres')
        return v.strip()
    
    
    
    @field_validator('email')
    def validar_sku(cls, v):
        if not v.strip(): #Valida que no esté vacío
            raise ValueError("El email no puede estar vacío")
        if len(v.strip()) < 3: #Valida que tenga al menos 3 caracteres
            raise ValueError('El email debe tener al menos 3 caracteres')
        if len(v.strip()) > 20: #Valida que no exceda 20 caracteres
            raise ValueError('El email no puede exceder 20 caracteres')
        return v.strip()
    
    @field_validator('descripcion')
    def validar_descripcion(cls, v):
        if not v.strip(): #Valida que la descripción no esté vacía
            raise ValueError('La descripción no puede estar vacía')
        if len(v.strip()) < 10: #Valida que tenga al menos 10 caracteres
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        if len(v.strip()) > 500: #Valida que no exceda 500 caracteres
            raise ValueError('La descripción no puede exceder 500 caracteres')
        return v

    @field_validator('stock')
    def validar_stock_str(cls, v):
        if not v.isdigit(): #Valida que el stock sea un número
            raise ValueError('El stock debe ser un número')
        return int(v)
    def validar_stock(cls, v):
        if v < 0: #Valida que el stock no sea negativo
            raise ValueError('El stock no puede ser negativo')
        return v
    def validar_int(cls, v):
        if not v.isdigit(): #Valida que el stock sea un número
            raise ValueError('El stock debe ser un número')
        return int(v)
    
    @field_validator('stock_minimo')
    def validar_stock_minimo_str(cls, v):
        if not v.isdigit(): #Valida que el stock mínimo sea un número
            raise ValueError('El stock mínimo debe ser un número')
        return int(v)
    def validar_stock_minimo(cls, v):
        if v < 0: #Valida que el stock mínimo no sea negativo
            raise ValueError('El stock mínimo no puede ser negativo')
        return v
    def validar_stock_minimo_int(cls, v):
        if not v.isdigit(): #Valida que el stock mínimo sea un número
            raise ValueError('El stock mínimo debe ser un número')
        return int(v)

class ProductoResponse(BaseModel):
    id: int
    nombre: str
    sku: str
    descripcion: str
    stock: int
    stock_minimo: int
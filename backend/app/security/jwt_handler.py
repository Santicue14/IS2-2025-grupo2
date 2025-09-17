from app.core.config import settings
from jose import jwt
from datetime import datetime, timedelta
import secrets
import hashlib
import base64

ALGORITHM = "HS256"

def hashear_password(password: str) -> str:
    """Hashea una contraseña usando PBKDF2 con salt aleatorio"""
    salt = secrets.token_bytes(16)  # Genera un salt aleatorio
    password_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    # Codificar en base64 para almacenar como string
    return base64.b64encode(salt + password_hash).decode('utf-8')

def verificar_password(password: str, hashed_password: str) -> bool:
    """Verifica una contraseña contra su hash"""
    try:
        # Decodificar desde base64
        decoded = base64.b64decode(hashed_password.encode('utf-8'))
        salt = decoded[:16]  # Obtiene el salt del hash
        stored_hash = decoded[16:]  # Obtiene el hash de la contraseña
        
        # Generar hash de la contraseña ingresada
        password_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
        return password_hash == stored_hash
    except Exception:
        return False

def create_token_acceso(data: dict, expires_delta: timedelta = None):
    """Crea un token JWT con expiración"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=1)  # 1 hora por defecto
    
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)

def decode_token_acceso(token: str) -> dict:
    # Retorna un diccionario con el username (sub) y el rol (rol)
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[ALGORITHM])

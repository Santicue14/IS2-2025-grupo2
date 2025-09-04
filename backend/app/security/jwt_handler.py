from app.core.config import settings
from jose import JWTError, jwt 

def create_hashed_password(password: str) -> str:
    password: str = password
    hashed_password: str = jwt.encode(password, settings.JWT_SECRET_KEY, algorithm="HS256")
    return hashed_password
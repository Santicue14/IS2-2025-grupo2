from app.domain.models.Usuario import Usuario
from app.db.models.UsuarioORM import UsuarioORM
from app.schemas.usuario import UsuarioCreate

#Mapper de UsuarioCreate a UsuarioORM
def usuario_a_usuario_orm(usuario_create: UsuarioCreate) -> UsuarioORM:
    try:
        return UsuarioORM(
            username=usuario_create.username,
            email=usuario_create.email,
            hashed_password=usuario_create.hashed_password,
            is_active=usuario_create.is_active
        )
    except Exception as e:
        raise ValueError(f"Error al convertir UsuarioCreate a UsuarioORM: {e}")

#Mapper de UsuarioORM a Usuario
def usuario_orm_a_usuario(usuario_orm: UsuarioORM) -> Usuario:
    try:
        return Usuario(
            username=usuario_orm.username,
            email=usuario_orm.email,
            hashed_password=usuario_orm.hashed_password,
            is_active=usuario_orm.is_active
        )
    except Exception as e:
        raise ValueError(f"Error al convertir UsuarioORM a Usuario: {e}")

#Mapper de UsuarioCreate a UsuarioORM
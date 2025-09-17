from app.db.models.UsuarioORM import UsuarioORM
from app.domain.models.Usuario import Usuario

#Mapper de usuario a UsuarioORM

def Usuario_a_UsuarioORM(usuario: Usuario) ->UsuarioORM:
    return UsuarioORM(
        username=usuario.username,
        email=usuario.email,
        hashed_password=usuario.hashed_password,
        is_active=usuario.is_active
    )
    
def UsuarioORM_a_Usuario(usuarioORM: UsuarioORM) -> Usuario:
    return Usuario(
        username=usuarioORM.username,
        email=usuarioORM.email,
        hashed_password=usuarioORM.hashed_password,
        is_active=usuarioORM.is_active,
        roles=usuarioORM.roles, # no estoy seguro, fijense porfa
        movimientos=usuarioORM.movimientos # no estoy seguro, fijense porfa
    )



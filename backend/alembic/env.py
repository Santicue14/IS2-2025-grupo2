import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Esto es para que Alembic pueda encontrar los módulos de tu proyecto
sys.path = ['', '..'] + sys.path

# alembic/env.py

# ... (código existente)
from backend.app.db.base import Base

# Asegúrate de importar todos tus modelos para que Alembic los reconozca.
# La siguiente línea importa todos los archivos dentro de la carpeta models.
from backend.app.db.models.deposito import DepositoORM
from backend.app.db.models.movimiento import MovimientoORM
from backend.app.db.models.producto import ProductoORM
from backend.app.db.models.rol import RolORM
from backend.app.db.models.usuario import UsuarioORM

# Agrega aquí los demás modelos...
# Agrega aquí los demás modelos...
# ... (resto del código)
from backend.app.db.engine import engine

# 2. Configura los metadatos
target_metadata = Base.metadata

# Esto es el Alembic Config object, el cual provee acceso a los valores dentro del archivo .ini
config = context.config

# Interpreta el archivo de configuración para logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine  # 3. Usa el motor de tu proyecto directamente

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
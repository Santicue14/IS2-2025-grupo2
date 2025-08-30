from enum import Enum

# Tipos de movimientos
class TipoMovimiento(Enum):
    INGRESO = 1
    SALIDA = 2

    def __str__(self):
        return f"""
        Tipo de movimiento: {self.name}
        """
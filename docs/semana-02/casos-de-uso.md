# Casos de uso

Se detallan a continuación los casos de uso, sobre los que se estarán trabajando.
Estos fueron realizados en base a los hitos dentro del [proyecto](https://github.com/users/Santicue14/projects/4/views/5?filterQuery=).

- [Actores principales](#actores)
- [Casos de uso](#casos)
    - [ABM de productos](#abm-de-productos)
    - [Movimiento de stock](#movimiento-de-stock)
    - [ABM de depósitos](#abm-de-depositos)
    - [Login y permisos](#login-y-permisos)
    - [Consulta de stock](#consulta-de-stock)
    - [Alertas](#alertas)

## Actores:

1. Administrador
2. Operador de depósito

## Casos

### ABM de productos

**Actor principal:** Administrador

**Descripción:** "Como administrador quiero dar de alta, modificar o eliminar productos, para mantener actualizada la base de datos y asegurar que el sistema refleje el contenido actual y real de la empresa”

### Movimiento de stock

**Actores principales:** Administrador y Sistema

**Descripción:** El objetivo es mantener un registro dentro del sistema de las entradas y salidas de stock, reflejando el inventario disponible

### ABM de depositos

 **Actor principal:** Administrador 

  **Descripción:** "Como administrador quiero dar de alta, modificar o eliminar depósitos, para mantener actualizada la base de datos y asegurar que el sistema refleje el contenido actual y real de la empresa”

### Login y permisos
**Actor principal:** Usuario General. 

**Descripción:** “Como usuario quiero iniciar sesión con mis credenciales y tener permisos diferenciados según mi rol, para garantizar la seguridad y el uso determinado del sistema, según corresponda”


### Consulta de stock

**Actor principal:** Usuario

**Descripción:** "el usuario selecciona la función "ver stock" y se muestran las existencias de los productos."

### Alertas
**Actor principal:** Sistema 

**Descripción:** Dar alerta cuando baja el stock de un producto
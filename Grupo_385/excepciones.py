# Excepción personalizada para errores de clientes
class ClienteError(Exception):
    pass


# Excepción personalizada para errores de servicios
class ServicioError(Exception):
    pass


# Excepción personalizada para errores de reservas
class ReservaError(Exception):
    pass
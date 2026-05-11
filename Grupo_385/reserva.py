# Importamos excepción personalizada
from excepciones import ReservaError


# Clase Reserva
class Reserva:

    # Constructor
    def __init__(self, cliente, servicio, duracion):

        # Validamos duración
        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # Método para confirmar reserva
    def confirmar(self):
        self.estado = "Confirmada"

    # Método para cancelar reserva
    def cancelar(self):
        self.estado = "Cancelada"

    # Método para procesar reserva
    def procesar(self):

        try:

            # Calculamos costo
            costo = self.servicio.calcular_costo()

        except Exception as e:

            # Encadenamiento de excepción
            raise ReservaError("Error procesando reserva") from e

        else:

            # Retornamos costo total
            return costo * self.duracion

        finally:

            # Mensaje final del proceso
            print("Proceso de reserva finalizado")
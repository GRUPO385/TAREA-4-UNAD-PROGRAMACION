# Importamos clases abstractas
from abc import ABC, abstractmethod

# Importamos excepción personalizada
from excepciones import ServicioError


# Clase abstracta Servicio
class Servicio(ABC):

    # Constructor
    def __init__(self, nombre, precio):

        # Validamos precio
        if precio <= 0:
            raise ServicioError("El precio debe ser mayor a cero")

        self.nombre = nombre
        self.precio = precio

    # Método abstracto para calcular costo
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto para descripción
    @abstractmethod
    def descripcion(self):
        pass


# Clase hija ReservaSala
class ReservaSala(Servicio):

    # Sobrescritura del método calcular_costo
    def calcular_costo(self):
        return self.precio * 2

    # Descripción del servicio
    def descripcion(self):
        return "Servicio de reserva de salas"


# Clase hija AlquilerEquipo
class AlquilerEquipo(Servicio):

    # Sobrescritura del método calcular_costo
    def calcular_costo(self):
        return self.precio * 3

    # Descripción del servicio
    def descripcion(self):
        return "Servicio de alquiler de equipos"


# Clase hija AsesoriaEspecializada
class AsesoriaEspecializada(Servicio):

    # Sobrescritura del método calcular_costo
    def calcular_costo(self):
        return self.precio * 4

    # Descripción del servicio
    def descripcion(self):
        return "Servicio de asesoría especializada"
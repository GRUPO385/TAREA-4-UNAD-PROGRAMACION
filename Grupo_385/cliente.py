# Importamos excepción personalizada
from excepciones import ClienteError


# Clase Cliente
class Cliente:

    # Constructor de la clase
    def __init__(self, nombre, correo, telefono):

        # Validamos que el nombre no esté vacío
        if nombre == "":
            raise ClienteError("El nombre no puede estar vacío")

        # Validamos el correo
        if "@" not in correo:
            raise ClienteError("Correo inválido")

        # Validamos teléfono
        if len(telefono) < 7:
            raise ClienteError("Teléfono inválido")

        # Encapsulación de atributos
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Método para mostrar información
    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__correo}"

    # Método getter
    def get_nombre(self):
        return self.__nombre
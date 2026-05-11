# Importamos clases
from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import AsesoriaEspecializada
from reserva import Reserva


# Función para guardar logs
def guardar_log(mensaje):

    archivo = open("logs.txt", "a")

    archivo.write(mensaje + "\n")

    archivo.close()


# Título del sistema
print("===== SISTEMA DE RESERVAS =====\n")


# OPERACION 1
# Registro de cliente válido
try:

    cliente1 = Cliente(
        "Carlos",
        "carlos@gmail.com",
        "1234567"
    )

    print(cliente1.mostrar_info())

    guardar_log("Cliente válido registrado")

except Exception as e:

    print(e)

    guardar_log(str(e))


# OPERACION 2
# Registro inválido
try:

    cliente2 = Cliente(
        "",
        "correo",
        "12"
    )

except Exception as e:

    print("Error:", e)

    guardar_log(str(e))


# OPERACION 3
# Servicio reserva sala
try:

    servicio1 = ReservaSala(
        "Sala VIP",
        100
    )

    print(servicio1.descripcion())

except Exception as e:

    print(e)

    guardar_log(str(e))


# OPERACION 4
# Servicio alquiler equipos
try:

    servicio2 = AlquilerEquipo(
        "Computadores",
        150
    )

    print(servicio2.descripcion())

except Exception as e:

    print(e)

    guardar_log(str(e))


# OPERACION 5
# Servicio asesoría
try:

    servicio3 = AsesoriaEspecializada(
        "Python",
        200
    )

    print(servicio3.descripcion())

except Exception as e:

    print(e)

    guardar_log(str(e))


# OPERACION 6
# Reserva exitosa
try:

    reserva1 = Reserva(
        cliente1,
        servicio1,
        2
    )

    reserva1.confirmar()

    total = reserva1.procesar()

    print("Costo total:", total)

    guardar_log("Reserva exitosa")

except Exception as e:

    print(e)

    guardar_log(str(e))


# OPERACION 7
# Reserva inválida
try:

    reserva2 = Reserva(
        cliente1,
        servicio2,
        -5
    )

except Exception as e:

    print("Error:", e)

    guardar_log(str(e))


# OPERACION 8
# Reserva cancelada
try:

    reserva3 = Reserva(
        cliente1,
        servicio3,
        1
    )

    reserva3.cancelar()

    print("Reserva cancelada")

    guardar_log("Reserva cancelada")

except Exception as e:

    print(e)

    guardar_log(str(e))


# OPERACION 9
# Segundo cliente válido
try:

    cliente4 = Cliente(
        "Ana",
        "ana@gmail.com",
        "7654321"
    )

    print(cliente4.mostrar_info())

except Exception as e:

    print(e)

    guardar_log(str(e))


# OPERACION 10
# Nueva reserva exitosa
try:

    reserva4 = Reserva(
        cliente4,
        servicio1,
        3
    )

    total = reserva4.procesar()

    print("Total reserva:", total)

    guardar_log("Reserva procesada")

except Exception as e:

    print(e)

    guardar_log(str(e))
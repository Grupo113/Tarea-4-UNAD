# main.py

"""
=====================================================
SISTEMA SOFTWARE FJ
=====================================================

Sistema orientado a objetos para gestión de:

✔ Clientes
✔ Servicios
✔ Reservas

El sistema implementa:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones

Características principales:

✔ Sin base de datos
✔ Manejo mediante objetos y listas
✔ Registro de eventos y errores
✔ Validaciones robustas
✔ Continuidad del sistema ante fallos

El sistema simula más de 10 operaciones,
incluyendo casos válidos e inválidos.
"""

# =====================================================
# IMPORTACIONES
# =====================================================

import logging
import os

from models.cliente import Cliente

from models.servicio import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)

from models.reserva import Reserva

from exceptions.custom_exceptions import (
    ClienteError,
    ServicioError,
    ReservaError
)

# =====================================================
# CONFIGURACIÓN DE LOGS
# =====================================================

# Crear carpeta data automáticamente
os.makedirs("data", exist_ok=True)

logging.basicConfig(
    filename="data/logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("software_fj")

# =====================================================
# FUNCIÓN PRINCIPAL
# =====================================================

def main():
    """
    Función principal del sistema.

    Aquí se realizan múltiples operaciones:

    ✔ Clientes válidos e inválidos
    ✔ Servicios válidos e inválidos
    ✔ Reservas exitosas y fallidas
    ✔ Confirmaciones
    ✔ Cancelaciones
    ✔ Finalizaciones
    ✔ Manejo robusto de errores
    """

    print("\n====================================================")
    print("              SISTEMA SOFTWARE FJ")
    print("====================================================")

    logger.info("Sistema iniciado correctamente.")

    # =================================================
    # LISTAS INTERNAS DEL SISTEMA
    # =================================================

    """
    El sistema NO utiliza bases de datos.

    Toda la información se almacena
    temporalmente mediante listas.
    """

    clientes = []
    servicios = []
    reservas = []

    # =================================================
    # OPERACIÓN 1 — CLIENTE VÁLIDO
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 1 — CLIENTE VÁLIDO")
    print("====================================================")

    try:

        cliente1 = Cliente(
            "CLI001",
            "Carlos Ramirez",
            "carlos@gmail.com",
            "+573001112233"
        )

        clientes.append(cliente1)

        print("✔ Cliente válido registrado.")

        logger.info(
            "Cliente válido registrado."
        )

    except ClienteError as error:

        print(f"✘ Error cliente: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 2 — CLIENTE INVÁLIDO
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 2 — CLIENTE INVÁLIDO")
    print("====================================================")

    try:

        cliente2 = Cliente(
            "",
            "12",
            "correo_invalido",
            "abc"
        )

        clientes.append(cliente2)

    except ClienteError as error:

        print(
            f"✔ Error controlado: {error}"
        )

        logger.error(error)

    # =================================================
    # OPERACIÓN 3 — SERVICIO SALA VÁLIDO
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 3 — SERVICIO SALA VÁLIDO")
    print("====================================================")

    try:

        sala = ServicioSala(
            "Sala Premium",
            120000,
            30
        )

        servicios.append(sala)

        print("✔ Servicio sala registrado.")

        logger.info(
            "Servicio sala registrado."
        )

    except ServicioError as error:

        print(f"✘ Error servicio: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 4 — SERVICIO EQUIPO VÁLIDO
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 4 — SERVICIO EQUIPO VÁLIDO")
    print("====================================================")

    try:

        equipo = ServicioEquipo(
            "Alquiler Portátiles",
            80000,
            "Portátil Gamer"
        )

        servicios.append(equipo)

        print("✔ Servicio equipo registrado.")

        logger.info(
            "Servicio equipo registrado."
        )

    except ServicioError as error:

        print(f"✘ Error servicio: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 5 — SERVICIO ASESORÍA VÁLIDO
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 5 — SERVICIO ASESORÍA VÁLIDO")
    print("====================================================")

    try:

        asesoria = ServicioAsesoria(
            "Asesoría Python",
            150000,
            "Ingeniero Senior"
        )

        servicios.append(asesoria)

        print("✔ Servicio asesoría registrado.")

        logger.info(
            "Servicio asesoría registrada."
        )

    except ServicioError as error:

        print(f"✘ Error servicio: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 6 — SERVICIO INVÁLIDO
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 6 — SERVICIO INVÁLIDO")
    print("====================================================")

    try:

        servicio_invalido = ServicioSala(
            "",
            -500,
            0
        )

        servicios.append(servicio_invalido)

    except ServicioError as error:

        print(
            f"✔ Error controlado: {error}"
        )

        logger.error(error)

    # =================================================
    # OPERACIÓN 7 — RESERVA VÁLIDA
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 7 — RESERVA VÁLIDA")
    print("====================================================")

    try:

        reserva1 = Reserva(
            cliente1,
            sala,
            5
        )

        reservas.append(reserva1)

        reserva1.confirmar()

        total = reserva1.calcular_total()

        print(
            f"✔ Reserva confirmada. "
            f"Total: ${total}"
        )

        logger.info(
            "Reserva válida procesada."
        )

    except ReservaError as error:

        print(f"✘ Error reserva: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 8 — RESERVA CON DESCUENTO
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 8 — RESERVA CON DESCUENTO")
    print("====================================================")

    try:

        reserva2 = Reserva(
            cliente1,
            equipo,
            3
        )

        reservas.append(reserva2)

        reserva2.confirmar()

        total = reserva2.calcular_total(0.10)

        print(
            f"✔ Reserva con descuento. "
            f"Total: ${total}"
        )

        logger.info(
            "Reserva con descuento procesada."
        )

    except ReservaError as error:

        print(f"✘ Error reserva: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 9 — RESERVA INVÁLIDA
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 9 — RESERVA INVÁLIDA")
    print("====================================================")

    try:

        reserva_invalida = Reserva(
            "cliente falso",
            asesoria,
            -8
        )

        reservas.append(reserva_invalida)

    except ReservaError as error:

        print(
            f"✔ Error controlado: {error}"
        )

        logger.error(error)

    # =================================================
    # OPERACIÓN 10 — FINALIZAR RESERVA
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 10 — FINALIZAR RESERVA")
    print("====================================================")

    try:

        reserva1.finalizar()

        print(
            "✔ Reserva finalizada correctamente."
        )

        logger.info(
            "Reserva finalizada."
        )

    except ReservaError as error:

        print(
            f"✘ Error finalizando reserva: {error}"
        )

        logger.error(error)

    # =================================================
    # OPERACIÓN 11 — CANCELAR RESERVA
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 11 — CANCELAR RESERVA")
    print("====================================================")

    try:

        reserva2.cancelar()

        print(
            "✔ Reserva cancelada correctamente."
        )

        logger.info(
            "Reserva cancelada."
        )

    except ReservaError as error:

        print(
            f"✘ Error cancelando reserva: {error}"
        )

        logger.error(error)

    # =================================================
    # OPERACIÓN 12 — TRY / EXCEPT / ELSE / FINALLY
    # =================================================

    print("\n====================================================")
    print("OPERACIÓN 12 — MANEJO AVANZADO DE EXCEPCIONES")
    print("====================================================")

    try:

        resultado = 10 / 2

    except ZeroDivisionError as error:

        print(
            f"✘ Error matemático: {error}"
        )

        logger.error(error)

    else:

        print(
            "✔ Operación matemática exitosa."
        )

        logger.info(
            "Operación matemática ejecutada."
        )

    finally:

        print(
            "✔ Bloque finally ejecutado."
        )

        logger.info(
            "Bloque finally ejecutado."
        )

    # =================================================
    # RESUMEN FINAL
    # =================================================

    print("\n====================================================")
    print("                 RESUMEN FINAL")
    print("====================================================")

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas registradas: {len(reservas)}")

    logger.info(
        "Sistema finalizado correctamente."
    )

    print("\n✔ Sistema ejecutado correctamente.")
    print("✔ Logs registrados en data/logs.txt")

    print("\n====================================================")

# =====================================================
# EJECUCIÓN PRINCIPAL
# =====================================================

if __name__ == "__main__":

    try:

        main()

    except Exception as error:

        print(
            "\n✘ Error crítico del sistema:",
            error
        )

        logger.critical(
            "Error crítico no controlado: %s",
            error
        )
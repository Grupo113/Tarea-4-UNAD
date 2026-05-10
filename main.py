"""
main.py

Archivo principal del sistema Software FJ.

Este módulo se encarga de:

- Integrar todos los componentes del sistema
- Ejecutar pruebas funcionales
- Simular operaciones reales
- Manejar excepciones globales
- Registrar eventos y errores
- Garantizar estabilidad del sistema

El sistema implementa:
- Programación Orientada a Objetos
- Manejo avanzado de excepciones
- Polimorfismo
- Encapsulación
- Herencia
- Abstracción

NO se utilizan bases de datos.
Toda la información se maneja mediante:
- Objetos
- Listas
- Archivos de logs
"""

# =====================================================
# IMPORTACIONES
# =====================================================

import os
import logging

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
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# =====================================================

"""
El sistema registra todos los eventos y errores
en el archivo:

data/logs.txt

Esto permite:
- auditoría
- seguimiento de errores
- trazabilidad del sistema
"""

# Crear carpeta data automáticamente
os.makedirs("data", exist_ok=True)

logging.basicConfig(
    filename="data/logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Logger principal
logger = logging.getLogger("software_fj")

# =====================================================
# FUNCIÓN PRINCIPAL DEL SISTEMA
# =====================================================

def main():
    """
    Función principal del sistema.

    Aquí se ejecutan:
    - Creación de clientes
    - Creación de servicios
    - Creación de reservas
    - Validaciones
    - Manejo de errores

    El sistema debe continuar funcionando
    aun cuando existan errores.
    """

    print("\n====================================")
    print("     SISTEMA SOFTWARE FJ")
    print("====================================\n")

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
    # OPERACIÓN 1
    # CREAR CLIENTE VÁLIDO
    # =================================================

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
            "Cliente registrado correctamente."
        )

    except ClienteError as error:

        print(f"✘ Error cliente: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 2
    # CREAR CLIENTE INVÁLIDO
    # =================================================

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
            f"✔ Error controlado "
            f"en cliente inválido: {error}"
        )

        logger.error(error)

    # =================================================
    # OPERACIÓN 3
    # CREAR SERVICIO SALA
    # =================================================

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

        print(f"✘ Error servicio sala: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 4
    # CREAR SERVICIO EQUIPO
    # =================================================

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

        print(f"✘ Error servicio equipo: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 5
    # CREAR SERVICIO ASESORÍA
    # =================================================

    try:

        asesoria = ServicioAsesoria(
            "Asesoría Python",
            150000,
            "Ingeniero Senior"
        )

        servicios.append(asesoria)

        print("✔ Servicio asesoría registrado.")

        logger.info(
            "Servicio asesoría registrado."
        )

    except ServicioError as error:

        print(f"✘ Error servicio asesoría: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 6
    # CREAR SERVICIO INVÁLIDO
    # =================================================

    try:

        servicio_invalido = ServicioSala(
            "",
            -500,
            0
        )

        servicios.append(servicio_invalido)

    except ServicioError as error:

        print(
            f"✔ Error controlado "
            f"en servicio inválido: {error}"
        )

        logger.error(error)

    # =================================================
    # OPERACIÓN 7
    # CREAR RESERVA VÁLIDA
    # =================================================

    try:

        reserva1 = Reserva(
            cliente1,
            sala,
            5
        )

        reservas.append(reserva1)

        # Confirmar reserva
        reserva1.confirmar()

        # Calcular total
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
    # OPERACIÓN 8
    # RESERVA CON DESCUENTO
    # =================================================

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
            f"✔ Reserva con descuento procesada. "
            f"Total: ${total}"
        )

        logger.info(
            "Reserva con descuento procesada."
        )

    except ReservaError as error:

        print(f"✘ Error reserva: {error}")

        logger.error(error)

    # =================================================
    # OPERACIÓN 9
    # RESERVA INVÁLIDA
    # =================================================

    try:

        reserva_invalida = Reserva(
            "cliente falso",
            asesoria,
            -8
        )

        reservas.append(reserva_invalida)

    except ReservaError as error:

        print(
            f"✔ Error controlado "
            f"en reserva inválida: {error}"
        )

        logger.error(error)

    # =================================================
    # OPERACIÓN 10
    # FINALIZAR RESERVA
    # =================================================

    try:

        reserva1.finalizar()

        print("✔ Reserva finalizada correctamente.")

        logger.info(
            "Reserva finalizada."
        )

    except ReservaError as error:

        print(
            f"✘ Error finalizando reserva: {error}"
        )

        logger.error(error)

    # =================================================
    # EJEMPLO AVANZADO
    # try / except / else / finally
    # =================================================

    """
    La guía solicita demostrar:

    - try
    - except
    - else
    - finally

    Aquí se implementa un ejemplo completo.
    """

    try:

        print("\nProcesando operación avanzada...")

        resultado = 10 / 2

    except ZeroDivisionError as error:

        print(f"Error matemático: {error}")

        logger.error(error)

    else:

        print(
            "✔ Operación matemática ejecutada "
            "correctamente."
        )

        logger.info(
            "Operación matemática exitosa."
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

    print("\n====================================")
    print("      RESUMEN DEL SISTEMA")
    print("====================================\n")

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas registradas: {len(reservas)}")

    logger.info(
        "Sistema finalizado correctamente."
    )

    print("\n✔ Sistema ejecutado correctamente.")
    print("✔ Logs registrados en data/logs.txt")

    print("\n====================================")

# =====================================================
# EJECUCIÓN PRINCIPAL
# =====================================================

"""
Este bloque garantiza que el sistema
solo se ejecute directamente desde main.py
"""

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
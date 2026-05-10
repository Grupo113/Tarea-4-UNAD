# tests/test_sistema.py

"""
ORGANIZACIÓN DE PRUEBAS DEL SISTEMA
SOFTWARE FJ

Este archivo centraliza todas las pruebas
funcionales del sistema.

Incluye pruebas para:

✔ Clientes
✔ Servicios
✔ Reservas

Cada integrante aporta:
- 1 caso válido
- 1 caso inválido

El sistema debe:
- continuar funcionando ante errores
- registrar eventos
- demostrar manejo de excepciones
- aplicar try / except / else / finally

NO se utilizan bases de datos.
"""

# =====================================================
# IMPORTACIONES
# =====================================================

import sys
import os
import logging

# Permite importar módulos del proyecto
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# =====================================================
# CONFIGURACIÓN DE LOGS
# =====================================================

os.makedirs("data", exist_ok=True)

logger = logging.getLogger("software_fj")

if not logger.handlers:

    logger.setLevel(logging.DEBUG)

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # Archivo de logs
    file_handler = logging.FileHandler(
        "data/software_fj.log",
        encoding="utf-8"
    )

    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formato)

    # Consola
    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formato)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# =====================================================
# IMPORTS DEL PROYECTO
# =====================================================

from models.cliente import Cliente

from models.servicio import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)

from models.reserva import Reserva

from exceptions.custom_exceptions import (
    ClienteError,
    NombreInvalidoError,
    EmailInvalidoError,
    TelefonoInvalidoError,
    IDClienteInvalidoError,
    ServicioError,
    ReservaError
)

# =====================================================
# PRUEBAS CLIENTE
# (SE RESPETA LA LÓGICA DEL COMPAÑERO)
# =====================================================

def test_cliente_valido():
    """
    Caso válido de cliente.

    Verifica:
    - creación correcta
    - getters
    - setters
    - actualización controlada
    """

    logger.info("─" * 55)
    logger.info("CASO 1 — Registro válido de cliente")
    logger.info("─" * 55)

    print("\n─── CASO 1 — Registro válido de cliente ───")

    cliente = None

    try:

        cliente = Cliente(
            id_cliente="CLI001",
            nombre="Fernanda Jiménez López",
            email="fernanda@softwarefj.com",
            telefono="+573001234567",
        )

    except ClienteError as e:

        logger.error(
            "CASO 1 — Error inesperado: %s",
            e
        )

        print(f"  [ERROR] {e}")

    else:

        # Verificación de atributos
        assert cliente.id_cliente == "CLI001"
        assert cliente.nombre == "Fernanda Jiménez López"
        assert cliente.email == "fernanda@softwarefj.com"
        assert cliente.telefono == "+573001234567"

        # Actualización mediante setters
        cliente.email = "fernanda.nueva@softwarefj.com"
        cliente.telefono = "3109876543"

        assert cliente.email == "fernanda.nueva@softwarefj.com"
        assert cliente.telefono == "3109876543"

        logger.info(
            "CASO 1 EXITOSO — %s",
            cliente
        )

        print(f"  [OK] {cliente}")

    finally:

        logger.info("CASO 1 — Finalizado.")

        print("  [INFO] Caso 1 finalizado.\n")


def test_cliente_invalido():
    """
    Casos inválidos de cliente.

    El sistema:
    - detecta errores
    - registra errores
    - continúa funcionando
    """

    logger.info("─" * 55)
    logger.info("CASO 2 — Intentos inválidos de registro")
    logger.info("─" * 55)

    print("─── CASO 2 — Intentos inválidos de registro ───")

    sub_casos = [

        {
            "desc": "2a — Nombre con números",

            "datos": dict(
                id_cliente="CLI002",
                nombre="Juan123 Pérez",
                email="juan@softwarefj.com",
                telefono="3001112233"
            ),

            "excepcion": NombreInvalidoError,
        },

        {
            "desc": "2b — Email sin @",

            "datos": dict(
                id_cliente="CLI003",
                nombre="Ana Torres",
                email="ana.softwarefj.com",
                telefono="3002223344"
            ),

            "excepcion": EmailInvalidoError,
        },

        {
            "desc": "2c — Teléfono inválido",

            "datos": dict(
                id_cliente="CLI004",
                nombre="Carlos Ruiz",
                email="carlos@softwarefj.com",
                telefono="ABC123"
            ),

            "excepcion": TelefonoInvalidoError,
        },

        {
            "desc": "2d — ID duplicado",

            "datos": dict(
                id_cliente="CLI001",
                nombre="Laura Gómez",
                email="laura@softwarefj.com",
                telefono="3003334455"
            ),

            "excepcion": IDClienteInvalidoError,
        },
    ]

    for sub in sub_casos:

        try:

            Cliente(**sub["datos"])

            logger.error(
                "CASO %s — Debió rechazarse.",
                sub["desc"]
            )

            print(
                f"  [FALLO] "
                f"{sub['desc']} debió rechazarse."
            )

        except sub["excepcion"] as e:

            logger.warning(
                "CASO %s — %s",
                sub["desc"],
                e
            )

            print(
                f"  [OK - Rechazado] "
                f"{sub['desc']}"
            )

        except Exception as e:

            logger.error(
                "CASO %s — Error inesperado: %s",
                sub["desc"],
                e
            )

            print(
                f"  [ERROR INESPERADO] "
                f"{sub['desc']}"
            )

        finally:

            logger.debug(
                "Subcaso procesado: %s",
                sub["desc"]
            )

    print(
        "\n  [INFO] Caso cliente inválido finalizado.\n"
    )

# =====================================================
# PRUEBAS SERVICIOS
# =====================================================

def test_servicio_valido():
    """
    Caso válido de servicio.

    Demuestra:
    - herencia
    - polimorfismo
    - cálculo de costos
    """

    logger.info("─" * 55)
    logger.info("CASO 3 — Servicio válido")
    logger.info("─" * 55)

    print("─── CASO 3 — Servicio válido ───")

    try:

        servicio = ServicioSala(
            "Sala Premium",
            120000,
            30
        )

        total = servicio.calcular_costo(
            horas=5,
            descuento=0.10
        )

    except ServicioError as e:

        logger.error(
            "CASO 3 — Error inesperado: %s",
            e
        )

        print(f"  [ERROR] {e}")

    else:

        assert total > 0

        logger.info(
            "Servicio válido procesado."
        )

        print(
            f"  [OK] Servicio creado. "
            f"Total calculado: ${total}"
        )

    finally:

        print("  [INFO] Caso servicio válido finalizado.\n")


def test_servicio_invalido():
    """
    Caso inválido de servicio.

    Verifica validaciones robustas.
    """

    logger.info("─" * 55)
    logger.info("CASO 4 — Servicio inválido")
    logger.info("─" * 55)

    print("─── CASO 4 — Servicio inválido ───")

    try:

        ServicioEquipo(
            "",
            -500,
            ""
        )

    except ServicioError as e:

        logger.warning(
            "Servicio inválido detectado: %s",
            e
        )

        print(
            "  [OK - Rechazado] "
            "Servicio inválido detectado."
        )

    else:

        print(
            "  [FALLO] "
            "El servicio inválido debió rechazarse."
        )

    finally:

        print(
            "  [INFO] Caso servicio inválido finalizado.\n"
        )

# =====================================================
# PRUEBAS RESERVAS
# =====================================================

def test_reserva_valida():
    """
    Caso válido de reserva.

    Demuestra:
    - integración de módulos
    - confirmación
    - finalización
    - cálculo de costo
    """

    logger.info("─" * 55)
    logger.info("CASO 5 — Reserva válida")
    logger.info("─" * 55)

    print("─── CASO 5 — Reserva válida ───")

    try:

        cliente = Cliente(
            "CLI100",
            "Carlos Pérez",
            "carlos@correo.com",
            "3001112233"
        )

        servicio = ServicioAsesoria(
            "Asesoría Python",
            150000,
            "Ingeniero Senior"
        )

        reserva = Reserva(
            cliente,
            servicio,
            3
        )

        reserva.confirmar()

        total = reserva.calcular_total(0.05)

        reserva.finalizar()

    except (
        ClienteError,
        ServicioError,
        ReservaError
    ) as e:

        logger.error(
            "CASO 5 — Error inesperado: %s",
            e
        )

        print(f"  [ERROR] {e}")

    else:

        assert reserva.estado == "Finalizada"

        logger.info(
            "Reserva válida procesada."
        )

        print(
            f"  [OK] Reserva finalizada. "
            f"Total: ${total}"
        )

    finally:

        print(
            "  [INFO] Caso reserva válida finalizado.\n"
        )


def test_reserva_invalida():
    """
    Caso inválido de reserva.

    Verifica:
    - validaciones
    - manejo de excepciones
    - robustez del sistema
    """

    logger.info("─" * 55)
    logger.info("CASO 6 — Reserva inválida")
    logger.info("─" * 55)

    print("─── CASO 6 — Reserva inválida ───")

    try:

        servicio = ServicioSala(
            "Sala Básica",
            80000,
            15
        )

        Reserva(
            "cliente falso",
            servicio,
            -5
        )

    except ReservaError as e:

        logger.warning(
            "Reserva inválida detectada: %s",
            e
        )

        print(
            "  [OK - Rechazado] "
            "Reserva inválida detectada."
        )

    else:

        print(
            "  [FALLO] "
            "La reserva inválida debió rechazarse."
        )

    finally:

        print(
            "  [INFO] Caso reserva inválida finalizado.\n"
        )

# =====================================================
# EJECUCIÓN PRINCIPAL
# =====================================================

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("     SOFTWARE FJ — PRUEBAS DEL SISTEMA")
    print("=" * 60)

    # Limpieza para evitar conflictos
    Cliente.limpiar_registro_ids()

    # =================================================
    # EJECUCIÓN DE PRUEBAS
    # =================================================

    test_cliente_valido()
    test_cliente_invalido()

    test_servicio_valido()
    test_servicio_invalido()

    test_reserva_valida()
    test_reserva_invalida()

    print("=" * 60)
    print("Pruebas finalizadas.")
    print("Logs disponibles en: data/software_fj.log")
    print("=" * 60 + "\n")
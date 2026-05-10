# utils/logger.py

"""
Módulo de registro (logging) del sistema Software FJ.

Este módulo permite:
- Registrar eventos normales del sistema
- Registrar errores y excepciones
- Guardar información en archivos de texto
- Crear automáticamente la carpeta de logs

Se implementan buenas prácticas de:
- Manejo de archivos
- Manejo de excepciones
- Programación orientada a objetos
- Programación defensiva
"""

# =====================================================
# IMPORTACIONES
# =====================================================

import os
from datetime import datetime

from config.settings import RUTA_LOGS

# =====================================================
# CLASE LOGGER
# =====================================================

class Logger:
    """
    Clase encargada del registro de eventos
    y errores del sistema.

    Garantiza que:
    - La carpeta de logs exista
    - El sistema no falle al escribir logs
    - Los errores críticos sean controlados
    """

    # =================================================
    # CONSTRUCTOR
    # =================================================

    def __init__(self):
        """
        Constructor del logger.

        Crea automáticamente la carpeta
        donde se almacenarán los logs
        si esta no existe.
        """

        # Obtener carpeta desde la ruta
        directorio = os.path.dirname(RUTA_LOGS)

        # Crear carpeta solo si existe una ruta válida
        if directorio:
            os.makedirs(directorio, exist_ok=True)

    # =================================================
    # REGISTRO DE ERRORES
    # =================================================

    def registrar_error(self, mensaje, excepcion=None):
        """
        Registra errores del sistema.

        Args:
            mensaje (str):
                Descripción del error.

            excepcion (Exception, opcional):
                Excepción capturada.
        """

        try:

            with open(
                RUTA_LOGS,
                "a",
                encoding="utf-8"
            ) as archivo:

                fecha = datetime.now()

                archivo.write(
                    f"[ERROR] {fecha} - {mensaje}"
                )

                # Registrar excepción si existe
                if excepcion:
                    archivo.write(
                        f" - {str(excepcion)}"
                    )

                archivo.write("\n")

        except Exception as e:

            # Última línea de defensa:
            # evitar que el logger rompa el sistema
            print(
                "Error crítico al escribir en logs:",
                e
            )

    # =================================================
    # REGISTRO DE EVENTOS
    # =================================================

    def registrar_evento(self, mensaje):
        """
        Registra eventos normales del sistema.

        Args:
            mensaje (str):
                Evento o acción realizada.
        """

        try:

            with open(
                RUTA_LOGS,
                "a",
                encoding="utf-8"
            ) as archivo:

                fecha = datetime.now()

                archivo.write(
                    f"[INFO] {fecha} - {mensaje}\n"
                )

        except Exception as e:

            # Evita que un fallo del logger
            # detenga el sistema completo
            print(
                "Error crítico al escribir evento:",
                e
            )
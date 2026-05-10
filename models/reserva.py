"""
models/reserva.py

Módulo encargado de gestionar reservas
del sistema Software FJ.

Este módulo integra:
- Clientes
- Servicios
- Duración de reservas
- Estados de reserva

Se implementan principios de:
- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones

Además, se incluyen:
- Validaciones robustas
- Registro de eventos
- Registro de errores
- Encadenamiento de excepciones
- Uso de try/except/else/finally

Siguiendo criterios de calidad de software
(ISO 25000).
"""

# =====================================================
# IMPORTACIONES
# =====================================================

import logging
from datetime import datetime

from models.base import BaseEntidad
from models.cliente import Cliente
from models.servicio import Servicio

from exceptions.custom_exceptions import (
    ReservaError,
    ClienteError,
    ServicioError
)

# =====================================================
# CONFIGURACIÓN DEL LOGGER
# =====================================================

# Logger principal del sistema
logger = logging.getLogger("software_fj")

# =====================================================
# CLASE RESERVA
# =====================================================

class Reserva(BaseEntidad):
    """
    Clase que representa una reserva
    dentro del sistema Software FJ.

    Una reserva relaciona:
    - Un cliente
    - Un servicio
    - Una duración
    - Un estado

    Esta clase implementa:
    - Validaciones robustas
    - Manejo de excepciones
    - Procesos de confirmación
    - Cancelación
    - Finalización
    """

    # =================================================
    # ESTADOS VÁLIDOS DE RESERVA
    # =================================================

    ESTADOS_VALIDOS = (
        "Pendiente",
        "Confirmada",
        "Cancelada",
        "Finalizada"
    )

    # =================================================
    # CONTADOR AUTOMÁTICO DE RESERVAS
    # =================================================

    _contador_reservas = 1

    # =================================================
    # CONSTRUCTOR
    # =================================================

    def __init__(self, cliente, servicio, horas):
        """
        Constructor de la clase Reserva.

        Args:
            cliente (Cliente):
                Cliente asociado a la reserva.

            servicio (Servicio):
                Servicio solicitado.

            horas (int | float):
                Duración de la reserva.

        Raises:
            ReservaError:
                Si los datos son inválidos.
        """

        # Inicializa atributos heredados
        # desde BaseEntidad
        super().__init__()

        try:

            # =========================================
            # VALIDACIONES PRINCIPALES
            # =========================================

            self.validar_cliente(cliente)
            self.validar_servicio(servicio)
            self.validar_horas(horas)

            # =========================================
            # GENERACIÓN AUTOMÁTICA DEL ID
            # =========================================

            self._id_reserva = (
                f"RES-{Reserva._contador_reservas}"
            )

            Reserva._contador_reservas += 1

            # =========================================
            # ASIGNACIÓN DE ATRIBUTOS
            # =========================================

            self._cliente = cliente
            self._servicio = servicio
            self._horas = horas

            # Estado inicial de la reserva
            self._estado = "Pendiente"

            # Fecha de creación
            self._fecha_creacion = datetime.now()

            logger.info(
                "Reserva creada correctamente | ID: %s",
                self._id_reserva
            )

        except (
            ClienteError,
            ServicioError,
            ReservaError
        ) as error:

            logger.error(
                "Error al crear reserva: %s",
                error
            )

            # Encadenamiento de excepciones
            raise ReservaError(
                "No fue posible crear la reserva."
            ) from error

    # =================================================
    # VALIDACIONES
    # =================================================

    def validar_cliente(self, cliente):
        """
        Valida el cliente asociado.

        Args:
            cliente (Cliente)

        Raises:
            ReservaError:
                Si el cliente es inválido.
        """

        if not isinstance(cliente, Cliente):
            raise ReservaError(
                "El objeto cliente no es válido."
            )

    def validar_servicio(self, servicio):
        """
        Valida el servicio asociado.

        Args:
            servicio (Servicio)

        Raises:
            ReservaError:
                Si el servicio es inválido.
        """

        if not isinstance(servicio, Servicio):
            raise ReservaError(
                "El objeto servicio no es válido."
            )

    def validar_horas(self, horas):
        """
        Valida duración de la reserva.

        Args:
            horas (int | float)

        Raises:
            ReservaError:
                Si las horas son inválidas.
        """

        if not isinstance(horas, (int, float)):
            raise ReservaError(
                "Las horas deben ser numéricas."
            )

        if horas <= 0:
            raise ReservaError(
                "Las horas deben ser mayores que cero."
            )

        # Validación lógica empresarial
        if horas > 24:
            raise ReservaError(
                "No se permiten reservas "
                "mayores a 24 horas."
            )

    def validar_estado(self, estado):
        """
        Valida estados permitidos.

        Args:
            estado (str)

        Raises:
            ReservaError:
                Si el estado es inválido.
        """

        if estado not in self.ESTADOS_VALIDOS:
            raise ReservaError(
                f"Estado inválido: {estado}"
            )

    # =================================================
    # PROCESOS DE RESERVA
    # =================================================

    def confirmar(self):
        """
        Confirma la reserva.

        Raises:
            ReservaError:
                Si la reserva no puede confirmarse.
        """

        try:

            # =========================================
            # VALIDACIONES DE LÓGICA EMPRESARIAL
            # =========================================

            if self._estado == "Cancelada":
                raise ReservaError(
                    "No se puede confirmar "
                    "una reserva cancelada."
                )

            if self._estado == "Finalizada":
                raise ReservaError(
                    "La reserva ya fue finalizada."
                )

            # Cambio de estado
            self._estado = "Confirmada"

        except ReservaError as error:

            logger.error(
                "Error al confirmar reserva %s: %s",
                self._id_reserva,
                error
            )

            raise

        else:

            logger.info(
                "Reserva confirmada | ID: %s",
                self._id_reserva
            )

        finally:

            logger.info(
                "Proceso de confirmación ejecutado."
            )

    def cancelar(self):
        """
        Cancela una reserva activa.

        Raises:
            ReservaError:
                Si la reserva no puede cancelarse.
        """

        try:

            if self._estado == "Finalizada":
                raise ReservaError(
                    "No se puede cancelar "
                    "una reserva finalizada."
                )

            # Cambio de estado
            self._estado = "Cancelada"

        except ReservaError as error:

            logger.error(
                "Error al cancelar reserva %s: %s",
                self._id_reserva,
                error
            )

            raise

        else:

            logger.info(
                "Reserva cancelada | ID: %s",
                self._id_reserva
            )

        finally:

            logger.info(
                "Proceso de cancelación ejecutado."
            )

    def finalizar(self):
        """
        Finaliza una reserva.

        Raises:
            ReservaError:
                Si la reserva no puede finalizarse.
        """

        try:

            if self._estado != "Confirmada":
                raise ReservaError(
                    "Solo reservas confirmadas "
                    "pueden finalizarse."
                )

            # Cambio de estado
            self._estado = "Finalizada"

        except ReservaError as error:

            logger.error(
                "Error al finalizar reserva %s: %s",
                self._id_reserva,
                error
            )

            raise

        else:

            logger.info(
                "Reserva finalizada | ID: %s",
                self._id_reserva
            )

        finally:

            logger.info(
                "Proceso de finalización ejecutado."
            )

    # =================================================
    # CÁLCULO DE COSTOS
    # =================================================

    def calcular_total(self, descuento=0):
        """
        Calcula el costo total de la reserva.

        Args:
            descuento (float):
                Descuento opcional.

        Returns:
            float:
                Valor total calculado.

        Raises:
            ReservaError:
                Si ocurre un error de cálculo.
        """

        try:

            # =========================================
            # POLIMORFISMO
            # =========================================
            # Cada tipo de servicio implementa
            # su propia lógica de cálculo.
            # =========================================

            total = self._servicio.calcular_costo(
                self._horas,
                descuento
            )

            return total

        except Exception as error:

            logger.error(
                "Error calculando costo "
                "de reserva %s: %s",
                self._id_reserva,
                error
            )

            raise ReservaError(
                "Error calculando total de reserva."
            ) from error

    # =================================================
    # IMPLEMENTACIÓN DE BaseEntidad
    # =================================================

    def describir(self):
        """
        Retorna descripción completa
        de la reserva.
        """

        return (
            f"Reserva[{self._id_reserva}] | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.obtener_id()} | "
            f"Horas: {self._horas} | "
            f"Estado: {self._estado}"
        )

    def obtener_id(self):
        """
        Retorna ID único de la reserva.
        """

        return self._id_reserva

    # =================================================
    # REPRESENTACIÓN TÉCNICA
    # =================================================

    def __repr__(self):
        """
        Retorna representación técnica del objeto.
        """

        return (
            f"Reserva(id='{self._id_reserva}', "
            f"cliente='{self._cliente.nombre}', "
            f"estado='{self._estado}')"
        )

    # =================================================
    # PROPIEDADES
    # =================================================

    @property
    def cliente(self):
        """
        Retorna cliente asociado.
        """

        return self._cliente

    @property
    def servicio(self):
        """
        Retorna servicio asociado.
        """

        return self._servicio

    @property
    def horas(self):
        """
        Retorna duración de la reserva.
        """

        return self._horas

    @property
    def estado(self):
        """
        Retorna estado actual.
        """

        return self._estado

    @property
    def fecha_creacion(self):
        """
        Retorna fecha de creación.
        """

        return self._fecha_creacion
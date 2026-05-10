"""
models/servicio.py

Módulo de servicios del sistema Software FJ.

Este módulo implementa:

- Clase abstracta Servicio
- Servicios especializados:
    * ServicioSala
    * ServicioEquipo
    * ServicioAsesoria

Se aplican principios de:
- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo de excepciones

Además, se implementan validaciones robustas
siguiendo criterios de calidad de software
(ISO 25000).
"""

# =====================================================
# IMPORTACIONES
# =====================================================

from abc import abstractmethod

from models.base import BaseEntidad
from exceptions.custom_exceptions import ServicioError

# =====================================================
# CLASE ABSTRACTA SERVICIO
# =====================================================

class Servicio(BaseEntidad):
    """
    Clase abstracta que representa un servicio general
    del sistema.

    Esta clase define atributos y comportamientos comunes
    para todos los servicios especializados.
    """

    def __init__(self, nombre, costo_base):
        """
        Constructor de la clase Servicio.

        Args:
            nombre (str):
                Nombre del servicio.

            costo_base (float):
                Costo base del servicio por hora.

        Raises:
            ServicioError:
                Si los datos son inválidos.
        """

        # Inicializa atributos heredados
        # desde BaseEntidad
        super().__init__()

        # =============================================
        # ATRIBUTOS PRINCIPALES DEL SERVICIO
        # =============================================

        self._nombre = nombre
        self._costo_base = costo_base

        # Validación general de datos
        self.validar_datos()

    # =================================================
    # VALIDACIONES GENERALES
    # =================================================

    def validar_datos(self):
        """
        Realiza validaciones generales del servicio.

        Raises:
            ServicioError:
                Si algún dato es inválido.
        """

        # =============================================
        # VALIDACIÓN DEL NOMBRE
        # =============================================

        if not isinstance(self._nombre, str):
            raise ServicioError(
                "El nombre del servicio debe ser texto."
            )

        if not self._nombre.strip():
            raise ServicioError(
                "El nombre del servicio no puede estar vacío."
            )

        # =============================================
        # VALIDACIÓN DEL COSTO BASE
        # =============================================

        if not isinstance(self._costo_base, (int, float)):
            raise ServicioError(
                "El costo base debe ser numérico."
            )

        if self._costo_base <= 0:
            raise ServicioError(
                "El costo base debe ser mayor que cero."
            )

        # Validación lógica empresarial
        if self._costo_base > 10000000:
            raise ServicioError(
                "El costo base supera el límite permitido."
            )

    def validar_horas(self, horas):
        """
        Valida la cantidad de horas del servicio.

        Args:
            horas (int | float):
                Número de horas solicitadas.

        Raises:
            ServicioError:
                Si las horas son inválidas.
        """

        if not isinstance(horas, (int, float)):
            raise ServicioError(
                "Las horas deben ser numéricas."
            )

        if horas <= 0:
            raise ServicioError(
                "Las horas deben ser mayores que cero."
            )

        # Validación lógica empresarial
        if horas > 24:
            raise ServicioError(
                "No se permiten reservas mayores a 24 horas."
            )

    def validar_descuento(self, descuento):
        """
        Valida descuentos aplicados al servicio.

        Args:
            descuento (float):
                Porcentaje de descuento.

        Raises:
            ServicioError:
                Si el descuento es inválido.
        """

        if not isinstance(descuento, (int, float)):
            raise ServicioError(
                "El descuento debe ser numérico."
            )

        if descuento < 0:
            raise ServicioError(
                "El descuento no puede ser negativo."
            )

        if descuento > 0.50:
            raise ServicioError(
                "El descuento no puede superar el 50%."
            )

    # =================================================
    # MÉTODOS ABSTRACTOS
    # =================================================

    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        """
        Método abstracto para calcular
        el costo de un servicio.
        """
        pass

    @abstractmethod
    def descripcion(self):
        """
        Método abstracto para describir
        el servicio.
        """
        pass

    # =================================================
    # IMPLEMENTACIÓN DE BaseEntidad
    # =================================================

    def describir(self):
        """
        Retorna la descripción general
        del servicio.
        """

        return self.descripcion()

    def obtener_id(self):
        """
        Retorna el identificador del servicio.

        En este sistema, el nombre del servicio
        funciona como identificador principal.
        """

        return self._nombre

# =====================================================
# SERVICIO DE RESERVA DE SALAS
# =====================================================

class ServicioSala(Servicio):
    """
    Clase que representa el servicio
    de reserva de salas.
    """

    def __init__(self, nombre, costo_base, capacidad):
        """
        Constructor de ServicioSala.

        Args:
            nombre (str):
                Nombre del servicio.

            costo_base (float):
                Costo base por hora.

            capacidad (int):
                Número máximo de personas.
        """

        # Inicializa atributos heredados
        super().__init__(nombre, costo_base)

        # Atributo propio de la clase
        self._capacidad = capacidad

        # Validación especializada
        self.validar_capacidad()

    def validar_capacidad(self):
        """
        Valida la capacidad de la sala.
        """

        if not isinstance(self._capacidad, int):
            raise ServicioError(
                "La capacidad debe ser un número entero."
            )

        if self._capacidad <= 0:
            raise ServicioError(
                "La capacidad debe ser mayor que cero."
            )

        # Validación lógica empresarial
        if self._capacidad > 500:
            raise ServicioError(
                "La capacidad supera el límite permitido."
            )

    def calcular_costo(self, horas, descuento=0):
        """
        Calcula el costo del servicio de sala.
        """

        # Validaciones generales
        self.validar_horas(horas)
        self.validar_descuento(descuento)

        # Cálculo base
        total = self._costo_base * horas

        # Aplicación de descuento
        total -= total * descuento

        return total

    def descripcion(self):
        """
        Retorna descripción del servicio.
        """

        return (
            f"Servicio Sala | "
            f"Nombre: {self._nombre} | "
            f"Capacidad: {self._capacidad}"
        )

# =====================================================
# SERVICIO DE ALQUILER DE EQUIPOS
# =====================================================

class ServicioEquipo(Servicio):
    """
    Clase que representa alquiler de equipos.
    """

    def __init__(self, nombre, costo_base, tipo_equipo):
        """
        Constructor de ServicioEquipo.
        """

        # Inicializa atributos heredados
        super().__init__(nombre, costo_base)

        # Atributo propio
        self._tipo_equipo = tipo_equipo

        # Validación especializada
        self.validar_equipo()

    def validar_equipo(self):
        """
        Valida el tipo de equipo.
        """

        if not isinstance(self._tipo_equipo, str):
            raise ServicioError(
                "El tipo de equipo debe ser texto."
            )

        if not self._tipo_equipo.strip():
            raise ServicioError(
                "Debe especificarse un tipo de equipo."
            )

    def calcular_costo(self, horas, descuento=0):
        """
        Calcula el costo del alquiler del equipo.
        """

        # Validaciones generales
        self.validar_horas(horas)
        self.validar_descuento(descuento)

        # Cálculo base
        total = self._costo_base * horas

        # Impuesto adicional del 10%
        impuesto = total * 0.10

        total += impuesto

        # Aplicar descuento
        total -= total * descuento

        return total

    def descripcion(self):
        """
        Retorna descripción del servicio.
        """

        return (
            f"Servicio Equipo | "
            f"Nombre: {self._nombre} | "
            f"Equipo: {self._tipo_equipo}"
        )

# =====================================================
# SERVICIO DE ASESORÍAS
# =====================================================

class ServicioAsesoria(Servicio):
    """
    Clase que representa asesorías especializadas.
    """

    def __init__(self, nombre, costo_base, especialista):
        """
        Constructor de ServicioAsesoria.
        """

        # Inicializa atributos heredados
        super().__init__(nombre, costo_base)

        # Atributo propio
        self._especialista = especialista

        # Validación especializada
        self.validar_especialista()

    def validar_especialista(self):
        """
        Valida especialista asignado.
        """

        if not isinstance(self._especialista, str):
            raise ServicioError(
                "El especialista debe ser texto."
            )

        if not self._especialista.strip():
            raise ServicioError(
                "Debe asignarse un especialista."
            )

    def calcular_costo(self, horas, descuento=0):
        """
        Calcula el costo del servicio de asesoría.
        """

        # Validaciones generales
        self.validar_horas(horas)
        self.validar_descuento(descuento)

        # Cálculo base
        total = self._costo_base * horas

        # Recargo especial del 15%
        recargo = total * 0.15

        total += recargo

        # Aplicación de descuento
        total -= total * descuento

        return total

    def descripcion(self):
        """
        Retorna descripción del servicio.
        """

        return (
            f"Servicio Asesoría | "
            f"Nombre: {self._nombre} | "
            f"Especialista: {self._especialista}"
        )
"""
models/base.py

Clase abstracta base del sistema Software FJ.

Todas las entidades principales del sistema
deben heredar de esta clase:

- Cliente
- Servicio
- Reserva

Implementa:
- Abstracción
- Encapsulación
- Herencia

Además, obliga a las clases hijas
a implementar métodos esenciales.
"""

from abc import ABC, abstractmethod
import uuid

# =====================================================
# CLASE ABSTRACTA BASE
# =====================================================

class BaseEntidad(ABC):
    """
    Clase abstracta base para todas
    las entidades del sistema.

    Proporciona:
    - ID único automático
    - Métodos abstractos obligatorios
    """

    def __init__(self):
        """
        Constructor de la clase base.

        Genera automáticamente
        un identificador único.
        """

        self._id = str(uuid.uuid4())

    # =================================================
    # PROPIEDAD DE SOLO LECTURA
    # =================================================

    @property
    def id(self):
        """
        Retorna el ID único
        de la entidad.
        """

        return self._id

    # =================================================
    # MÉTODOS ABSTRACTOS OBLIGATORIOS
    # =================================================

    @abstractmethod
    def describir(self):
        """
        Retorna una descripción
        general de la entidad.
        """
        pass

    @abstractmethod
    def obtener_id(self):
        """
        Retorna el identificador
        lógico de la entidad.
        """
        pass
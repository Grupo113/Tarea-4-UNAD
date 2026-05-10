"""
exceptions/custom_exceptions.py

Módulo de excepciones personalizadas
del sistema Software FJ.
"""

# =====================================================
# EXCEPCIÓN BASE DEL SISTEMA
# =====================================================

class SistemaError(Exception):
    """
    Excepción principal del sistema.

    Todas las demás excepciones
    heredan de esta clase.
    """
    pass

# =====================================================
# EXCEPCIÓN GENERAL DE VALIDACIÓN
# =====================================================

class ValidacionError(SistemaError):
    """
    Error general para procesos
    de validación del sistema.
    """
    pass

# =====================================================
# EXCEPCIONES DE CLIENTE
# =====================================================

class ClienteError(SistemaError):
    """
    Errores relacionados con clientes.
    """
    pass


class NombreInvalidoError(ClienteError):
    """
    Error en nombres inválidos.
    """
    pass


class EmailInvalidoError(ClienteError):
    """
    Error en correos inválidos.
    """
    pass


class TelefonoInvalidoError(ClienteError):
    """
    Error en teléfonos inválidos.
    """
    pass


class IDClienteInvalidoError(ClienteError):
    """
    Error en IDs inválidos.
    """
    pass

# =====================================================
# EXCEPCIONES DE SERVICIOS
# =====================================================

class ServicioError(SistemaError):
    """
    Errores relacionados con servicios.
    """
    pass

# =====================================================
# EXCEPCIONES DE RESERVAS
# =====================================================

class ReservaError(SistemaError):
    """
    Errores relacionados con reservas.
    """
    pass
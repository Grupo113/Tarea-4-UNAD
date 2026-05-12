# SOFTWARE FJ

Sistema integral orientado a objetos desarrollado en Python para la gestión de:

- Clientes
- Servicios
- Reservas

El proyecto fue desarrollado siguiendo los principios de:

- Programación Orientada a Objetos (POO)
- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones

Además, el sistema implementa:

- Validaciones robustas
- Registro de eventos y errores
- Manejo de logs
- Persistencia mediante objetos y listas
- Simulación completa sin bases de datos

---

# DESCRIPCIÓN DEL SISTEMA

Software FJ es una aplicación que permite administrar reservas para una empresa que ofrece:

- Reservas de salas
- Alquiler de equipos
- Asesorías especializadas

El sistema fue diseñado para:

✔ Continuar funcionando aun cuando ocurran errores  
✔ Capturar excepciones de forma controlada  
✔ Registrar eventos importantes en archivos de logs  
✔ Mantener una arquitectura modular y extensible  

NO utiliza bases de datos.

Toda la información se maneja mediante:

- Objetos
- Listas
- Archivos de logs

---

# FUNCIONALIDADES PRINCIPALES

## Gestión de clientes

Permite:

- Registrar clientes
- Validar nombres
- Validar correos electrónicos
- Validar teléfonos
- Evitar IDs duplicados

---

## Gestión de servicios

Incluye:

### ServicioSala
- Reserva de salas
- Validación de capacidad
- Cálculo de costos

### ServicioEquipo
- Alquiler de equipos
- Impuestos automáticos
- Validación de equipos

### ServicioAsesoria
- Asesorías especializadas
- Recargos profesionales
- Validación de especialistas

---

## Gestión de reservas

Permite:

- Crear reservas
- Confirmar reservas
- Cancelar reservas
- Finalizar reservas
- Calcular costos
- Aplicar descuentos

---

## Manejo avanzado de excepciones

El sistema implementa:

- try / except
- try / except / else
- try / except / finally
- Encadenamiento de excepciones
- Excepciones personalizadas

---

# ESTRUCTURA DEL PROYECTO

```text
TAREA-4-UNAD/
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── data/
│   └── logs.txt
│
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py
│
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── cliente.py
│   ├── servicio.py
│   └── reserva.py
│
├── tests/
│   ├── __init__.py
│   └── test_sistema.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
├── main.py
└── README.md
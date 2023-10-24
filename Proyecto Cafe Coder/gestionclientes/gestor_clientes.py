from .cliente_minorista import ClienteMinorista
from .cliente_minorista_ventas import VentasClienteMinorista

# Funciones para trabajar con los clientes minoristas
def mostrar_informacion_cliente(cliente):
    print(f"Nombre: {cliente.nombre}")
    print(f"Ubicación: {cliente.ubicacion}")

# Funciones para trabajar con las ventas de clientes minoristas
def registrar_venta_cliente(cliente, producto, monto, registro_ventas):
    for registro in registro_ventas:
        if registro.cliente == cliente:
            registro.registrar_venta(producto, monto)
            return
    nuevo_registro = VentasClienteMinorista(cliente, [producto], monto)
    registro_ventas.append(nuevo_registro)
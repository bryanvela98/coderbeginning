from gestionclientes.cliente_minorista import ClienteMinorista
from gestionclientes.cliente_minorista_ventas import VentasClienteMinorista
from gestionclientes.gestor_clientes import *

from login import *

def main():
    # Crear instancias de la clase ClienteMinorista
    cliente_minorista = ClienteMinorista("NombreMinorista", "UbicacionMinorista", "FrecuenciaMinorista", "ComprasAnualesMinorista")
    
    # Mostrar información del cliente minorista
    print("Información de Cliente Minorista:")
    print(cliente_minorista)

    # Registrar ventas del cliente minorista
    registro_ventas = []
    registrar_venta_cliente(cliente_minorista, "Producto1", 100, registro_ventas)
    registrar_venta_cliente(cliente_minorista, "Producto2", 150, registro_ventas)

    # Mostrar datos de ventas
    for venta in registro_ventas:
        print(venta)

    # Registrar usuarios y probar la función de inicio de sesión
    registrar_usuario("usuario1", "Contraseña1")
    registrar_usuario("usuario2", "Contraseña2")

    # Iniciar sesión con usuarios registrados
    print("\nIntento de inicio de sesión:")
    print(iniciar_sesion("usuario1", "Contraseña1"))
    print(iniciar_sesion("usuario2", "ContraseñaIncorrecta"))

    # Mostrar datos almacenados
    mostrar_datos()

if __name__ == "__main__":
    main()
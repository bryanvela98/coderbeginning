class VentasClienteMinorista:
    def __init__(self, cliente, productos, total_ventas):
        self.cliente = cliente
        self.productos = productos
        self.total_ventas = total_ventas

    def registrar_venta(self, producto, monto):
        self.productos.append(producto)
        self.total_ventas += monto

    def __str__(self):
        return f"Ventas del cliente minorista {self.cliente.nombre}: {self.total_ventas} en total"
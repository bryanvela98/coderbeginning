class ClienteMinorista:
    def __init__(self, nombre, ubicacion, frecuencia_compra, compras_anuales):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.frecuencia_compra = frecuencia_compra
        self.compras_anuales = compras_anuales

    def __str__(self):
        return f"Cliente minorista: {self.nombre}, ubicado en {self.ubicacion}"
    
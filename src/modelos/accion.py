class Accion:
    def __init__(self, idAccion = None, cuit = None, simbolo = None, cantidadEnExistencia = None, precioActual = None):
        self.idAccion = idAccion
        self.cuit = cuit
        self.simbolo = simbolo
        self.cantidadEnExistencia = cantidadEnExistencia
        self.precioActual = precioActual

    def __str__(self):
        return (f"Accion ID: {self.idAccion}\n"
                f"Cuit: {self.cuit}\n"
                f"Simbolo: {self.simbolo}\n"
                f"Stock: {self.cantidadEnExistencia}\n"
                f"Precio actual: ${self.precioActual}")
class Portafolio:
    def __init__(self, idPortafolio = None, cuil = None, descripcion = None, fechaCreacion = None, saldoActual = None):
        self.idPortafolio = idPortafolio
        self.cuil = cuil
        self.descripcion = descripcion
        self.fechaCreacion = fechaCreacion
        self.saldoActual = saldoActual

    def __str__(self):
        return (f"Portafolio ID: {self.idPortafolio}\n"
                f"Cuil: {self.cuil}\n"
                f"Descripción: {self.descripcion}\n"
                f"Fecha de Creación: {self.fechaCreacion}\n"
                f"Saldo Actual: ${self.saldoActual}")
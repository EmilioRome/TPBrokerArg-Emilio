class PortafolioDTO:
    def __init__(self, Titular = None, saldoActual = None, totalInvertido = None, rendimientoActualTotal = None,
                accion = None, empresa = None, precioActual = None, cantidadEnExistencia = None, rendimientoActual = None):
        self.Titular = Titular
        self.saldoActual = saldoActual
        self.totalInvertido = totalInvertido
        self.rendimientoActualTotal = rendimientoActualTotal
        self.accion = accion
        self.empresa = empresa
        self.precioActual = precioActual
        self.cantidadEnExistencia = cantidadEnExistencia
        self.rendimientoActual = rendimientoActual

    def __str__(self):
        return (f"Titular: {self.Titular}\n"
                f"Saldo actual: {self.saldoActual}\n"
                f"Total invertido: {self.totalInvertido}\n"
                f"Rendimiento: {self.rendimientoActualTotal}\n")
        
    def mostrar_activos(self):
        return (f"Accion: {self.accion}\n"
                f"Empresa: {self.empresa}\n"
                f"En poseción: {self.cantidadEnExistencia}\n"
                f"Precio actual de mercado: {self.precioActual}\n"
                f"Rendimiento: {self.rendimientoActual}\n")
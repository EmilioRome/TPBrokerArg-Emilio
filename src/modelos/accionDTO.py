class AccionDTO:
    def __init__(self, idAccion = None, precio_actual = None, cantidad_en_existencia = None, mensaje = None, error = None):
        self.idAccion = idAccion
        self.precio_actual = precio_actual
        self.cantidad_en_existencia = cantidad_en_existencia
        self.mensaje = mensaje
        self.error = error
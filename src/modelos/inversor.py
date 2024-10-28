
class Inversor:
    def __init__(self, cuil = None, nombre = None, apellido = None, email = None, telefono = None, direccion = None, contraseña = None, bloqueado = None):
        self.cuil = cuil
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.contraseña = contraseña
        self.bloqueado = bloqueado

    def __str__(self):
        return (f"Inversor: {self.nombre} {self.apellido}\n"
                f"Cuil: {self.cuil}\n"
                f"Email: {self.email}\n"
                f"Teléfono: {self.telefono}\n"
                f"Dirección: {self.direccion}")
        
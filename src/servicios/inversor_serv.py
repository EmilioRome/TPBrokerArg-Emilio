from repositorio.inversorRepository import InversorRepository

class InversorService:
    inversorRepository = InversorRepository()

    def consultar_inversor (self, cuil):
        return self.inversorRepository.obtener_inversor(cuil)
    
    def consultar_inversor_email (self, email):
        return self.inversorRepository.obtener_inversor(email, es_cuil= False)

    def crear_inversor_serv (self, inversor_nuevo):
        return self.inversorRepository.crear_inversor(inversor_nuevo)
    
    def bloquear_contraseña (self, cuil_inversor, bloquear):
        return self.inversorRepository.bloquear_inversor(cuil_inversor, bloquear)
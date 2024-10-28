from repositorio.portafolioRepository import PortafolioRepository

class PortafolioService:
    portafolioRepository = PortafolioRepository()

    def consultar_portafolio (self, cuil):
        return self.portafolioRepository.obtener_portafolio(cuil)

    def crear_portafolio_serv (self, portafolio_nuevo):
        return self.portafolioRepository.crear_portafolio(portafolio_nuevo)
    
    def consultar_saldo_portafolio (self, idPortafolio):
        return self.portafolioRepository.saldo_portafolio(idPortafolio)
    
    def consultar_activos(self, idPortafolio):
        return self.portafolioRepository.activos_portafolio(idPortafolio)
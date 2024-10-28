from repositorio.accionRepository import AccionRepository
from modelos.accionDTO import AccionDTO
from modelos.portafolio import Portafolio

class AccionService:
    accionRepository = AccionRepository()

    def mostrar_acciones_disponibles(self):
        return self.accionRepository.obtener_acciones_disponibles()
    
    def comprar_accion(self, portafolioLogueado, idAccion, cantidad):
        accion = self.accionRepository.obtener_accion(idAccion)
        
        if accion.error == True:
            accion.mensaje = "La acción no existe."
            return accion
        
        if cantidad > accion.cantidad_en_existencia:
            accion.mensaje = "Cantidad solicitada excede la cantidad disponible."
            return accion
        
        costo_total = accion.precio_actual * cantidad
        
        if portafolioLogueado.saldoActual < costo_total:
            accion.mensaje = "Saldo insuficiente."
            return accion
        
        accion = self.accionRepository.realizar_compra(portafolioLogueado, accion, costo_total, cantidad)
        return accion
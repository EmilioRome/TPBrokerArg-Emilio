from servicios.inversor_serv import InversorService
from servicios.portafolio_serv import PortafolioService
from servicios.accion_serv import AccionService
from modelos.inversor import Inversor
from modelos.portafolio import Portafolio

def menu():
    print("1. Ingresar")
    print("2. Registrarse")
    print("3. Recuperar cuenta")
    print("4. Salir")
    
def menu_logueado(inversorLogueado, portafolioLogueado, servicePort, serviceAccion):
    while True:
        print("1. Consultar saldo")
        print("2. Consultar activos")
        print("3. Acciones en mercado")
        print("4. Comprar acciones")
        print("5. Cerrar sesión")
        opcion = input("Selecciona una opción: ")
        print()

        if opcion == "1":
            saldo_portafolio = servicePort.consultar_saldo_portafolio(portafolioLogueado.idPortafolio)
            print(saldo_portafolio)
        
        elif opcion == "2":
            activos_portafolio = servicePort.consultar_activos(portafolioLogueado.idPortafolio)
            if activos_portafolio:
                for activo in activos_portafolio:
                    print(activo.mostrar_activos())
            else:    
                print("No se encontraron activos en el portafolio\n")

        elif opcion == "3":
            acciones = serviceAccion.mostrar_acciones_disponibles()
            
            if acciones:
                print("Acciones disponibles en el mercado:")
                for accion in acciones:
                    print(f"ID: {accion['idAccion']}, Símbolo: {accion['simbolo']}, Precio Actual: ${accion['precio_actual']}, Cantidad en Existencia: {accion['cantidad_en_existencia']}")
            else:
                print("No hay acciones disponibles en el mercado.")
                
        elif opcion == "4":
            id_accion = input("Ingrese el ID de la accion a comprar: ")
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            accionAux = serviceAccion.comprar_accion(portafolioLogueado, id_accion, cantidad)
        
            print(accionAux.mensaje)
            print()
                
        elif opcion == "5":
            print("Cerrando sesión...\n")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

def login(inversorAux):
    intentos = 3
    while intentos > 0:
        contraseña = input("Ingrese su contraseña: ")
        print()
        
        if inversorAux.contraseña == contraseña:
            return inversorAux
        else:
            intentos -= 1
            print(f"Datos incorrectos. Le quedan {intentos} intentos.")
    
    return None

def main():
    inversor_service = InversorService()
    portafolio_service = PortafolioService()
    accion_service = AccionService()

    while True:
        inversorAux = Inversor()
        menu()
        choice = input("Selecciona una opción: ")
        print()

        if choice == "1":
            inversorAux.cuil = input("Ingrese su cuil: ")
            inversorAux = inversor_service.consultar_inversor(inversorAux.cuil)

            if inversorAux == None:
                print("Inversor no encontrado.")
                
            elif inversorAux.bloqueado == 1: 
                print("Cuenta bloqueada, por favor recupere su contraseña para desbloquear")
            else:
                cuil_inversor = inversorAux.cuil
                inversorAux= login(inversorAux)
                
                if inversorAux:
                    print(f"Bienvenido/a {inversorAux.nombre} {inversorAux.apellido}\n")
                    
                    portafolioAux = portafolio_service.consultar_portafolio(inversorAux.cuil)
                    menu_logueado(inversorAux, portafolioAux, portafolio_service, accion_service)
                    
                else:
                    inversor_service.bloquear_contraseña(cuil_inversor, True)
                    print("Cuenta bloqueada. Por favor recupere su contraseña para desbloquear.")

        elif choice == "2":
            inversor_nuevo = Inversor()

            inversor_nuevo.cuil = input("Ingrese su cuil: ")
            inversor_nuevo.nombre = input("Ingrese su nombre: ")
            inversor_nuevo.apellido = input("Ingrese su apellido: ")
            inversor_nuevo.email = input("Ingrese su email: ")
            inversor_nuevo.telefono = input("Ingrese su telefono: ")
            inversor_nuevo.direccion = input("Ingrese su direccion: ")
            inversor_nuevo.contraseña = input("Ingrese su contraseña: ")

            creado = inversor_service.crear_inversor_serv(inversor_nuevo)

            if creado:
                print("Se creo al nuevo inversor")

                portafolio_nuevo = Portafolio()
                portafolio_nuevo.descripcion = input("Ingrese una descripcion para su portafolio: ")
                portafolio_nuevo.cuil = inversor_nuevo.cuil

                portafolio_creado = portafolio_service.crear_portafolio_serv(portafolio_nuevo)

                if portafolio_creado:
                    print("Se creo su portafolio")
                else:
                    print("Error al crear el portafolio")

            else:
                print("no se pudo crearlo")

        elif choice == "3":
            inversorAux = Inversor()
            
            inversorAux.email = input("Ingrese su correo: ")
            inversorAux = inversor_service.consultar_inversor_email(inversorAux.email)
            
            if inversorAux == None:
                print("Inversor no encontrado.")
            else:
                print(f"Se envio un correo a {inversorAux.email} Codigo recupero: 123.")
                
                while True:
                    codigo = input("Ingrese el código de recuperación: ")
                    if codigo == "123":                       
                        print(f"Codigo correcto. Tu contraseña es {inversorAux.contraseña}.")
                        if inversorAux.bloqueado == 1:
                            inversor_service.bloquear_contraseña(inversorAux.cuil, False)
                            print("Cuenta desbloqueada.")
                        break
                    else:
                        print("Código incorrecto. Intente nuevamente.")
            
        elif choice == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

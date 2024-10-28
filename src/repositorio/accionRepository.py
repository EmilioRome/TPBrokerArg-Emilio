from repositorio.database import DatabaseConnection
from modelos.accionDTO import AccionDTO

class AccionRepository:
    def obtener_acciones_disponibles(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = """
        SELECT idAccion, simbolo, precio_actual, cantidad_en_existencia 
        FROM acciones 
        WHERE cantidad_en_existencia > 0
        """

        try:
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            acciones_disponibles = [
                {"idAccion": row[0], "simbolo": row[1], "precio_actual": row[2], "cantidad_en_existencia": row[3]}
                for row in resultados
            ]
            return acciones_disponibles

        except Exception as e:
            print(f"Error al obtener acciones disponibles: {e}")
            return []

        finally:
            cursor.close()
            connection.close()
            
    def obtener_accion(self, accionID):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = "SELECT precio_actual, cantidad_en_existencia FROM acciones WHERE idAccion = %s"
        
        try:
            cursor.execute(query, (accionID,))
            resultado = cursor.fetchone()

            if resultado:
                return AccionDTO(
                    precio_actual=resultado[0],
                    cantidad_en_existencia=resultado[1],
                    idAccion= accionID,
                    error=False
                )
            return AccionDTO(
                error = True
            )

        except Exception as e:
            print(f"Error al obtener el portafolio: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
            
    def realizar_compra(self, portafolioLogueado, accionDTO, costo_total, cantidad):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        
        try:
            actualizar_saldo = "UPDATE portafolios SET saldo_actual = saldo_actual - %s WHERE idPortafolio = %s"
            cursor.execute(actualizar_saldo, (costo_total, portafolioLogueado.idPortafolio))
            
            actualizar_cantidad = "UPDATE acciones SET cantidad_en_existencia = cantidad_en_existencia - %s WHERE idAccion = %s"
            cursor.execute(actualizar_cantidad, (cantidad, accionDTO.idAccion))
            
            registrar_operacion = """
            INSERT INTO detalleOperaciones (idPortafolio, idAccion, cantidad, tipo_operacion, comision, valor_accion)
            SELECT %s, %s, %s, 'Compra', ROUND(20 * %s * 0.015), %s
            FROM Acciones
            WHERE idAccion = %s;
            """
            cursor.execute(registrar_operacion, (portafolioLogueado.idPortafolio, accionDTO.idAccion, cantidad, accionDTO.precio_actual,
                                                accionDTO.precio_actual, accionDTO.idAccion))
            
            connection.commit()
            accionDTO.mensaje ="Compra realizada con éxito."
            accionDTO.error = False
            return accionDTO

        except Exception as e:
            print(f"Error al realizar la compra: {e}")
            connection.rollback()
            return False

        finally:
            cursor.close()
            connection.close()
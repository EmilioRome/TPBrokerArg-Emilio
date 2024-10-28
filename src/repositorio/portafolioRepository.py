from repositorio.database import DatabaseConnection
from modelos.portafolio import Portafolio
from modelos.portafolioDTO import PortafolioDTO

class PortafolioRepository:
    def crear_portafolio(self, nuevo_portafolio):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = """
            INSERT INTO portafolios (cuil, descripcion, saldo_actual) 
            VALUES (%s, %s, 1000000)
        """

        try:
            cursor.execute(query, (
                nuevo_portafolio.cuil, nuevo_portafolio.descripcion
            ))
            connection.commit()
            return True

        except Exception as e:
            print(f"Error al crear el portafolio: {e}")
            connection.rollback()
            return False

        finally:
            cursor.close()
            connection.close()
            
    def obtener_portafolio (self, cuil):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = "SELECT * FROM portafolios WHERE cuil = %s"
        
        try:
            cursor.execute(query, (cuil,))
            resultado = cursor.fetchone()

            if resultado:
                return Portafolio(
                    idPortafolio=resultado[0],
                    cuil=resultado[1],
                    descripcion=resultado[2],
                    fechaCreacion=resultado[3],
                    saldoActual=resultado[4]
                )
            return None

        except Exception as e:
            print(f"Error al obtener el portafolio: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
            
    def saldo_portafolio (self, id_buscar):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = """
        SELECT 
            i.nombre AS Titular,
            p.saldo_actual AS SaldoActual,
            SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN d.cantidad * d.valor_accion ELSE 0 END) AS TotalInvertido,
            SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN (d.valor_accion * d.cantidad) ELSE 0 END) 
            - SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN d.cantidad * d.valor_accion ELSE 0 END) 
            + (SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN (d.cantidad * a.precio_actual) ELSE 0 END)
                - SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN (d.cantidad * a.precio_actual) ELSE 0 END))
            AS RendimientoActualTotal
        FROM portafolios p
        LEFT JOIN detalleOperaciones d ON p.IdPortafolio = d.idPortafolio
        LEFT JOIN acciones a ON d.idAccion = a.idAccion
        LEFT JOIN inversores i ON p.cuil = i.cuil
        WHERE p.IdPortafolio = %s
        GROUP BY p.descripcion, p.saldo_actual;
        """
        
        try:
            cursor.execute(query, (id_buscar,))
            resultado = cursor.fetchone()

            if resultado:
                return PortafolioDTO(
                    Titular=resultado[0],
                    saldoActual=resultado[1],
                    totalInvertido=resultado[2],
                    rendimientoActualTotal=resultado[3]
                )
            return None

        except Exception as e:
            print(f"Error al obtener el portafolio: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
            
    def activos_portafolio (self, id_buscar):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = """
        SELECT 
            a.simbolo AS Accion,
            e.nombre AS Empresa,
            a.precio_actual AS PrecioActual,
            SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN d.cantidad ELSE 0 END) - 
            SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN d.cantidad ELSE 0 END) AS CantidadEnExistencia,
            SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN (d.valor_accion * d.cantidad) ELSE 0 END) 
	            - SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN d.cantidad * d.valor_accion ELSE 0 END) 
                + (SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN (d.cantidad * a.precio_actual) ELSE 0 END)
			    -SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN (d.cantidad * a.precio_actual) ELSE 0 END))
                AS RendimientoActual
            FROM inversores i
            JOIN portafolios p ON i.cuil = p.cuil
            JOIN detalleOperaciones d ON p.IdPortafolio = d.idPortafolio
            JOIN acciones a ON d.idAccion = a.idAccion
            JOIN empresas e ON a.Cuit = e.Cuit
            WHERE p.IdPortafolio = %s
            GROUP BY a.simbolo, e.nombre, a.precio_actual
            HAVING CantidadEnExistencia > 0;
        """
        
        try:
            cursor.execute(query, (id_buscar,))
            resultados = cursor.fetchall()

            if resultados:
                activos = [
                    PortafolioDTO(
                        accion=row[0],
                        empresa=row[1],
                        precioActual=row[2],
                        cantidadEnExistencia=row[3],
                        rendimientoActual=row[4]
                    ) for row in resultados
                ]
                return activos
            else:
                return None

        except Exception as e:
            print(f"Error al obtener el portafolio: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
from repositorio.database import DatabaseConnection
from modelos.inversor import Inversor

class InversorRepository:
    def obtener_inversor(self, identificador, es_cuil=True):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        if es_cuil:
            query = "SELECT * FROM inversores WHERE cuil = %s"
        else:
            query = "SELECT * FROM inversores WHERE email = %s"
        
        try:
            cursor.execute(query, (identificador,))
            resultado = cursor.fetchone()

            if resultado:
                return Inversor(
                    cuil=resultado[0],
                    nombre=resultado[1],
                    apellido=resultado[2],
                    email=resultado[3],
                    telefono=resultado[4],
                    direccion=resultado[5],
                    contraseña=resultado[6],
                    bloqueado=resultado[7]
                )
            return None

        except Exception as e:
            print(f"Error al obtener el inversor: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

    def crear_inversor(self, nuevo_inversor):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = """
            INSERT INTO inversores (cuil, nombre, apellido, email, telefono, direccion, contraseña) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(query, (
                nuevo_inversor.cuil, nuevo_inversor.nombre, nuevo_inversor.apellido,
                nuevo_inversor.email, nuevo_inversor.telefono, nuevo_inversor.direccion, nuevo_inversor.contraseña
            ))
            connection.commit()
            return True

        except Exception as e:
            print(f"Error al crear el inversor: {e}")
            connection.rollback()
            return False

        finally:
            cursor.close()
            connection.close()
            
    def bloquear_inversor(self, cuil, bloquear):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = "UPDATE inversores SET bloqueado = %s WHERE cuil = %s"

        try:
            if bloquear:
                cursor.execute(query, (1, cuil))
            else:
                cursor.execute(query, (0, cuil))
                
            connection.commit()
            return True

        except Exception as e:
            print(f"Error al bloquear el inversor: {e}")
            connection.rollback()
            return False

        finally:
            cursor.close()
            connection.close()

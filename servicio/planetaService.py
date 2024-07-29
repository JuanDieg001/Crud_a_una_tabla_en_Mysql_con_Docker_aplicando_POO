from abc import ABC, abstractmethod
from accessData.conexion import Conexion
from dominio.dominio import Planeta

class BaseDatos:

    #Create
    @abstractmethod
    def crear (self,datos):
        pass

    #Read
    @abstractmethod
    def leer (self,nombre):
        pass

    #Update
    @abstractmethod
    def actualizar (self, id, datos):
        pass

    #Delete
    @abstractmethod
    def borrar (self, id):
        pass


class PlanetaService(BaseDatos):
    
    def __init__(self):
        pass
    
    def crear(self, datos):#modulo para crear planetas

        self.connection = Conexion.obtener_conexion()
        self.cursor = self.connection.cursor()
        
        try:
            sql = "INSERT INTO planeta (nombre, tipo, radio, distancia_sol) VALUES (%s, %s, %s, %s)"
            valores = (datos.nombre, datos.tipo, datos.radio, datos.distanciaSol)
            #ejecuta consulta SQL a través de el objeto cursor
            self.cursor.execute(sql, valores)
            #confirmar la transacción
            self.connection.commit()
            print("Planeta creado exitosamente.")

        except Exception as error:
            print("Error al insertar:", error)
            # Deshacer la transacción en caso de error
            self.connection.rollback()
        
        finally:
            #cierra el cursor, liberando así los recursos asociados a ese cursor.
            self.cursor.close()
            self.connection.close()
    
    def leer(self, nombre=None):
        
        self.connection = Conexion.obtener_conexion()
        self.cursor = self.connection.cursor()
        
        try:
            sql = "SELECT * FROM planeta"
            if nombre:
                sql += " WHERE nombre = %s"
                self.cursor.execute(sql, (nombre,))
            else:
                self.cursor.execute(sql)

            lista = []
            for (id, nombre, tipo, radio, distanciaSol) in self.cursor:
                lista.append(Planeta(id, nombre, tipo, radio, distanciaSol))
            return lista
        
        except Exception as err:
            print("Error en la ejecución de la consulta:", err)
            self.connection.rollback()
        
        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar(self, id, datos):
        try:
            self.connection = Conexion.obtener_conexion()
            self.cursor = self.connection.cursor()
            sql = "UPDATE planeta SET nombre=%s, tipo=%s, radio=%s, distancia_sol=%s WHERE id=%s"
            valores = (datos.nombre, datos.tipo, datos.radio, datos.distanciaSol, id)
            self.cursor.execute(sql, valores)
            self.connection.commit()
            print("Planeta actualizado exitosamente.")
        except Exception as err:
            print("Error en la actualizacion:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()

    def borrar(self, id):
        try:
            self.connection = Conexion.obtener_conexion()
            self.cursor = self.connection.cursor()
            sql = "DELETE FROM planeta WHERE id=%s"
            self.cursor.execute(sql, (id,))
            self.connection.commit()
            print("Planeta eliminado")
        except Exception as err:
            print("Error en la eliminación:", err)
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.connection.close()

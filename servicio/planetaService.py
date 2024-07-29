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
    def actualizar (self, nombre, datos):
        pass

    #Delete
    @abstractmethod
    def borrar (self, nombre):
        pass


class PlanetaService(BaseDatos):
    
    def __init__(self):
        pass
    
    def crear(self, datos):

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

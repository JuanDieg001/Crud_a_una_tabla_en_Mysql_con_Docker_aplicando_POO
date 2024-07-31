# Importa las clases ABC y abstractmethod del módulo abc
# ABC se usa para definir clases abstractas que no pueden ser instanciadas directamente.
# abstractmethod se usa para definir métodos que deben ser implementados por las subclases
from abc import ABC, abstractmethod

# Importa la clase Conexion desde el módulo accessData.conexion
# accessData es un paquete y conexion es un módulo dentro de él
# La clase Conexion se usa para manejar la conexión a la base de datos.
from accessData.conexion import Conexion

# Importa la clase Planeta desde el módulo dominio.dominio
# dominio es un paquete y dominio es un módulo dentro de él
# La clase Planeta se usa para representar planetas con atributos como id, nombre, tipo, radio y distancia al sol.
from dominio.dominio import Planeta

from servicio.logService import LogService


class BaseDatos:# clase abstracata que se usa como plantilla para crear otras clases que requieran los mismo metodos

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


class PlanetaService(BaseDatos):#clase que usa los metodos de la clase abstracata y los adapta a su necesidad

    
    def __init__(self): #metodo constructor de la clase PlanetaSservice que inicializa con valores None
        # Inicializa los atributos de la clase
        # 'connection' y 'cursor' se inicializan en None
        self.connection = None
        self.cursor = None
        # Inicializa el atributo 'registro' con una nueva instancia de LogService
        self.registro = LogService()
    
    def crear(self, datos):#modulo para crear planetas en la BdD

        # Llama al método 'logger' del objeto 'registro'
        self.registro.logger("se crea el planeta: "+str(datos.nombre))

        # Obtiene una conexión a la base de datos mediante el método 'obtener_conexion' de la clase 'Conexion'.
        self.connection = Conexion.obtener_conexion()

        # Crea un cursor a partir de la conexión obtenida. El cursor se usa para ejecutar comandos SQL y manipular la base de datos.
        self.cursor = self.connection.cursor()
        
        try:
            # Define una sentencia SQL para insertar un nuevo registro en la tabla 'planeta'
            # Los valores a insertar se representan con marcadores de posición (%s)
            sql = "INSERT INTO planeta (nombre, tipo, radio, distancia_sol) VALUES (%s, %s, %s, %s)"

            # Crea una tupla 'valores' que contiene los datos a insertar en la tabla 'planeta'
            # Los valores se extraen de las propiedades del objeto 'datos'.
            valores = (datos.nombre, datos.tipo, datos.radio, datos.distanciaSol)
            
            # Ejecuta la sentencia SQL utilizando el cursor
            # Los marcadores de posición en la sentencia SQL se reemplazan por los valores de la tupla 'valores'.
            self.cursor.execute(sql, valores)
           
            # Confirma la transacción, haciendo permanentes los cambios realizados en la base de datos.
            self.connection.commit()
            print("Planeta creado exitosamente.")

        except Exception as error:
            print("Error al insertar:", error)
            # Deshacer la transacción en caso de error
            self.connection.rollback()
        
        finally:
            #cierra el cursor, liberando así los recursos asociados a ese cursor.
            self.cursor.close()

            # Cierra la conexión a la base de datos para liberar los recursos y evitar posibles fugas de conexión
            self.connection.close()
    
    def leer(self, nombre=None):#modulo para leer planetas en la BdD
        
        
        
        # Llama al método 'logger' del objeto 'registro'
        self.registro.logger("se ingreso al metodo leer: "+str(nombre))

        # Obtiene una conexión a la base de datos mediante el método 'obtener_conexion' de la clase 'Conexion'.
        self.connection = Conexion.obtener_conexion()

        # Crea un cursor a partir de la conexión obtenida. El cursor se usa para ejecutar comandos SQL y manipular la base de datos.
        self.cursor = self.connection.cursor()

        try:
        
            # Define la consulta SQL básica que selecciona todas las columnas de la tabla 'planeta'
            sql = "SELECT * FROM planeta"

            # Verifica si se ha proporcionado un nombre para filtrar los resultados
            if nombre:
                # Si 'nombre' no es None o una cadena vacía, agrega una cláusula WHERE a la consulta SQL
                sql += " WHERE nombre = %s"

                # Ejecuta la consulta SQL con el nombre proporcionado como parámetro
                self.cursor.execute(sql, (nombre,))

            else:
                # Si 'nombre' no se proporciona, ejecuta la consulta SQL sin ninguna cláusula WHERE
                self.cursor.execute(sql)

            # Inicializa una lista vacía para almacenar los objetos 'Planeta'
            lista = []

            # Recorre todos los resultados devueltos por la consulta SQL
            for (id, nombre, tipo, radio, distanciaSol) in self.cursor:
                # Crea una instancia del objeto 'Planeta' para cada fila de resultados
                lista.append(Planeta(id, nombre, tipo, radio, distanciaSol))

            # Devuelve la lista de objetos 'Planeta'    
            return lista
        
        except Exception as err:
            print("Error en la ejecución de la consulta:", err)
            # Deshacer la transacción en caso de error
            self.connection.rollback()
        
        finally:
             #cierra el cursor, liberando así los recursos asociados a ese cursor.
            self.cursor.close()

            # Cierra la conexión a la base de datos para liberar los recursos y evitar posibles fugas de conexión
            self.connection.close()

    def actualizar(self, id, datos):#metodo para actualizar planetas en la BdD
        
        # Llama al método 'logger' del objeto 'registro'
        self.registro.logger("se actualizo el planeta: "+str(datos.nombre))

        # Obtiene una conexión a la base de datos mediante el método 'obtener_conexion' de la clase 'Conexion'.
        self.connection = Conexion.obtener_conexion()

        # Crea un cursor a partir de la conexión obtenida. El cursor se usa para ejecutar comandos SQL y manipular la base de datos.
        self.cursor = self.connection.cursor()

        try:
            # Define una consulta SQL para actualizar un registro en la tabla 'planeta'.
            # Se establecen nuevos valores para las columnas 'nombre', 'tipo', 'radio' y 'distancia_sol'
            # en el registro que coincida con el 'id' proporcionado.
            sql = "UPDATE planeta SET nombre=%s, tipo=%s, radio=%s, distancia_sol=%s WHERE id=%s"

            # Prepara una tupla con los valores que se usarán para actualizar el registro.
            # Los valores se corresponden con los nuevos datos para 'nombre', 'tipo', 'radio' y 'distancia_sol',
            # y el 'id' del registro que se debe actualizar.
            valores = (datos.nombre, datos.tipo, datos.radio, datos.distanciaSol, id)
            
            # Ejecuta la consulta SQL utilizando los valores proporcionados.
            # La consulta se parametriza para evitar inyecciones SQL.
            self.cursor.execute(sql, valores)

            # Confirma los cambios realizados en la base de datos.
            self.connection.commit()
            print("Planeta actualizado exitosamente.")

        except Exception as err:
            print("Error en la actualizacion:", err)
            # Deshacer la transacción en caso de error
            self.connection.rollback()

        finally:
            #cierra el cursor, liberando así los recursos asociados a ese cursor.
            self.cursor.close()
            # Cierra la conexión a la base de datos para liberar los recursos y evitar posibles fugas de conexión
            self.connection.close()

    def borrar(self, id):#metodo para borrar planetas en la BdD
        
         # Llama al método 'logger' del objeto 'registro'
        self.registro.logger("se elimino el planeta con el id: "+str(id))
        
        # Obtiene una conexión a la base de datos mediante el método 'obtener_conexion' de la clase 'Conexion'.
        self.connection = Conexion.obtener_conexion()

        # Crea un cursor a partir de la conexión obtenida. El cursor se usa para ejecutar comandos SQL y manipular la base de datos.
        self.cursor = self.connection.cursor()

        try:
            # Define una consulta SQL para eliminar un registro de la tabla 'planeta'.
            # El registro a eliminar es el que coincide con el 'id' proporcionado.
            sql = "DELETE FROM planeta WHERE id=%s"

            # Ejecuta la consulta SQL utilizando el 'id' como parámetro.
            # Esto elimina el registro con el 'id' especificado.
            self.cursor.execute(sql, (id,))

            # Confirma los cambios realizados en la base de datos.
            self.connection.commit()
            print("Planeta eliminado")

        except Exception as err:
            print("Error en la eliminación:", err)
            # Deshacer la transacción en caso de error
            self.connection.rollback()
            
        finally:
            #cierra el cursor, liberando así los recursos asociados a ese cursor.
            self.cursor.close()
            # Cierra la conexión a la base de datos para liberar los recursos y evitar posibles fugas de conexión
            self.connection.close()

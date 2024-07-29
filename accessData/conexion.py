import mysql.connector #mporta el módulo necesario para conectar y manejar la base de datos MySQL.


# Define la clase Conexion
class Conexion:

    # Método estático para obtener una conexión a la base de datos
    @staticmethod
    def obtener_conexion():
        try:
            # Intenta establecer la conexión a la base de datos usando los parámetros proporcionados
            conexion = mysql.connector.connect(
                host="localhost",          # Dirección del servidor de base de datos
                user="root",               # Nombre de usuario para la conexión
                password="admin",          # Contraseña del usuario
                database="sistema_solar",  # Nombre de la base de datos a la que conectar
                port="3307"                # Puerto en el que el servidor de base de datos está escuchando
            )
            # Si la conexión es exitosa, imprime un mensaje de éxito
            print("Conexión correcta :D ")
            # Devuelve la conexión establecida
            return conexion
        except mysql.connector.Error as error:
            # Si ocurre un error al intentar conectarse, imprime el mensaje de error
            print(f"Error al conectarse en la base de datos: {error}")
            # Devuelve None en caso de error
            return None

    
    # Llamada al método para verificar la conexión
    #obtener_conexion()
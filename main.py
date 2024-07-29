# Importa la clase Planeta desde el módulo dominio.dominio
# De la estructura de directorios donde 'dominio' es un paquete 
# y dentro de ese paquete hay un archivo llamado 'dominio.py' que define la clase Planeta.
from dominio.dominio import Planeta

# Importa la clase PlanetaService desde el módulo servicio.planetaService
# ADe la estructura de directorios donde 'servicio' es otro paquete
# y dentro de ese paquete hay un archivo llamado 'planetaService.py' que define la clase PlanetaService
from servicio.planetaService import PlanetaService

def main():

    planeta_service = PlanetaService()  # Crear una instancia de PlanetaService    

    while True: #bucle while que se va a ejecutar porque tiene True
        print("""
               --- MENU ---
               1. Crear planeta
               2. Consultar planetas
               3. Actualizar planeta
               4. Eliminar planeta
               5. Salir
        """)

        opcion = int(input("Seleccione una opción: ")) #asigna un valor a la variable opcion para que se pueda usar en el matcha case
        match opcion: #match case de python

            case 1:# se ingresan los valores a la variables
                nombre = input("Ingrese el nombre del planeta: ")
                tipo = input("Ingrese el tipo de planeta (Rocoso, Gaseoso, etc.): ")
                radio = float(input("Ingrese el radio del planeta: "))
                distancia_Sol = float(input("Ingrese la distancia al sol del planeta: "))

                #se pasan los valores con las variables de arriba
                instancia_planeta = Planeta(None, nombre, tipo, radio, distancia_Sol)
                planeta_service.crear(instancia_planeta)
            
            case 2:
                nombre = input("Ingrese el nombre del planeta que desea consultar (deje vacío para consultar todos): ")
                if nombre.strip() == "":
                    planetas = planeta_service.leer()
                else:
                    planetas = planeta_service.leer(nombre)
                for planeta in planetas:
                    print(vars(planeta))

            case 3:
                id = int(input("Ingrese el id del planeta que desea actualizar: "))
                nombre = input("Ingrese el nuevo nombre del planeta: ")
                tipo = input("Ingrese el  nuevo tipo de planeta (Rocoso, Gaseoso, etc.): ")
                radio = float(input("Ingrese el nuevo radio del planeta: "))
                distancia_Sol = float(input("Ingrese la  nueva distancia al sol del planeta: "))

                #se pasan los valores con las variables de arriba
                instancia_planeta = Planeta(id, nombre, tipo, radio, distancia_Sol)
                planeta_service.actualizar(id, instancia_planeta)

            case 4:
                id = int(input("Ingrese el id del planeta que desea elminiar: "))
                planeta_service.borrar(id)

            case 5:
                print("¡Hasta luego! (╯°□°)╯︵ ┻━┻")
                break

if __name__ == "__main__":
    main()
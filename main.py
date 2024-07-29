from dominio.dominio import Planeta
from servicio.planetaService import PlanetaService

def main():

    planeta_service = PlanetaService()  # Crear una instancia de PlanetaService    

    while True:
        print("""
               --- MENU ---
               1. Crear planeta
               2. Consultar planetas
               3. Actualizar planeta
               4. Eliminar planeta
               5. Salir
        """)

        opcion = int(input("Seleccione una opción: "))
        match opcion:
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
                planeta_service.cerrar_conexion()
                print("¡Hasta luego! (╯°□°)╯︵ ┻━┻")
                break

if __name__ == "__main__":
    main()
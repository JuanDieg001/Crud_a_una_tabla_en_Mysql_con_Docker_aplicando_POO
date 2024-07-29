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

if __name__ == "__main__":
    main()
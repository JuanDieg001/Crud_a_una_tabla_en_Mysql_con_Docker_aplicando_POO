
# Categoria principal
class CuerpoCeleste:
    
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo


    # Getters
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo
    
    # Setters
    @id.setter
    def id(self, id):
        self._id = id

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo


# Sub categoría
class Planeta(CuerpoCeleste):
    def __init__(self, id, nombre, tipo, radio, distanciaSol):
        super().__init__(id, nombre, tipo)
        self.radio = radio
        self.distanciaSol = distanciaSol

    # Getters de la clase Planeta
    @property
    def radio(self):
        return self._radio
    
    @property
    def distanciaSol(self):
        return self._distanciaSol
    
    # Setters de la clase Planeta
    @radio.setter
    def radio(self, radio):
        self._radio = radio

    @distanciaSol.setter
    def distanciaSol(self, distanciaSol):
        self._distanciaSol = distanciaSol


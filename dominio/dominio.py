
# Clase base que representa un cuerpo celeste
class CuerpoCeleste:
    
    def __init__(self, id, nombre, tipo):#metodo constructor
        # Inicializa los atributos de la clase
        self.id = id
        self.nombre = nombre
        self.tipo = tipo


    # Getters para los atributos
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


# Subclase que representa un planeta, heredando de CuerpoCeleste
class Planeta(CuerpoCeleste):
    # Llama al constructor de la clase base
    def __init__(self, id, nombre, tipo, radio, distanciaSol):
        # Inicializa los atributos específicos de Planeta
        super().__init__(id, nombre, tipo)
        self.radio = radio
        self.distanciaSol = distanciaSol

    # Getters para los atributos adicionales de Planeta
    @property
    def radio(self):
        return self._radio
    
    @property
    def distanciaSol(self):
        return self._distanciaSol
    
    # Setters para los atributos adicionales de Planeta
    @radio.setter
    def radio(self, radio):
        self._radio = radio

    @distanciaSol.setter
    def distanciaSol(self, distanciaSol):
        self._distanciaSol = distanciaSol


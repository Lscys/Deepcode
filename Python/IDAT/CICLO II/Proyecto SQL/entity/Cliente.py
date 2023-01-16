class Cliente:
    def __init__(self, dni, nombre, apellido, telefono):
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__telefono=telefono

    @property
    def dni(self):
        return self.__dni
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido=apellido

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono=telefono
    

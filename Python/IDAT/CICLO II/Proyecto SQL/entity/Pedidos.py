class Pedidos:
    def __init__(self, codigo, nombre, direccion, producto, bebidas, fecha):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__producto=producto
        self.__bebidas=bebidas
        self.__fecha=fecha

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion=direccion

    @property
    def producto(self):
        return self.__producto
    @producto.setter
    def producto(self, producto):
        self.__producto=producto
    
    @property
    def bebidas(self):
        return self.__bebidas
    @bebidas.setter
    def bebidas(self, bebidas):
        self.__bebidas=bebidas

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha=fecha

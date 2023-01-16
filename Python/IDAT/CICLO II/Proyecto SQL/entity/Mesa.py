class Mesa:
    def __init__(self,mesa,producto,bebida,fecha):
        self.__mesa=mesa
        self.__producto=producto
        self.__bebida=bebida
        self.__fecha=fecha

    @property
    def mesa(self):
        return self.__mesa

    @property
    def producto(self):
        return self.__producto
    @producto.setter
    def producto(self,producto):
        self.__producto=producto

    @property
    def bebida(self):
        return self.__bebida
    @bebida.setter
    def bebida(self,bebida):
        self.__bebida=bebida
    
    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self,fecha):
        self.__fecha=fecha

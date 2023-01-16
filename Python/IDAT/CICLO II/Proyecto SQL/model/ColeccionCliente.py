from entity.Cliente import Cliente

class ColeccionCliente:
    def __init__(self):
        self.__listaCliente=[]
        #self.cargar()
    
    def agregar(self,objeto):
        self.__listaCliente.append(objeto)

    def longitud(self):
        return len(self.__listaCliente)
    
    def obtener(self,pos):
        return self.__listaCliente[pos]

    def buscar(self,dni):
        for i in range(self.longitud()):
            if dni==self.__listaCliente[i].dni:
                return i
        return -1 

    def eliminar(self, pos):
        del self.__listaCliente[pos]

    def modificar(self, objCliente, pos):
        self.obtener(pos).nombre = objCliente.nombre
        self.obtener(pos).apellido = objCliente.apellido
        self.obtener(pos).telefono = objCliente.telefono

    """def cargar(self):
        try:
            archivo=open("data/Cliente.txt","r",encoding="utf-8")
            for linea in archivo.readlines():
                columna=str(linea).split(";")
                dni=columna[0]
                nombre=columna[1]
                apellido=columna[2]
                telefono=columna[3]
                objCliente=Cliente(dni,nombre,apellido,telefono)
                self.agregar(objCliente)
            archivo.close()
        except IOError:
            print("Error de E/S")
    
    def grabar(self):
        archivo=open("data/Cliente.txt","w",encoding="utf-8")
        for posicion in range(self.longitud()):
            cadena=self.obtener(posicion).dni+";"
            cadena+=self.obtener(posicion).nombre+";"
            cadena+=self.obtener(posicion).apellido+";"
            cadena+=self.obtener(posicion).telefono+"\n"
            archivo.write(cadena)
        archivo.close()
     """ 
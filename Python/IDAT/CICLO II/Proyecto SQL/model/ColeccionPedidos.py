from entity.Pedidos import Pedidos

class ColeccionPedidos:
    def __init__(self):
        self.__listaPedidos=[]
        self.cargar()

    def agregar(self,objeto):
        self.__listaPedidos.append(objeto)

    def longitud(self):
        return len(self.__listaPedidos)

    def obtener(self, pos):
        return self.__listaPedidos[pos]

    def buscar(self, codigo):
        for i in range(self.longitud()):
            if codigo==self.__listaPedidos[i].codigo:
                return i
        return -1

    def eliminar(self, pos):
        del self.__listaPedidos[pos]

    def modificar(self, objPedido, pos):
        self.obtener(pos).nombre = objPedido.nombre
        self.obtener(pos).direccion = objPedido.direccion
        self.obtener(pos).producto = objPedido.producto
        self.obtener(pos).bebidas = objPedido.bebidas
        self.obtener(pos).fecha = objPedido.fecha

    def cargar(self):
        try:
            archivo=open("data/Pedidos.txt","r",encoding="utf-8")
            for linea in archivo.readlines():
                columna=str(linea).split(";")
                codigo=columna[0]
                nombre=columna[1]
                direccion=columna[2]
                producto=columna[3]
                bebidas=columna[4]
                fecha=columna[5]
                objMesa=Pedidos(codigo,nombre,direccion,producto,bebidas,fecha)
                self.agregar(objMesa)
            archivo.close()
        except IOError:
            print("Error de E/S")
    
    def grabar(self):
        archivo=open("data/Pedidos.txt","w",encoding="utf-8")
        for posicion in range(self.longitud()):
            cadena=self.obtener(posicion).codigo+";"
            cadena+=self.obtener(posicion).nombre+";"
            cadena+=self.obtener(posicion).direccion+";"
            cadena+=self.obtener(posicion).producto+";"
            cadena+=self.obtener(posicion).bebidas+";"
            cadena+=self.obtener(posicion).fecha+"\n"
            archivo.write(cadena)
        archivo.close()
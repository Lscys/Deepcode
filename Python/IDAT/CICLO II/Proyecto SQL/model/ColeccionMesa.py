from entity.Mesa import Mesa

class ColeccionMesa:
    def __init__(self):
        self.__listaMesa=[]
        self.cargar()
    
    def agregar(self,objeto):
        self.__listaMesa.append(objeto)

    def longitud(self):
        return len(self.__listaMesa)
    
    def obtener(self,pos):
        return self.__listaMesa[pos]

    def buscar(self,mesa):
        for i in range(self.longitud()):
            if mesa==self.__listaMesa[i].mesa:
                return i
        return -1 

    def eliminar(self, pos):
        del self.__listaMesa[pos]

    def modificar(self, objMesa, pos):
        self.obtener(pos).producto = objMesa.producto
        self.obtener(pos).bebida = objMesa.bebida
        self.obtener(pos).fecha = objMesa.fecha

    def cargar(self):
        try:
            archivo=open("data/Mesa.txt","r",encoding="utf-8")
            for linea in archivo.readlines():
                columna=str(linea).split(";")
                mesa=columna[0]
                producto=columna[1]
                bebidas=columna[2]
                fecha=columna[3]
                objMesa=Mesa(mesa,producto,bebidas,fecha)
                self.agregar(objMesa)
            archivo.close()
        except IOError:
            print("Error de E/S")
    
    def grabar(self):
        archivo=open("data/Mesa.txt","w",encoding="utf-8")
        for posicion in range(self.longitud()):
            cadena=self.obtener(posicion).mesa+";"
            cadena+=self.obtener(posicion).producto+";"
            cadena+=self.obtener(posicion).bebida+";"
            cadena+=self.obtener(posicion).fecha+"\n"
            archivo.write(cadena)
        archivo.close()
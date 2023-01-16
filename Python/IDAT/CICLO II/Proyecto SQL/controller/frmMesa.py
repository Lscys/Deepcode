from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem
from entity.Mesa import Mesa
from model.ColeccionMesa import ColeccionMesa

objColeccionMesa = ColeccionMesa()


class frmMesa(QMainWindow):
    def __init__(self, parent=None):
        super(frmMesa,self).__init__(parent)
        uic.loadUi("view/TablaMesa.ui", self)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.tblMesa.itemClicked.connect(self.mostrar)
        self.tblMesa.verticalHeader().setVisible(False)
        self.listar()

    def agregar(self):
        mesa = self.lneMesa.text()
        producto = self.lneProductoMesa.text()
        bebida = self.lneBebidasMesa.text()
        fecha = self.lneFechaMesa.text() 
        objMesa = Mesa(mesa,producto,bebida,fecha)
        posicion = objColeccionMesa.buscar(mesa)

        if posicion==-1:
            objColeccionMesa.agregar(objMesa)
        else:
            objColeccionMesa.modificar(objMesa, posicion)
        objColeccionMesa.grabar()
        self.listar()
        self.limpiar()

    def listar(self):
        self.tblMesa.setRowCount(objColeccionMesa.longitud())
        for i in range(objColeccionMesa.longitud()):
            self.tblMesa.setItem(i,0,QTableWidgetItem(objColeccionMesa.obtener(i).mesa))
            self.tblMesa.setItem(i,1,QTableWidgetItem(objColeccionMesa.obtener(i).producto))
            self.tblMesa.setItem(i,2,QTableWidgetItem(objColeccionMesa.obtener(i).bebida))
            self.tblMesa.setItem(i,3,QTableWidgetItem(objColeccionMesa.obtener(i).fecha))

    def limpiar(self):
        self.lneMesa.setText("")
        self.lneProductoMesa.setText("")
        self.lneBebidasMesa.setText("")
        self.lneFechaMesa.setText("")

    def mostrar(self):
        filas = self.tblMesa.selectedItems()
        indiceFila = filas[0].row()
        mesa = self.tblMesa.item(indiceFila,0).text()
        producto = self.tblMesa.item(indiceFila,1).text()
        bebidas = self.tblMesa.item(indiceFila,2).text()
        fecha = self.tblMesa.item(indiceFila,3).text()
        self.lneMesa.setText(mesa)
        self.lneProductoMesa.setText(producto)
        self.lneBebidasMesa.setText(bebidas)
        self.lneFechaMesa.setText(fecha)


    def cancelar(self):
            self.close()

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem, QMessageBox
from PyQt5 import QtWidgets as qtw
from entity.Cliente import Cliente
from model.ColeccionCliente import ColeccionCliente
import data.conexion as cn


objColeccionCliente = ColeccionCliente()


class frmCliente(qtw.QMainWindow):
    def __init__(self, parent=None):
        super(frmCliente,self).__init__(parent)
        uic.loadUi("view/TablaClientes.ui", self)
        #self.btnGuardar.clicked.connect(self.agregar)
        self.btnGuardar.clicked.connect(self.RegistrarCliente)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.tblCliente.itemClicked.connect(self.mostrar)
        self.tblCliente.verticalHeader().setVisible(False)
        #self.listar()
        self.Datos()

    def agregar(self):
        dni = self.lneDni.text()
        nombre = self.lneNombre.text()
        apellido = self.lneApellido.text()
        telefono = self.lneTelefono.text() 
        objCliente = Cliente(dni,nombre,apellido,telefono)
        posicion = objColeccionCliente.buscar(dni)

        if posicion==-1:
            objColeccionCliente.agregar(objCliente)
        else:
            objColeccionCliente.modificar(objCliente, posicion)
        #objColeccionCliente.grabar()
        #self.listar()
        self.limpiar()


    def listar(self):
        self.tblCliente.setRowCount(objColeccionCliente.longitud())
        for i in range(objColeccionCliente.longitud()):
            self.tblCliente.setItem(i,0,QTableWidgetItem(objColeccionCliente.obtener(i).dni))
            self.tblCliente.setItem(i,1,QTableWidgetItem(objColeccionCliente.obtener(i).nombre))
            self.tblCliente.setItem(i,2,QTableWidgetItem(objColeccionCliente.obtener(i).apellido))
            self.tblCliente.setItem(i,3,QTableWidgetItem(objColeccionCliente.obtener(i).telefono))


    def limpiar(self):
        self.lneDni.setText("")
        self.lneNombre.setText("")
        self.lneApellido.setText("")
        self.lneTelefono.setText("")

    def mostrar(self):
        filas = self.tblCliente.selectedItems()
        indiceFila = filas[0].row()
        dni = self.tblCliente.item(indiceFila,0).text()
        nombre = self.tblCliente.item(indiceFila,1).text()
        apellido = self.tblCliente.item(indiceFila,2).text()
        telefono = self.tblCliente.item(indiceFila,3).text()
        self.lneDni.setText(dni)
        self.lneNombre.setText(nombre)
        self.lneApellido.setText(apellido)
        self.lneTelefono.setText(telefono)
    
    def Datos(self):
        tabla=self.tblCliente
        conex=cn
        sql="SELECT dni, nombre, apellido, telefono FROM TBL_CLIENTE"
        datosP=conex.mostrarDatos(sql)
        row=0
        while(datosP.next()):
            tabla.insertRow(row)
            dni=QTableWidgetItem(str(datosP.value(0)))
            nombre=QTableWidgetItem(str(datosP.value(1)))
            apellido=QTableWidgetItem(str(datosP.value(2)))
            telefono=QTableWidgetItem(str(datosP.value(3)))
            tabla.setItem(row,0,dni)
            tabla.setItem(row,1,nombre)
            tabla.setItem(row,2,apellido)
            tabla.setItem(row,3,telefono)
            row=row+1
        conex.db.close()

    def RegistrarCliente (self):
        sql = "INSERT INTO TBL_CLIENTE (dni, nombre, apellido, telefono) VALUES (?,?,?,?)"
        datos = [self.lneDni.text(), self.lneNombre.text(), self.lneApellido.text(),self.lneTelefono.text()]
        if (cn.Query(sql, datos)):
            qtw.QMessageBox.information(self, "Exito", "Datos almacenados")
            self.Datos()
        else:
            qtw.QMessageBox.critical(self, "error", "no se puede almacenar datos")

    def cancelar(self):
            self.close()
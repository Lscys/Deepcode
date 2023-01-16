from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem
from controller.frmMesa import frmMesa
from controller.frmPedidos import frmPedidos
from controller.frmHorario import frmHorario
from controller.frmPersonal import frmPersonal
from controller.frmVentas import frmVentas
from controller.frmCliente import frmCliente
import data.conexion as cn

class Menu(QMainWindow):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        uic.loadUi("view/Menu.ui", self)
        self.btnRegistrarPedidos.clicked.connect(self.RegistrarPedidos)
        self.btnRegistrarMesa.clicked.connect(self.RegistrarPedidosMesa)
        self.btnHorario.clicked.connect(self.Horario)
        self.btnVentas.clicked.connect(self.Ventas)
        self.btnPersonal.clicked.connect(self.Personal)
        self.btnCliente.clicked.connect(self.Cliente)
        self.tblPedidosMenu.verticalHeader().setVisible(False)
        self.datos()

    def RegistrarPedidos(self):
        gui = frmPedidos(self)
        gui.show()

    def RegistrarPedidosMesa(self):
        gui = frmMesa(self)
        gui.show()

    def Horario(self):
        gui = frmHorario(self)
        gui.show()
    
    def Ventas(self):
        gui = frmVentas(self)
        gui.show()

    def Personal(self):
        gui = frmPersonal(self)
        gui.show()

    def Cliente(self):
        gui = frmCliente(self)
        gui.show()


    def datos(self):
        tabla=self.tblPedidosMenu
        conex=cn
        sql="SELECT registro_pe ,dni,cod_venta,direccion,producto,bebidas,fecha FROM TBL_RT_PEDIDOS"
        datosP=conex.mostrarDatos(sql)
        row=0
        while(datosP.next()):
            tabla.insertRow(row)
            registro=QTableWidgetItem(str(datosP.value(0)))
            dni=QTableWidgetItem(str(datosP.value(1)))
            cod_venta=QTableWidgetItem(str(datosP.value(2)))
            direccion=QTableWidgetItem(str(datosP.value(3)))
            producto=QTableWidgetItem(str(datosP.value(4)))
            bebidas=QTableWidgetItem(str(datosP.value(5)))
            fecha=QTableWidgetItem(str(datosP.value(6)))
            tabla.setItem(row,0,registro)
            tabla.setItem(row,1,dni)
            tabla.setItem(row,2,cod_venta)
            tabla.setItem(row,3,direccion)
            tabla.setItem(row,4,producto)
            tabla.setItem(row,5,bebidas)
            tabla.setItem(row,6,fecha)
            row=row+1
        conex.db.close()
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem
from entity.Pedidos import Pedidos
from model.ColeccionPedidos import ColeccionPedidos
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
#from data.conexion import Conexion
from datetime import datetime, date, time

objColeccionPedidos=ColeccionPedidos()

class frmPedidos(QMainWindow):
    def __init__(self, parent=None):
        super(frmPedidos,self).__init__(parent)
        uic.loadUi("view/TablaPedidos.ui", self)
        self.tblPedidos.verticalHeader().setVisible(False)
        self.btnAgregarPedidos.clicked.connect(self.agregar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.tblPedidos.itemClicked.connect(self.mostrar)
        #self.btnAgregarPedidos.clicked.connect(self.SQL)
        self.listar()
        self.Time()
        #Conexion()

    def agregar(self):
        codigo = self.lneCodigo.text()
        nombre = self.lneNombrePedido.text()
        direccion = self.lneDireccionPedido.text()
        producto = self.lneProductoPedidos.text()
        bebida = self.lneBebidaPedidos.text()
        fecha = self.txeFecha.text()  
        objPedidos = Pedidos(codigo,nombre, direccion,producto, bebida, fecha)
        posicion = objColeccionPedidos.buscar(codigo)
        if posicion==-1:
            objColeccionPedidos.agregar(objPedidos)
        else:
            objColeccionPedidos.modificar(objPedidos, posicion)
        objColeccionPedidos.grabar()
        self.listar()
        self.limpiar()  

    def listar(self):
        self.tblPedidos.setRowCount(objColeccionPedidos.longitud())
        for i in range(objColeccionPedidos.longitud()):
            self.tblPedidos.setItem(i,0,QTableWidgetItem(objColeccionPedidos.obtener(i).codigo))
            self.tblPedidos.setItem(i,1,QTableWidgetItem(objColeccionPedidos.obtener(i).nombre))
            self.tblPedidos.setItem(i,2,QTableWidgetItem(objColeccionPedidos.obtener(i).direccion))
            self.tblPedidos.setItem(i,3,QTableWidgetItem(objColeccionPedidos.obtener(i).producto))
            self.tblPedidos.setItem(i,4,QTableWidgetItem(objColeccionPedidos.obtener(i).bebidas))
            self.tblPedidos.setItem(i,5,QTableWidgetItem(objColeccionPedidos.obtener(i).fecha))
        
    def limpiar(self):
        self.lneCodigo.setText("")
        self.lneNombrePedido.setText("")
        self.lneDireccionPedido.setText("")
        self.lneProductoPedidos.setText("")
        self.lneBebidaPedidos.setText("")
        self.txeFecha.setText("")

    def mostrar(self):
        filas = self.tblPedidos.selectedItems()
        indiceFila = filas[0].row()
        codigo = self.tblPedidos.item(indiceFila,0).text()
        nombre = self.tblPedidos.item(indiceFila,1).text()
        direccion = self.tblPedidos.item(indiceFila,2).text()
        producto = self.tblPedidos.item(indiceFila,3).text()
        bebida = self.tblPedidos.item(indiceFila,4).text()
        fecha = self.tblPedidos.item(indiceFila,5).text()
        self.lneCodigo.setText(codigo)
        self.lneNombrePedido.setText(nombre)
        self.lneDireccionPedido.setText(direccion)
        self.lneProductoPedidos.setText(producto)
        self.lneBebidaPedidos.setText(bebida)
        self.txeFecha.setText(fecha) 
    
    def Time(self):
        self.Time = datetime.now()
        return self.txeFecha.setText(self.Time.strftime('%d-%m-%Y'))
    
    """ def SQL(self):
        codigo=self.lneCodigo.text()
        nombre=self.lneNombrePedido.text()
        bebidas=self.lneBebidaPedidos.text()
        #direccion=self.lneDireccionPedido.text()
        #producto=self.lneProductoPedidos.text()
        fecha=self.Time()
        sql=QSqlQuery()
        if self.btnAgregarPedidos.text()=="Agregar":
            sql.exec_("insert into TBL_PERSONAL values ('"+codigo+"' ,'"+
                     nombre+"','"+
                     bebidas + "','"+
                     fecha+ "');")
            print("Se guardo Correctamente")
        else:
            sql.exec_("update TBL_PERSONAL set empresa='"+codigo+"',"+
                     "nombre='"+bebidas+"',Precio='"+fecha+"';")
            self.lneCodigo.setReadOnly(False)
            self.btnAgregarPedidos.setText("Agregar")
    """

    def cancelar(self):
        self.close()

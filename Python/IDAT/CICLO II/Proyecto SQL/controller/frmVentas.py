from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtWidgets as qtw
import data.conexion as cn


class frmVentas(QMainWindow):
    def __init__(self, parent=None):
        super(frmVentas, self).__init__(parent)
        uic.loadUi("view/TablaVentas.ui", self)
        self.btnBuscar.clicked.connect(self.RegistrarVenta)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.Datos()


    def Datos(self):
        tabla=self.tblVenta
        conex=cn
        sql="SELECT cod_venta, cod_personal, monto_final, tipo_venta, fecha FROM TBL_VENTA"
        datosP=conex.mostrarDatos(sql)
        row=0
        while(datosP.next()):
            tabla.insertRow(row)
            venta=QTableWidgetItem(str(datosP.value(0)))
            personal=QTableWidgetItem(str(datosP.value(1)))
            monto_final=QTableWidgetItem(str(datosP.value(2)))
            tipo_venta=QTableWidgetItem(str(datosP.value(3)))
            fecha=QTableWidgetItem(str(datosP.value(4)))
            tabla.setItem(row,0,venta)
            tabla.setItem(row,1,personal)
            tabla.setItem(row,2,monto_final)
            tabla.setItem(row,3,tipo_venta)
            tabla.setItem(row,4,fecha)
            row=row+1
        conex.db.close()
        
    def RegistrarVenta (self):
        sql = "INSERT INTO TBL_VENTA (cod_venta, cod_personal, monto_final, tipo_venta, fecha) VALUES (?,?,?,?,?)"
        datos = [self.lneCodVenta.text(), self.lneCodPersonal.text(), self.lneMontoFinal.text(), self.lneTipoVenta.text(), self.lneFecha.text()]
        if (cn.Query(sql, datos)):
            qtw.QMessageBox.information(self, "Exito", "Datos almacenados")
            self.Datos()
        else:
            qtw.QMessageBox.critical(self, "error", "no se puede almacenar datos")



    def cancelar(self):
        self.close()

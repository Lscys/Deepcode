from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtWidgets as qtw
from datetime import datetime, date, time
import data.conexion as cn


class frmPersonal(QMainWindow):
    def __init__(self, parent=None):
        super(frmPersonal, self).__init__(parent)
        uic.loadUi("view/TablaPersonal.ui", self)   
        self.btnAgregar.clicked.connect(self.RegistrarPersonal)
        self.Datos()
        #self.Time()


    def Datos(self):
        tabla=self.tblPersonal
        conex=cn
        sql="SELECT cod_personal, nombre, telefono, fecha FROM TBL_PERSONAL"
        datosP=conex.mostrarDatos(sql)
        row=0
        while(datosP.next()):
            tabla.insertRow(row)
            personal=QTableWidgetItem(str(datosP.value(0)))
            nombre=QTableWidgetItem(str(datosP.value(1)))
            telefono=QTableWidgetItem(str(datosP.value(2)))
            fecha=QTableWidgetItem(str(datosP.value(3)))
            tabla.setItem(row,0,personal)
            tabla.setItem(row,1,nombre)
            tabla.setItem(row,2,telefono)
            tabla.setItem(row,3,fecha)
            row=row+1
        conex.db.close()

    def RegistrarPersonal (self):
        sql = "INSERT INTO TBL_PERSONAL (COD_PERSONAL, nombre, telefono, fecha) VALUES (?,?,?,?)"
        datos = [self.lneCodigo.text(), self.lneNombre.text(), self.lneTelefono.text(),self.lneFecha.text()]
        if (cn.Query(sql, datos)):
            qtw.QMessageBox.information(self, "Exito", "Datos almacenados")
            self.Datos()
        else:
            qtw.QMessageBox.critical(self, "error", "no se puede almacenar datos")

    """
    def Time(self):
        self.Time = datetime.now()
        return self.lneFecha.setText(self.Time.strftime('%Y-%m-%d'))
"""
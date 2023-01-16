from datetime import date, datetime, time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem
from PyQt5 import QtWidgets as qtw
import data.conexion as cn

class frmHorario(QMainWindow):
    def __init__(self, parent=None):
        super(frmHorario,self).__init__(parent)
        uic.loadUi("view/TablaHorario.ui",self)
        self.btnAgregar.clicked.connect(self.RegistrarHorario)
        self.btnCancelar.clicked.connect(self.cancelar)
        #self.btnBuscar.clicked.connect(self.buscar)
        self.Time()
        self.Datos()
    
    def Time(self):
        self.Time = datetime.now()
        return self.txeFecha.setText(self.Time.strftime('%d-%m-%Y --- %H:%M:%S'))

    def Datos(self):
        tabla=self.tblHorario
        conex=cn
        sql="SELECT personal, area FROM TBL_HORARIO"
        datosP=conex.mostrarDatos(sql)
        row=0
        while(datosP.next()):
            tabla.insertRow(row)
            personal=QTableWidgetItem(str(datosP.value(0)))
            area=QTableWidgetItem(str(datosP.value(1)))
            tabla.setItem(row,0,personal)
            tabla.setItem(row,1,area)
            row=row+1
        conex.db.close()
        
    def RegistrarHorario (self):
        sql = "INSERT INTO TBL_HORARIO (personal, area) VALUES (?,?)"
        datos = [self.lnePersonal.text(), self.lneArea.text()]
        if (cn.Query(sql, datos)):
            qtw.QMessageBox.information(self, "Exito", "Datos almacenados")
            self.Datos()
        else:
            qtw.QMessageBox.critical(self, "error", "no se puede almacenar datos")



    def cancelar(self):
        self.close()

"""
    def buscar(self):
        codigo = self.lneCodigo.text()
        
        if codigo == "10":
            self.lneNombre.setText("Jefferson")
            self.lneArea.setText("Cocinero")
        else:
            self.lneError.setText("Error")
"""
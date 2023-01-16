from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from controller.Menu import Menu

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/Login.ui", self)
        self.btnIngresar.clicked.connect(self.ingresar)
        self.show()

    def ingresar(self):
        usuario = self.lneUsuario.text()
        contraseña = int(self.lnePassword.text())

        if usuario == "Jefferson" and contraseña == 123456:
            self.close()
            gui = Menu(self)
            gui.show()
        else:
            self.lneUsuario.setText("")
            self.lnePassword.setText("")
            self.lblError.setText("Credenciales Incorrectas")
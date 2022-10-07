import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    gui = login()
    gui.show()
    sys.exit(app.exec())
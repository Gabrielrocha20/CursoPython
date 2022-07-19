"""
PyQT e um toolkit desenvolvido em C++ utilizado por varios programas para criaçao de aplicativos GUI(Interface Grafica)
Tambem inclui diversas funcionalidades, como: acesso a base de dados, thereads, comunicaçao de rede, etc...
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()

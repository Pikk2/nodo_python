import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType(r'C:\nado_python\nodo_python\section6\example\pyqt_basic4.ui')[0]

class TestForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()

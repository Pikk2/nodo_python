import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TestForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(800,400,500,300)

        btn1 = QPushButton("Click1", self)
        btn2 = QPushButton("Click2", self)
        btn3 = QPushButton("Exit", self)

        btn1.move(20, 20)
        btn2.move(20, 60)
        btn3.move(20, 100)

        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)
        btn3.clicked.connect(QCoreApplication.instance().quit)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked1")
        
    def btn2_clicked(self):
        QMessageBox.about(self, "message", "clicked2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()

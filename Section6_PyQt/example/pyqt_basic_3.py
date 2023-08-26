import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore

class TestForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(4200,800,800,800)

        label_1 = QLabel("입력테스트", self)
        label_2 = QLabel("출력테스트", self)

        label_1.move(20, 20)
        label_2.move(20, 60)

        self.lineEdit = QLineEdit("", self) #default 값
        self.plainEdit = QtWidgets.QPlainTextEdit(self)
        self.plainEdit.setReadOnly(True)

        self.lineEdit.move(90, 20)
        self.plainEdit.setGeometry(QtCore.QRect(20,90,361,231))

        # 시그널 생성
        self.lineEdit.textChanged.connect(self.lineEditChanged)
        self.lineEdit.returnPressed.connect(self.lineEditEnter)

        # statusBar 
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
      
    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text())
        self.lineEdit.clear()

if __name__ == "__main__":   # 공식처럼 외워!
    app = QApplication(sys.argv)
    window = TestForm()
    window.show() 
    app.exec_()
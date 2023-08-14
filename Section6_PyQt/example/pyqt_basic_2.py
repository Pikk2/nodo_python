import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TestForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(800,400,800,480)

        btn_1 = QPushButton("Click1", self)
        btn_1.move(20, 20)
        btn_2 = QPushButton("Click2", self)
        btn_2.move(20, 60)
        btn_3 = QPushButton("Click3", self)
        btn_3.move(20,100)

        btn_1.clicked.connect(self.btn_1_clicked)
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit)     # 이미 작성되어 있는 코드 연결
        # instance 가져와서 종료 해라.. 

    def btn_1_clicked(self):
        QMessageBox.about(self, "message!", "Clicked!")

    def btn_2_clicked(self):
        print("버튼 2 클릭됨ㅎㅎ")


if __name__ == "__main__":   # 공식처럼 외워!
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()

    app.exec_()
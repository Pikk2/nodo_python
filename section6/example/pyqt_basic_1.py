import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

label = QLabel("PyQT First Test")
label.show()

app.exec_()
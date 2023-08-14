import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
# print(sys.argv)

label = QLabel("PyQT First Test!!")
label.show()

print("Before Loop")
app.exec_()
# 윈도우에 종속 되어 잇음.. 루프에 반복되면서 사용자의 응답을 기다린다!
# while과 같이 무한루프임.. 
print("After Loop") # 호출이 안됨..
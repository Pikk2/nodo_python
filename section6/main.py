import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import uic
from lib.You_viewer_layout import Ui_MainWindow

'''
import Dialog
'''
from lib.AuthDialog import AuthDialog
from lib.LoginDialog_designer import MyDialog

import datetime
import re

# form_class = uic.loadUiType(r"C:/nado_python/nodo_python/section6/ui/you_viewer_v1.0.ui")[0]

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAuthenticationLock()

        # 여기서부터 중요함.. 이걸 해야 designer로 그린 UI를 불러올 수 있음 
        # pyuic5 -x you_viewer_v1.0.ui -o you_viewer_layout.py
        # from lib.AuthDialog import AuthDialog
        self.initSignal()

        # 로그인 관련 변수 선언
        self.user_id = None
        self.user_pw = None

    # 기본 UI 비활성화
    def initAuthenticationLock(self):
        self.previewButton.setEnabled(False)
        self.filenavigationButton.setEnabled(False)
        self.streamComboBox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg("인증안됨")

    # 기본 UI 활성화
    def initAuthenticationActive(self):
        self.previewButton.setEnabled(True)
        self.filenavigationButton.setEnabled(True)
        self.streamComboBox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg("인증완료")

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        # self.loginButton.clicked.connect(self.authCheck)
        self.loginButton.clicked.connect(self.designer_login)

    @pyqtSlot()
    def authCheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

        # if문에서 비교 
        print(self.user_id, self.user_pw)

        if self.user_id == "t" and self.user_pw == "1":
            self.initAuthenticationActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
        else:
            QMessageBox.critical(self, "인증오류", "ID 또는 비밀번호 인증 오류")

    @pyqtSlot()
    def designer_login(self):
        dlg = MyDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

        # if문에서 비교 
        # print(self.user_id, self.user_pw)

        if self.user_id == "t" and self.user_pw == "1":
            self.initAuthenticationActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)

            # log 추가
            self.append_log_msg("login Success")
        else:
            QMessageBox.critical(self, "인증오류", "ID 또는 비밀번호 인증 오류")


    def append_log_msg(self, act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg = self.user_id + ' : ' + act + '-(' + nowDatetime + ')'
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg)

        # 활동 로그 저장 ( 또는 DB )
        with open(r'C:\nado_python\nodo_python-1\section6\log\log.txt', 'a') as f:
            f.write(app_msg+'\n')
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
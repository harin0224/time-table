import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import

#UI파일 연결 코드
UI_class = uic.loadUiType("UI/timetable.ui")[0]


class MyWindow(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv) 

Window = MyWindow() 

Window.show()

app.exec_()
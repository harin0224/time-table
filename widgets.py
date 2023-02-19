from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import

#UI파일 연결 코드
calendarUI = uic.loadUiType("UI/calendar.ui")[0]
tableListUI = uic.loadUiType("UI/tablelist.ui")[0]


class CalendarWidget(QWidget, calendarUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
              
class TableListWidget(QWidget, tableListUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
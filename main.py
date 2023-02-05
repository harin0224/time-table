import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import
import datetime

#UI파일 연결 코드
timeTableUI = uic.loadUiType("UI/timetable.ui")[0]
calendarUI = uic.loadUiType("UI/calendar.ui")[0]
tableListUI = uic.loadUiType("UI/tablelist.ui")[0]

class MainWindow(QMainWindow, timeTableUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #시간 표시
        time = datetime.datetime.now().date()
        self.textdate.setText(str(time))
        
        #캘린더 팝업
        self.actioncalendar.triggered.connect(self.openCalendarWidget)
        
        #시간표 리스트 팝업
        self.load_the_time_table_act.triggered.connect(self.openListWidget)
        
        
        
        
        
    def openCalendarWidget (self) :
        self.calendarWidget = CalendarWidget()
        self.calendarWidget.show()
    
    def openListWidget (self) :
        self.tableListWidget = TableListWidget()
        self.tableListWidget.show()
        
    
        
    
class CalendarWidget(QWidget, calendarUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        
class TableListWidget(QWidget, tableListUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
    
    
#    def btn_clicked(self):
#       QMessageBox.about(self, "message", "clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
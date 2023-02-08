import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import
import datetime
from PyQt5.QtCore import Qt

#UI파일 연결 코드
timeTableUI = uic.loadUiType("UI/timetable.ui")[0]
calendarUI = uic.loadUiType("UI/calendar.ui")[0]
tableListUI = uic.loadUiType("UI/tablelist.ui")[0]
typingScheduleUI = uic.loadUiType("UI/typingschedule.ui")[0]

class MainWindow(QMainWindow, timeTableUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.selRow = None
        self.selColumn = None
        
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
        
    def openTypingScheduleWidget (self) :
        self.typingScheduleWidget = TypingScheduleWidget()
        if self.typingScheduleWidget.exec_():
            self.enterText = self.typingScheduleWidget.schedule_text.text()
            #print(self.selRow, self.selColumn)
            self.time_table.setItem(self.selRow, self.selColumn, QTableWidgetItem(self.enterText))
            
        
            
            
    def keyPressEvent(self, e): #키가 눌러졌을 때 실행됨
        if (e.key() == Qt.Key_Return) and self.time_table.selectedIndexes() : 
           
            self.selRow = self.time_table.selectedIndexes()[0].row()
            self.selColumn = self.time_table.selectedIndexes()[0].column()
            self.openTypingScheduleWidget()
            
    

            
        
        
        
        
class CalendarWidget(QWidget, calendarUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        
class TableListWidget(QWidget, tableListUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
class TypingScheduleWidget(QDialog, typingScheduleUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.accept)
        
    
        
        
    
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
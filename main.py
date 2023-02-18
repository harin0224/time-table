import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import
import datetime
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore
import json

#UI파일 연결 코드
timeTableUI = uic.loadUiType("UI/timetable.ui")[0]
calendarUI = uic.loadUiType("UI/calendar.ui")[0]
tableListUI = uic.loadUiType("UI/tablelist.ui")[0]
typingScheduleUI = uic.loadUiType("UI/typingschedule.ui")[0]
typingNameUI = uic.loadUiType("UI/typingname.ui")[0]

class MainWindow(QMainWindow, timeTableUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.selRow = None
        self.selColumn = None
        self.colorPalette = [(222,164,144),(222,220,189),(255,207,191),(139,195,74),
                             (255,207,153),(140,161,255),(255,253,191),(189,153,255)]
        self.colorCnt = 0
        
        #시간 표시
        time = datetime.datetime.now().date()
        self.textdate.setText(str(time))
        #캘린더 팝업
        self.actioncalendar.triggered.connect(self.openCalendarWidget)
        #시간표 리스트 팝업
        self.load_the_time_table_act.triggered.connect(self.openListWidget)
        #액션바
        self.save_act.triggered.connect(self.saveFiles)
        #self.save_as_act.triggered.connect()
        #self.load_act.triggered.connect()
        #self.calendar_act.triggered.connect()
        
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
            
            currentColor = self.colorPalette[self.colorCnt % len(self.colorPalette)]
     
            for index in self.time_table.selectedIndexes() :
                selRowColor = index.row()
                selColumnColor = index.column()
                self.time_table.setItem(selRowColor, selColumnColor, QTableWidgetItem())
                self.time_table.item(selRowColor, selColumnColor).setBackground(QtGui.QColor(currentColor[0],currentColor[1],currentColor[2]))
            self.colorCnt = self.colorCnt + 1
 
            self.time_table.item(self.selRow, self.selColumn).setText(self.enterText)
            

        
    def keyPressEvent(self, e): #키가 눌러졌을 때 실행됨
        if (e.key() == Qt.Key_Return) and self.time_table.selectedIndexes() : 
            self.selRow = self.time_table.selectedIndexes()[0].row()
            self.selColumn = self.time_table.selectedIndexes()[0].column()
            self.openTypingScheduleWidget()
        elif (e.key() == QtCore.Qt.Key_Delete) :
             for index in self.time_table.selectedIndexes() :
                selRowColor = index.row()
                selColumnColor = index.column()
                self.time_table.setItem(selRowColor, selColumnColor, QTableWidgetItem())
            
    def saveFiles(self) :
        self.typingNameWidget = TypingNameWidget()
        if self.typingNameWidget.exec_():
            self.enterName = self.typingNameWidget.name_text.text()
            
            result = {}
            for i in range(self.time_table.rowCount()):
                for j in range(self.time_table.columnCount()):
                    item = self.time_table.item(i,j)
                    if item is None:
                        continue
                    label = self.time_table.horizontalHeaderItem(j).text()
                    print('label : ', label)
                    
                    color = item.background().color().getRgb()
                    if label not in result :
                        result[label] = []
                    temp = {
                        "row":i,
                        "column":j,
                        "text":item.text(),
                        "color":{
                            "r":color[0],
                            "g":color[1],
                            "b":color[2],
                        },
                    }
                    #print(result[label])
                    result[label].append(temp)
            with open(self.enterName + ".json", "w") as json_file:
                json.dump(result, json_file)
                
                    
            
        
        
        
        
        
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
        
class TypingNameWidget(QDialog, typingNameUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.accept)        
    
        
        
    
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
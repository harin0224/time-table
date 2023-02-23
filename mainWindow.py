from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore
import dialogs, widgets
import json, os
from shutil import copyfile

#UI파일 연결 코드
timeTableUI = uic.loadUiType("UI/timetable.ui")[0]

class MainWindow(QWidget, timeTableUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.selRow = None
        self.selColumn = None
        self.fileName = None
        self.colorPalette = [(222,164,144),(222,220,189),(255,207,191),(139,195,74),
                             (255,207,153),(140,161,255),(255,253,191),(189,153,255)]
        self.colorCnt = 0
        
        os.makedirs(os.path.expanduser('~/Documents/Timetable'), exist_ok=True)
        
        #시간 표시
        #time = datetime.datetime.now().date()
        #self.textdate.setText(str(time))

        #액션바
        self.save_act.triggered.connect(self.saveFiles)
        self.save_as_act.triggered.connect(self.saveAs)
        self.load_act.triggered.connect(self.openListWidget)
        #self.calendar_act.triggered.connect()
        
    def openCalendarWidget (self) :
        self.calendarWidget = widgets.CalendarWidget()
        self.calendarWidget.show()
    
    def openListWidget (self) :
        self.tableListWidget = dialogs.TableListWidget()
        self.tableListWidget.show()
        
    def openTypingScheduleWidget (self) :
        self.typingScheduleWidget = dialogs.TypingScheduleWidget()
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
                self.time_table.item(selRowColor, selColumnColor).setBackground(QtGui.QColor(255,255,255))

    def getTableData(self) :
        result = {}
        for i in range(self.time_table.rowCount()):
            for j in range(self.time_table.columnCount()):
                item = self.time_table.item(i,j)
                if item is None:
                    continue
                label = self.time_table.horizontalHeaderItem(j).text()
                
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
                result[label].append(temp)
        return result        
                        
    def getFilePath(self, fileName):
        return os.path.expanduser('~/Documents/Timetable/' + fileName + '.json')
    
    def saveFiles(self) :
        result = self.getTableData()
        if self.fileName is None:
            self.typingNameWidget = dialogs.TypingNameWidget()
            if self.typingNameWidget.exec_():
                self.fileName = self.typingNameWidget.name_text.text()     

                with open(self.getFilePath(self.fileName), 'w') as json_file:
                    json.dump(result, json_file)
         
    def saveAs(self) :    
        self.typingNameWidget = dialogs.TypingNameWidget()
        if self.typingNameWidget.exec_():
            result = self.getTableData()                                   
            self.fileName = self.typingNameWidget.name_text.text()
            
            with open(self.getFilePath(self.fileName), 'w') as json_file:
                   json.dump(result, json_file)

    def setTableData(self, data) :
        for day in data:
            for index in data[day]:
                self.time_table.setItem(index['row'], index['column'], QTableWidgetItem(index['text']))
                self.time_table.item(index['row'], index['column']).setBackground(
                    QtGui.QColor(index['color']['r'], index['color']['g'], index['color']['b'])
                )

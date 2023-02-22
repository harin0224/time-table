from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import
import os
import mainWindow

#UI파일 연결 코드
typingScheduleUI = uic.loadUiType("UI/typingschedule.ui")[0]
typingNameUI = uic.loadUiType("UI/typingname.ui")[0]
tableListUI = uic.loadUiType("UI/tablelist.ui")[0]


class TypingScheduleWidget(QDialog, typingScheduleUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.schedule_text.setFocus()
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        
class TypingNameWidget(QDialog, typingNameUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.name_text.setFocus()
        self.ok_btn.clicked.connect(self.accept) 
        self.cancel_btn.clicked.connect(self.reject)       

class TableListWidget(QDialog, tableListUI) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.getTableNames()
        self.showTableNames()
        self.Load_btn.clicked.connect(self.loadFile)
        #self.Del_btn.clicked.connect() 
        #self.loadFile()
        
        
        
    def getTableNames (self) :
        pathDir = os.path.expanduser('~/Documents/Timetable')
        fileList = os.listdir(pathDir)
        return fileList
        
    
    def showTableNames (self) :
        for index in self.getTableNames() :
            self.listWidget.addItem(index)
            
    def loadFile (self) :
        
        fileName = self.listWidget.selectedItems()
        print(fileName[0].text())
        


        
    

from PyQt5.QtWidgets import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import

#UI파일 연결 코드
typingScheduleUI = uic.loadUiType("UI/typingschedule.ui")[0]
typingNameUI = uic.loadUiType("UI/typingname.ui")[0]


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
    
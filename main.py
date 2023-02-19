import sys
from PyQt5.QtWidgets import *
import mainWindow
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = mainWindow.MainWindow()
    mainWindow.show()
    app.exec_()
import sys
from PyQt5.QtWidgets import *
import mainWindow
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = mainWindow.MainWindow()
    main.show()
    app.exec_()
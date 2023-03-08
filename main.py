import sys
from PyQt5.QtWidgets import *
import mainWindow, common
#from os import environ
from PyQt5.QtGui import QIcon
    
# environ["QT_DEVICE_PIXEL_RATIO"] = "1"
# environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
# environ["QT_SCREEN_SCALE_FACTORS"] = "1"
# environ["QT_SCALE_FACTOR"] = "1"

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = mainWindow.MainWindow()
    app.setWindowIcon(QIcon(common.getResourcePath('meow.ico')))
    main.show()
    app.exec_()
    
 
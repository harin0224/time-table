import sys
from PyQt5.QtWidgets import *
import mainWindow
from os import environ
    
# environ["QT_DEVICE_PIXEL_RATIO"] = "1"
# environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
# environ["QT_SCREEN_SCALE_FACTORS"] = "1"
# environ["QT_SCALE_FACTOR"] = "1"

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = mainWindow.MainWindow()
    main.show()
    app.exec_()
    
 
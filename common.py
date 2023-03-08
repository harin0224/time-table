import sys, os
from PyQt5 import uic

def getUIFile(relative_path):
    form = getResourcePath(relative_path)
    form_class = uic.loadUiType(form)[0]
    return form_class

def getResourcePath(path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, path)
import sys, os
from PyQt5 import uic

def getUIFile(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    form = os.path.join(base_path, relative_path)
    print(form)
    form_class = uic.loadUiType(form)[0]
    return form_class

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPixmap

form_class = uic.loadUiType("myomok01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
        self.lbl.mousePressEvent = self.lbl_click
        self.show()

        
    def myClick(self):
        try:
            icon_path = '2.png'
            icon = QIcon(icon_path)
            self.pb.setIcon(icon)
        except Exception as e : 
            print(e)
            
    def lbl_click(self, event):
        try:
            img = QPixmap('2.png')
            
            self.lbl.setPixmap(img)
        except Exception as e :
            print(e)
            
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
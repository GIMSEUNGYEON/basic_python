import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("myqt09.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.buttons = [self.pb1, self.pb2, self.pb3, self.pb4, self.pb5, 
                        self.pb6, self.pb7, self.pb8, self.pb9, self.pb0]
        
        for button in self.buttons :
            button.clicked.connect(self.myClick)
        
        self.pb_call.clicked.connect(self.myCall)
        
    def myClick(self):
        num = self.sender()
        old_str = self.le.text()
        new_str = num.text()
        
        self.le.setText(old_str + new_str)
            

    def myCall(self):
        str_tel = self.le.text()
        QMessageBox.about(self,'Calling','calling...\n'+str_tel)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
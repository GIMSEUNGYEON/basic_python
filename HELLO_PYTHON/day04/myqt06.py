import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt06.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        
        if(random() > 0.5) :
            self.le_com.setText("홀")
        else : 
            self.le_com.setText("짝")
            
        com = self.le_com.text()
        # print(com)
        mine = self.le_mine.text()
        # print(mine)
        if(mine == com) : 
            self.le_result.setText("승리")
        else :
            self.le_result.setText("패배")
                
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
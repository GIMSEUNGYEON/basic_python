import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt08.ui")[0]
# 업 앤 다운 게임
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.com = (int)(random()*99) +1
        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        mine = int(self.le.text())
        print(mine)
        str = self.pte.toPlainText()
        
        if (mine < self.com) :
            str += (f"{mine} UP\n")
        elif (mine > self.com) : 
            str += (f"{mine} DOWN\n")
        elif(mine == self.com) : 
            str += (f"{mine} 정답입니다!\n")
        
        self.pte.setPlainText(str)
            
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
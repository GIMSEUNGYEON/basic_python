import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt05.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myClick)
    # lotto 
    def myClick(self):
        arr = [1,2,3,4,5,       6,7,8,9,10,    
               11,12,13,14,15,  16,17,18,19,20, 
               21,22,23,24,25,  26,27,28,29,30, 
               31,32,33,34,35,  36,37,38,39,40,      
               41,42,43,44,45 ]
        
        for i in range(10000) :
            rnd = int(random()*len(arr))
            a = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = a
            
        self.sp1.setValue(arr[0])
        self.sp2.setValue(arr[1])
        self.sp3.setValue(arr[2])
        self.sp4.setValue(arr[3])
        self.sp5.setValue(arr[4])
        self.sp6.setValue(arr[5])
        # self.sp1.setValue()

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
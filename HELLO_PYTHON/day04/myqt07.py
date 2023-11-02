import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt07.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        # self.getStar(5)
        self.pb.clicked.connect(self.myClick)
    
    def myClick(self):
        first = self.sb_first.value()
        last = self.sb_last.value()
        answer = ''
        for i in range(first, last+1) :
            print(i)
            answer += self.getStar(i)
    
        self.te.setPlainText(answer)
    

    def getStar(self, num):
        star = ''
        for i in range(1,num+1) :
            star += '*'
        star+='\n'
        # print(star)
        return star
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
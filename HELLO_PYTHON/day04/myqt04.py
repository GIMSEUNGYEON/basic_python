import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt04.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        dan = int(self.te.toPlainText())
        # toPlainText가져올 땐 여러줄 가져올때
        # labelText는 한줄만 들어갈 수 있는 텍스트이므로 text로 가져옴
        str = "";
        for i in range(1, 9+1) :
            str += f"{dan} * {i} = {dan*i}\n"
            
        self.pte.setPlainText(str)
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QWidget, QPushButton, QLabel, QPixmap

    
class MainClass(QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.show()
        self.flag_wb = True
        self.flag_ing = True
        self.pane()
    
    def pane(self):
        self.setGeometry(100,100,450,450)
        self.setWindowTitle('omok')
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        self.lbl_reset = QPushButton('reset', central_widget)
        self.lbl_reset.setGeometry(410, 25, 40,40)
        self.lbl_reset.clicked.connect(self.myReset)
        
        self.lbl2D = [[None for _ in range(10)] for _ in range(10)]
        
        for i in range(10) : 
            for j in range(10) :
                self.lbl2D[i][j] = QLabel('', central_widget)
                self.lbl2D[i][j].setPixmap(QPixmap('0.png'))                
                self.lbl2D[i][j].setGeometry(j*40, i*40, 40, 40)
                self.lbl2D[i][j].setText('')
                self.lbl2D[i][j].mousePressEvent = self.myClick
                # print(self.lbl2D[i][j]) # PyQt5.QtWidgets.QLabel object
        self.arr2D = [[0]*10 for _ in range(10)]
        
        # self.myRender()
    
    def myClick(self, event):
        if not(self.flag_ing) : 
            return
        try :
            lbl = self.sender()
            if self.flag_wb : 
                print(lbl)
                # print(f'event {event}') # PyQt5.QtGui.QMouseEvent object
                # lbl.setPixmap(QPixmap('1.png'))                
        except Exception as e : 
            print(f'error : {e}')
    def myRender(self):
        pass
    
    def myReset(self):
        pass 
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
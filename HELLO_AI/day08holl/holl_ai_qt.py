import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
import tensorflow as tf
import numpy as np

form_class = uic.loadUiType("holl_ai_qt.ui")[0]
model = tf.keras.models.load_model('holl.h5')

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        mine = self.le_mine.text()
        # print(mine)
        
        if mine == "홀" :
            x_rf = np.array([
                [1,0]
            ])
        else : 
            x_rf = np.array([
                [0,1]
            ])
            
        pred_rf = model.predict(x_rf)
        com = np.argmax(pred_rf)
        com_ans = ""
        if com == 0:
            com_ans = "홀"

        else:
            com_ans = "짝"
        
        self.le_com.setText(com_ans)
        
        if(mine == com_ans) : 
            self.le_result.setText("승리")
        else :
            self.le_result.setText("패배")
                
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()

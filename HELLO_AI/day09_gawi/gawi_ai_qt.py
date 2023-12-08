import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import tensorflow as tf
import numpy as np

form_class = uic.loadUiType("gawi_ai_qt.ui")[0]
model = tf.keras.models.load_model('gawi.h5')

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myClick)
        
    def myClick(self):
        mine = self.le_mine.text()
        result =""
        if mine == "가위" :
            x_rf = np.array([
                [1,0,0]
            ])
        elif mine == "바위" : 
            x_rf = np.array([
                [0,1,0]
            ])
        elif mine == "보" :
            x_rf = np.array([
                [0,0,1]
            ])
            
        pred_rf = model.predict(x_rf)
        com = np.argmax(pred_rf)
        com_ans = ""
        if com == 0:
            com_ans = "가위"
        elif com == 1:
            com_ans = "바위"        
        elif com == 2:
            com_ans = "보"
        
        self.le_com.setText(com_ans)
        
        if com_ans == "가위" and mine == "가위" : result = "비김"
        if com_ans == "가위" and mine == "바위" : result = "이김"
        if com_ans == "가위" and mine == "보" : result = "짐"
        
        if com_ans == "바위" and mine == "가위" : result = "짐"
        if com_ans == "바위" and mine == "바위" : result = "비김"
        if com_ans == "바위" and mine == "보" : result = "이김"
        
        if com_ans == "보" and mine == "가위" : result = "이김"
        if com_ans == "보" and mine == "바위" : result = "짐"
        if com_ans == "보" and mine == "보" : result = "비김"
        
        self.le_result.setText(result)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()

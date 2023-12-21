import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QMessageBox
from tensorflow.keras.models import load_model
import numpy as np

form_class = uic.loadUiType("myomok03_20_myai.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.model = load_model('omok.h5')
        # self.gibo = [
        #         {'i':0, 'j':0},
        #         {'i':1, 'j':0},
        #         {'i':2, 'j':0},
        #         {'i':3, 'j':0},
        #         {'i':4, 'j':0}
        #     ]
        #
        # self.gibo_cnt = 0
        
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
        ]
        
        self.pb2D =[]
        self.flag_wb=True;
        self.flag_ing=True;
        self.setupUi(self)
        self.pb.clicked.connect(self.myreset)
        for i in range(20):
            line = []
            for j in range(20):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                btn.clicked.connect(self.myclick)
                btn.setToolTip("{},{}".format(i,j))
                line.append(btn)
            self.pb2D.append(line)
                
        self.show()
        self.myrender()
        
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j]==0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j]==1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j]==-1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                    
                    
    
    def myclick(self) :
        if not(self.flag_ing):
            return
        
        str_ij=self.sender().toolTip()
        arr_ij=str_ij.split(",")
        i=int(arr_ij[0])
        j=int(arr_ij[1])
        
        if self.arr2D[i][j]>0:
            return

        self.arr2D[i][j]=1
        stone=1
     
        self.myrender()
        
        UP = self.getUP(i,j,stone);
        DW = self.getDW(i,j,stone);
        LE = self.getLE(i,j,stone);
        RI = self.getRI(i,j,stone);
        
        UR = self.getUR(i,j,stone);
        UL = self.getUL(i,j,stone);
        DR = self.getDR(i,j,stone);
        DL = self.getDL(i,j,stone);
        
        # print('흑돌')
        # print(UP, end="\t")
        # print(DW, end="\t")
        # print(LE, end="\t")
        # print(RI, end="\t")
        #
        # print(UR, end="\t")
        # print(UL, end="\t")
        # print(DR, end="\t")
        # print(DL, end="\t\n")
        
        d1=UP+DW+1;
        d2=LE+RI+1;
        d3=UR+DL+1;
        d4=DR+UL+1;
        
        if d1==5 or d2==5 or d3==5 or d4==5 :
            vic="흑";
            self.flag_ing=not(self.flag_ing)
            QMessageBox.about(self, "승리", vic+"돌 승리")
            
#------------------------------------------------------------------------------------------
        
        if not(self.flag_ing):
            return
        
        input = np.array(self.arr2D)
        input = np.expand_dims(input, axis=(0, -1)).astype(np.float32)
        
        output = self.model.predict(input)
        
        out400 = np.argmax(output[0])
        
        ii = int(out400/20)
        
        jj = out400%20
        
        output = output.reshape((20,20))
        print("out400",out400)
        print("ii",ii)
        print("jj",jj)
        
        
        output_y, output_x = np.unravel_index(np.argmax(output), output.shape)

        i = output_y
        j = output_x
        
        self.arr2D[i][j]=-1
        stone=-1
        
        self.myrender()
        
        UP = self.getUP(i,j,stone);
        DW = self.getDW(i,j,stone);
        LE = self.getLE(i,j,stone);
        RI = self.getRI(i,j,stone);
        
        UR = self.getUR(i,j,stone);
        UL = self.getUL(i,j,stone);
        DR = self.getDR(i,j,stone);
        DL = self.getDL(i,j,stone);
        
        # print('백돌')
        # print(UP, end="\t")
        # print(DW, end="\t")
        # print(LE, end="\t")
        # print(RI, end="\t")
        #
        # print(UR, end="\t")
        # print(UL, end="\t")
        # print(DR, end="\t")
        # print(DL, end="\t\n")
        
        
        d1=UP+DW+1;
        d2=LE+RI+1;
        d3=UR+DL+1;
        d4=DR+UL+1;
        
        if d1==5 or d2==5 or d3==5 or d4==5 :
            vic="백";
            self.flag_ing=not(self.flag_ing)
            QMessageBox.about(self, "승리", vic+"돌 승리")
            
    def myreset(self) :
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j]=0
                
        self.myrender()
        self.flag_ing=True
        self.flag_wb=True
        self.gibo_cnt = 0

    def getUP(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                i=i-1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e:
            return cnt;
    def getDW(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i+=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except :
            return cnt;
    def getRI(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                j+=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e:
            return cnt;
    def getLE(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                j-=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e:
            return cnt;
    
    def getUL(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i-=1
                j-=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;
        
    def getUR(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i-=1
                j+=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;
    def getDL(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i+=1
                j-=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;
    def getDR(self,i,j,stone) :
        cnt = 0;
        try:
            while True:
                i+=1
                j+=1
                if i < 0:
                    return cnt;
                if j < 0:
                    return cnt;
                if self.arr2D[i][j]==stone:
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            return cnt;   
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    
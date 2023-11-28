import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton, QMessageBox

form_class = uic.loadUiType("myomok02.ui")[0]

arr2D = [[0]*15 for _ in range(15)]
flag_wb = True
flag_ing = True
# wb가 true일 때 흑돌, 흑돌이 2

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.pb2D = [[None for _ in range(10)] for _ in range(10)]
        for i in range(len(self.pb2D)) :
            for j in range(len(self.pb2D[0])) : 
                self.pb2D[i][j] = QPushButton("", self)
                self.pb2D[i][j].setIcon(QIcon("0.png"))
                self.pb2D[i][j].setIconSize(QtCore.QSize(40,40))
                self.pb2D[i][j].setGeometry(40 * j,40 * i,40,40)
                self.pb2D[i][j].clicked.connect(lambda _, i=i, j=j: self.myClick( i, j))
                
        self.pb.clicked.connect(self.myReset)
        self.show()
        
    def myClick(self, i, j):
        global flag_wb
        global flag_ing
        # print(arr2D[i][j])
        if not(flag_ing):
            return 
        
        try:
            btn = self.sender()
            
            if arr2D[i][j] != 0 : 
                return
            # print(i, j)
            if flag_wb :
                icon_path = '2.png'
                btn.setToolTip('2')
                arr2D[i][j] = 2
            else : 
                icon_path = '1.png'
                btn.setToolTip('1')
                arr2D[i][j] = 1
                
            icon = QIcon(icon_path)
            btn.setIcon(icon)
            
            stone = arr2D[i][j]
            
            up = self.getUP(i, j, stone)
            dw = self.getDW(i, j, stone)
            le = self.getLE(i, j, stone)
            ri = self.getRI(i, j, stone)
            ur = self.getUR(i, j, stone)
            ul = self.getUL(i, j, stone)
            dr = self.getDR(i, j, stone)
            dl = self.getDL(i, j, stone)
            
            # print("up", up)
            
            d1 = up + dw + 1;
            d2 = ur + dl + 1;
            d3 = ri + le + 1;
            d4 = ul + dr + 1;
            
            if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
                if flag_wb :
                    tmp = '흑'
                else :
                    tmp = '백'
                    
                QMessageBox.information(self, '결과', tmp+"돌 승리")
                flag_ing = False
            
        except Exception as e : 
            print(e)
        
        finally:
            flag_wb = not(flag_wb)
     
    def getUP(self, row, col, stone):            
        cnt = 0
        try:
            while True :
                row-=1
                if(arr2D[row][col] == stone) :
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            print(e)

    def getDW(self, row, col, stone):            
        cnt = 0
        try:
            while True :
                row+=1
                if(arr2D[row][col] == stone) :
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            print(e)

    def getLE(self, row, col, stone):            
        cnt = 0
        try:
            while True :
                col-=1
                if(arr2D[row][col] == stone) :
                    cnt+=1
                else :
                    return cnt;
        except Exception as e :
            print(e)
    
    def getRI(self, row, col, stone):            
        cnt = 0
        try:
            while True :
                col+=1
                if(arr2D[row][col] == stone) :
                    cnt+=1
                else :
                    return cnt;
    
        except Exception as e :
            print(e)

    def getUR(self, row, col, stone):            
        cnt = 0
        try:
            while True :
                row-=1
                col+=1
                if(arr2D[row][col] == stone) :
                    cnt+=1
                else :
                    return cnt;
    
        except Exception as e :
            print(e)

    def getUL(self, row, col, stone):            
        cnt = 0
        try:
            while True :
                row-=1
                col-=1
                if(arr2D[row][col] == stone) :
                    cnt+=1
                else :
                    return cnt;
    
        except Exception as e :
            print(e)
            
    def getDR(self, row, col, stone):            
        cnt = 0
        try:
            while True :
                row+=1
                col+=1
                if(arr2D[row][col] == stone) :
                    cnt+=1
                else :
                    return cnt;
    
        except Exception as e :
            print(e)

    def getDL(self, row, col, stone):            
        cnt = 0
        try:
            while True :
                row+=1
                col-=1
                if(arr2D[row][col] == stone) :
                    cnt+=1
                else :
                    return cnt;
    
        except Exception as e :
            print(e)
            
    def myReset(self):
        global flag_ing
        global flag_wb
        
        flag_ing = True
        flag_wb = True
        
        for i in range(10) : 
            for j in range(10) :
                self.pb2D[i][j].setIcon(QIcon("0.png"))
                arr2D[i][j] = 0 
    
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
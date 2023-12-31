import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QWidget, QPushButton, QLabel, QPixmap, QMessageBox

flag_wb = True
flag_ing = True
arr2D = [[0]*15 for _ in range(15)]

class MyLabel(QLabel):
    def __init__(self, row, col, parent=None):
        super().__init__(parent)
        self.row = row
        self.col = col
        
    def mousePressEvent(self, event):
        global flag_wb
        global flag_ing
        
        if not(flag_ing) :
            # 게임이 끝나면 ing를 False 처리하고 reset하면 다시 True
            return
        
        currentImg = self.pixmap().toImage().cacheKey()
        paneImg = QPixmap('0.png').toImage().cacheKey()
        
        if currentImg and currentImg != paneImg: 
            # 현재 이미지가 none이 아니고 & 패널 이미지와 같지 않을 때 
            return
            
        try : 
            if flag_wb : 
                # True일때 흑돌
                img = QPixmap('2.png')
                arr2D[self.row][self.col] = 1
            else :
                # False일때 백돌
                img = QPixmap('1.png')
                arr2D[self.row][self.col] = 2
    
            self.setPixmap(img)
            
            # print(f"클릭한 라벨 위치 : row {self.row}, col {self.col}")
            
            stone = arr2D[self.row][self.col]
            
            up = self.getUP(self.row, self.col, stone)
            dw = self.getDW(self.row, self.col, stone)
            le = self.getLE(self.row, self.col, stone)
            ri = self.getRI(self.row, self.col, stone)
            ur = self.getUR(self.row, self.col, stone)
            ul = self.getUL(self.row, self.col, stone)
            dr = self.getDR(self.row, self.col, stone)
            dl = self.getDL(self.row, self.col, stone)
            
            # print("up",up)
            # print("dw",dw)
            # print("le",le)
            # print("ri",ri)
            # print("ur",ur)
            # print("ul",ul)
            # print("dr",dr)
            # print("dl",dl)
            
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
                
            flag_wb = not(flag_wb)
            # 한 턴이 끝나면 순서 반전
        except Exception as e :
            print(e)
        
        
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
        
class MainClass(QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.show()
        self.flag_wb = True
        self.flag_ing = True
        self.pane()
    
    def pane(self):
        # 패널을 선언하는 메서드

        self.setGeometry(100,100,650,650)
        self.setWindowTitle('omok')
        # 전체 패널 크기, 윈도우창의 이름 설정
        
        central_widget = QWidget(self)
        
        self.setCentralWidget(central_widget)
        # 중앙 위젯에 해당하여 윈도우 초기화
        
        self.btn_reset = QPushButton('reset', central_widget)
        self.btn_reset.setGeometry(610, 25, 40,40)
        self.btn_reset.clicked.connect(self.MyClick)
        # 리셋 버튼 선언
        
        self.lbl2D = [[None for _ in range(15)] for _ in range(15)]
        
        img = QPixmap('0.png')
        for i in range(15) : 
            for j in range(15) :
                self.lbl2D[i][j] = MyLabel(i, j, central_widget)
                self.lbl2D[i][j].setPixmap(img)                
                self.lbl2D[i][j].setGeometry(j*40, i*40, 40, 40)
        # 2차원 라벨 배열 선언
        
    def MyClick(self):
        global flag_ing
        global flag_wb
        
        flag_ing = True
        flag_wb = True
        
        for i in range(15) : 
            for j in range(15) :
                self.lbl2D[i][j].setPixmap(QPixmap('0.png'))
                arr2D[i][j] = 0                
    # 리셋 버튼이 클릭됐을 때 호출되는 리셋 메서드    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    
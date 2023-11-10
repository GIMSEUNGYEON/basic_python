import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('myqt01.ui', self)
        
        self.pb.clicked.connect(self.change_label_text)
        # pb객체가 클릭되면 함수를 호출
        self.click_count = 0
        # 클릭 횟수를 카운트하는 변수
        
    def change_label_text(self):
        self.click_count += 1
        print('click')
        # 함수가 호출될 때마다 클릭 횟수 증가
        if(self.click_count%2 == 0) :
            new_text = "Good Morning"
            # 클릭 횟수가 짝수이면 Good Morning으로 대체
        else : 
            new_text = "Good Evening"
            # 클릭 횟수가 홀수이면 Good Evening으로 대체
            
        self.lbl.setText(new_text)
        # lbl객체의 텍스트를 new_text로 변환
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # QApplication: 프로그램을 실행시켜주는 클래스
    window = MyWindow()
    # WindowClass의 인스턴스 생성
    window.show()
    # 프로그램 화면을 보여주는 코드
    sys.exit(app.exec_())
    # 프로그램을 작동시키는 코드
    
    
    
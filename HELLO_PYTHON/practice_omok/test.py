import sys
from PyQt5 import uic
from PyQt5.Qt import QPixmap, QLabel
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI 파일(myqt10.ui)을 로드하고 사용할 클래스를 미리 정의
form_class = uic.loadUiType("./omok_10.ui")[0]

# 전역 변수로 사용할 boolean 변수 선언, 초기값은 True
flag_wb = True

# MyLabel 클래스 정의
class MyLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)  # QLabel 클래스의 생성자 호출
       
    def mousePressEvent(self, event):
        global flag_wb
        
        # flag_wb에 따라 이미지를 변경
        if flag_wb:
            icon = QPixmap("/workspace_python/HELLO_PYTHON/day04/1.png")
        else:
            icon = QPixmap("/workspace_python/HELLO_PYTHON/day04/2.png")
            
        self.setPixmap(icon)  # 현재 라벨의 이미지를 변경
        flag_wb = not flag_wb  # flag_wb 값을 반전

# WindowClass 클래스 정의
class WindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        super().__init__(parent)  # QMainWindow과 UI 클래스 생성자 호출
        self.setupUi(self)  # UI를 초기화하고 설정

        # 15x15 그리드 생성 및 각 라벨에 이미지 설정
        for i in range(15):
            for j in range(15):
                icon = QPixmap("/workspace_python/HELLO_PYTHON/day04/0.png")  # 이미지 로드
                label = MyLabel(self)  # MyLabel 클래스의 인스턴스 생성
                label.setPixmap(icon)  # 라벨에 이미지 설정
                label.setGeometry(0 + i * 40, 0 + j * 40, 40, 40)  # 라벨의 위치 및 크기 설정

if __name__ == "__main__":
    app = QApplication(sys.argv)  # PyQt5 애플리케이션을 초기화
    myWindow = WindowClass()  # WindowClass의 인스턴스 생성
    myWindow.show()  # 창을 화면에 표시
    app.exec_()  # 애플리케이션 실행
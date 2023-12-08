import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

form_class = uic.loadUiType("my_daejeon_qt01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        self.browser = webdriver.Firefox()
        self.url = 'http://traffic.daejeon.go.kr'
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.browser.get(self.url)
        self.pb.clicked.connect(self.myClick)
        self.show()
    def myClick(self):
        self.list = []
        try:
            inputs = self.browser.find_elements(By.CSS_SELECTOR, "input[type='hidden']")
            for idx, i in enumerate(inputs):
                values = i.get_attribute("value")
                json_data = json.loads(values)
                if isinstance(json_data, int):
                    continue
                print(idx, json_data.get("busstopNm"), end=" ")
                print("위도", json_data.get("gpsLati"), end=" ")
                print("경도", json_data.get("gpsLong"))
                
        except Exception as e :
            print(e)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass()
    app.exec_()
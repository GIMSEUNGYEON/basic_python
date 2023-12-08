import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.by import By

form_class = uic.loadUiType("my_selenium_qt01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        self.browser = webdriver.Firefox()
        self.url = 'https://map.kakao.com/'
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.browser.get(self.url)
        self.pb.clicked.connect(self.myClick)
        self.show()
    def myClick(self):
        self.list = []
        try:
            strongs = self.browser.find_elements(By.CSS_SELECTOR, "strong[class='busstop']")
            for idx, s in enumerate(strongs) :
                
                obj_sele_s = s.find_element(By.XPATH,"..")
                obj_busstop = obj_sele_s.find_element(By.CSS_SELECTOR,"p[class='busid']")
                
                sta_name = s.text
                sta_id = obj_busstop.text
                print(idx, sta_name, sta_id)
        
        except Exception as e :
            print(e)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass()
    app.exec_()
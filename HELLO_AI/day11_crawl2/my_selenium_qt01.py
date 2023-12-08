import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

form_class = uic.loadUiType("my_selenium_qt01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        self.browser = webdriver.Firefox()
        self.url = 'https://map.kakao.com/'
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
        self.show()
    def myClick(self):
        try:
            self.browser.get(self.url)
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placename')))
            # print(self.browser.page_source)
            bus_stop = (self.browser.find_element(By.CLASS_NAME, "placename").text)
            print(bus_stop)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'busname')))
            bus = (self.browser.find_element(By.CLASS_NAME, "busname").text)
            print(bus)
        except Exception as e:
            print(e)
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
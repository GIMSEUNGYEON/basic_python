import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from day11_crawl2.dao_bus_path import DaoBusPath

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
        self.dbp = DaoBusPath()
    def myClick(self):
        self.list = []
        try:
            bp_name = self.browser.find_element(By.CSS_SELECTOR, "mark[class*='bus_type']").text
            bus_no = self.browser.find_element(By.CSS_SELECTOR, "strong[class='bus_no']").text
            spans = self.browser.find_elements(By.CSS_SELECTOR, "span[class='st_id']")
            
            bp_name += bus_no
            
            for idx, s in enumerate(spans):
                parent_s = s.find_element(By.XPATH, '..')
                span2 = parent_s.find_elements(By.CSS_SELECTOR, "span[class='st_name']")

                sta_id = s.text
                sta_name = span2[0].text
                
                
                ip = parent_s.find_elements(By.CSS_SELECTOR, "input")[0]
                txt = ip.get_attribute("value")
                myjson = json.loads(txt)
        
                lat = myjson["gpsLati"]
                lng = myjson["gpsLong"]
                
                print(idx, sta_id, sta_name, lat, lng)
                cnt = self.dbp.insert(bp_name, idx, sta_id, sta_name, lat, lng)
                
                print(cnt)
        except Exception as e :
            print(e)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass()
    app.exec_()
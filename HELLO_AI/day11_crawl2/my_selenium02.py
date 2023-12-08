from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
url = 'https://map.kakao.com/'
browser.get(url)


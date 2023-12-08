from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://localhost:8888/HELLO_WEB_EMP/emp_list'
browser.get(url)
print(browser.page_source)
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'http://localhost:8888/HELLO_WEB_EMP/emp_list'
browser.get(url)
# print(browser.page_source)
# time.sleep(5)
trs = (browser.find_elements(By.CSS_SELECTOR, "tr"))

for idx, tr in enumerate(trs) :
    if idx==0:
        continue
    # print(tr.get_attribute("outerHTML"))
    tds = tr.find_elements(By.CSS_SELECTOR, "td")
    # print(tr.text)
    print(tds[1].text, tds[3].text)
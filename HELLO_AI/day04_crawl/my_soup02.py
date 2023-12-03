import requests
from bs4 import BeautifulSoup as bs

url='http://localhost:8888/HELLO_WEB_EMP/emp_list'

resp = requests.get(url)

soup= bs(resp.text, "html.parser")


trs = soup.select("tr")

for idx, tr in enumerate(trs) :
    if idx == 0:
        continue
    tds = tr.select("td")
    print(tds[1].text, tds[3].text)

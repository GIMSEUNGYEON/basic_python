import requests
from bs4 import BeautifulSoup as bs

url='http://localhost:8888/MVVM_EMP/emp.html'

resp = requests.get(url)
resp.encoding = 'utf-8'
soup= bs(resp.text, "html.parser", from_encoding='utf-8')
# print(resp.text)

# print(soup)

trs = soup.select("tr")

print(trs)

# for idx, tr in enumerate(trs) :
#     if idx == 0:
#         continue
#     tds = tr.select("td")
#     print(tds[1].text, tds[3].text)
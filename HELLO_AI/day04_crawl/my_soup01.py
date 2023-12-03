import requests
from bs4 import BeautifulSoup as bs

url='http://localhost:8888/HELLO_WEB_EMP/emp_list'

resp = requests.get(url)

# print(resp) # status code

# print("==========================")

# print(resp.text) # html

soup= bs(resp.text, "html.parser")

# print("==========================")

# print(soup) # text parsing html

print(soup.find_all("tr")[1].find_all("td")[1].text)
print(soup.find_all("tr")[1].find_all("td")[3].text)

print(soup.find_all("tr")[2].find_all("td")[1].text)
print(soup.find_all("tr")[2].find_all("td")[3].text)

trs = soup.find_all("tr")
for idx, t in enumerate(trs) : 
    if idx == 0 :
        continue
    tds = t.find_all("td")
    print(tds[1].text, tds[3].text)



from bs4 import BeautifulSoup as bs
import requests
import re
import time
from datetime import datetime
from homework.DaoKospi import DaoKospi
temp = 0
dk = DaoKospi()
url = 'https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry'
while True :
    resp = requests.get(url)
    
    soup = bs(resp.text, "html.parser")
    
    name_list = soup.select(".st_name")
    price_list = soup.select(".st_price")
    code_list = []
    for i in name_list : 
        tmp = (i.select("a[href]"))
        i = str(tmp)
        match = re.search(r'/price/home/(\w+)', i)
        code_list.append(match.group(1))
    
    current_time = datetime.now().strftime("%Y%m%d_%H%M")
    
    for i in range(len(name_list)):
        cnt = dk.insert(name_list[i].text, price_list[i].text.replace(",", ""), code_list[i], current_time)
        temp += cnt;
    print(temp, "행 성공")
    time.sleep(60)
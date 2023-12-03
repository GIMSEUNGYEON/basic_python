import time
import requests
from bs4 import BeautifulSoup as bs
import datetime
from day04_crawl.daostock import DaoStock

ds = DaoStock()

ymd = datetime.datetime.now().strftime("%Y%m%d-%H%M")

res = requests.get("https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry")

soup = bs(res.text, "html.parser")

name= soup.select(".st_name")
for idx, n in enumerate(name):
    s_name = n.text.strip()
    s_code = n.select("a")[0]["href"].split("/")[3]
    price = n.parent.select(".price")[0].text.replace(",", "")
    cnt = ds.insert(s_name, price, s_code, ymd)
    print(idx,cnt, s_name, s_code, price)
    
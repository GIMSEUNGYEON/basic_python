import urllib.request
from bs4 import BeautifulSoup as bs
client_id = "yjuqpVrHff18N74xlrWP"
client_secret = "p3b_AYdMN0"
encText = urllib.parse.quote("장원영")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = response.read()
# print(response_body.decode('utf-8'))

txt = response_body.decode('utf-8')

soup = bs(txt, "xml")

item = soup.select("channel item")[0]

print(item.select("title")[0].text)
print(item.select("link")[0].text)

print("====================================")

items = soup.find_all("item")
for i in items:
    print(i.find("title"))
    print(i.find("link"))
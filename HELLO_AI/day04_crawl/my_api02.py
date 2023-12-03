import urllib.request
import json
client_id = "yjuqpVrHff18N74xlrWP"
client_secret = "p3b_AYdMN0"
encText = urllib.parse.quote("장원영")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = response.read()
# print(response_body.decode('utf-8'))

txt = response_body.decode('utf-8')

# print(txt)
json_txt = json.loads(txt)
print(json_txt)
print(json_txt["items"])
print(json_txt.get("items")[0]["title"])
print(json_txt.get("items")[0].get("link"))
import http.client
from urllib.request import urlopen

response = urlopen("http://www.baidu.com") # type:http.client.HTTPResponse
# response = urlopen("http://www.github.com")
# response = urlopen("https://diannao.jd.com/")
# print(type(response))

baidu_str = response.read().decode()

print(baidu_str)

# with open("bai_du.html","w",encoding="utf8") as f:
# with open("github.html","w",encoding="utf8") as f:
# with open("jingdong.html","w",encoding="utf8") as f:
#     f.write(baidu_str)
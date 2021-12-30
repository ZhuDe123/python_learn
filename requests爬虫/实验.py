import requests
from urllib.request import urlopen
import http.client

header1 = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36"}

response = requests.get("https://www.baidu.com",headers = header1)

print(response.content.decode())

r = urlopen("http://baiwu.com") # type:http.client.HTTPResponse


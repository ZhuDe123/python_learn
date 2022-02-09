import requests

url = "https://fanyi.baidu.com/v2transapi"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

data = {
    "from": "en",
    "to": "zh",
    "query":"鸟",
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "882014.628335",
    "token": "8bdd5034d624215e53128066dbeb0ee5",
    "domain": "common"
}

response = requests.post(url,headers=headers,data=data)

print(response.content.decode())
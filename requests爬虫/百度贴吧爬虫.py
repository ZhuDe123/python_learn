import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36",
            "cookie": "PSTM=1638765459; BAIDUID=09F901C6E303B14527BE7417815FF89D:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_3334a7bedb8943055943242664fad80a1638779906958; BIDUPSID=AE41826A01C92FCFF84EDB8853E4F976; BDUSS=lMaW1CU2tsLUo5SGY0UXZnYUFpUzFDU1g1VXBGYkZqSDdzZ213flZNc3M3T2RoRUFBQUFBJCQAAAAAAAAAAAEAAAAOhBNPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACxfwGEsX8BhWG; BDUSS_BFESS=lMaW1CU2tsLUo5SGY0UXZnYUFpUzFDU1g1VXBGYkZqSDdzZ213flZNc3M3T2RoRUFBQUFBJCQAAAAAAAAAAAEAAAAOhBNPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACxfwGEsX8BhWG; H_WISE_SIDS=110085_127969_164869_176398_179346_182245_184441_184716_186635_186743_186840_187605_187828_188453_188744_189087_189254_189325_189731_189755_190474_190617_190791_191068_191246_191368_191810_192206_192237_192407_193040_193283_193348_193560_193756_194085_194130_194513_194519_194583_194998_195187_195342_195477_195540_195551_195592_195625_195632_195679_196045_196050_196230_196274_196275_196425_196754_196833_196838_196881_196939_197038_197096_197204_197226_197293_197552_197582_197669_197698_197711_197783_197973_198070_198123_198167_198189_198264_198327_198388_198430_198509_198580_198591_198649_198911_198998_199270_199284_199470; delPer=0; PSINO=1; BAIDU_WISE_UID=wapp_1640741236457_336; H_PS_PSSID=35638_34439_35106_35627_35456_34584_35491_35542_35644_35324_26350_35561; BA_HECTOR=a501al05012h00a4ni1gsng6q0r; ab_sr=1.0.1_Y2YyYWFiNjc0OTRiNDZkN2QzYTk2NTk2YTE2OWY4NGRkZjdlYTViMTA1ODBmY2I4NzcwYjRhNDRjMWE3ZmE5MzdhMDYwNjAyNGFmMWFlMmMyYmU4YWQ1NjdjYWQ0OWY4OTJiMjNiOWQ3NjA3Yjk3MGM1ZDkyMmQzZTY1ODQ0ZThhMDhhNDk5YmI2MjZhZGEwNWMzYTk2MDBjMjM5YmNmNDQ4ZDdiYjY4ZTcwY2Y0OGQzNTRiNzlhZDkzMzM2MjQx"
        }

    def get_url_list(self):
        # 构造url列表
        url_list = []
        for i in range(5):
            url_list.append(self.url_temp.format(i * 50))
        return url_list

    def parse_url(self, url):
        # 发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_number):
        file_path = "{0}--第{1}页.html".format(self.tieba_name, page_number)
        # 保存html字符串
        with open(file_path, "w", encoding="utf8") as f:  # 保存成“**-第1页”
            f.write(html_str)

    # 实现主要逻辑
    def run(self):

        # 1构造url列表
        url_list = self.get_url_list()
        # 遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_number = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_number)
            print(url)


if __name__ == '__main__':
    tieba = TiebaSpider("蓝牙")
    tieba.run()

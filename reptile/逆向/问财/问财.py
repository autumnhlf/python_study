import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='UTF-8')
# 上面的代码是用于js中有中文时，调用报错或者乱码（必须要放在最开头的地方）

import execjs

f = open("问财.js", mode="r", encoding="utf-8")
js_code = f.read()
# 先加载js代码
js = execjs.compile(js_code)
hexinv = js.call("rt.update")
# print(r)

import json
import requests

data = {
    "source": "Ths_iwencai_Xuangu",
    "version": "2.0",
    "query_area": "",
    "block_list": "",
    "add_info": {
        "urp": {
            "scene": 1,
            "company": 1,
            "business": 1
        },
        "contentType": "json",
        "searchInfo": True
    },
    "question": "20231025涨跌",
    "perpage": 50,
    "page": 1,
    "secondary_intent": "usstock",
    "log_info": {"input_type": "typewrite"},
    "rsh": "Ths_iwencai_Xuangu_ia3t37w35184mw0jkzlrsyn74bgr9dd9"
}

# print(r)

url = "https://www.iwencai.com/customized/chart/get-robot-data"
headers = {
    "Content-Type": "application/json",
    "Hexin-V": hexinv,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}

resp = requests.post(url=url, data=json.dumps(data), headers=headers)
print("resp.text", resp.text)

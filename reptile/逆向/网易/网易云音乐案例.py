import json
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen,encoding='UTF-8')
# 上面的代码是用于js中有中文时，调用报错或者乱码（必须要放在最开头的地方）

import execjs


# 准备参数
data = {
    "ids" : '[2083785152]',
    "level" : 'standard',
    "encodeType" : 'aac',
    "csrf_token" : ''
}
f = open("网易.js",mode="r",encoding="utf-8")
js_code = f.read()
# 先加载js代码
js = execjs.compile(js_code)
r = js.call("fnOne",data)
# print(r)
import requests
real_data = {
    "params":r['encText'],
    "encSecKey":r['encSecKey']
}
print(real_data)
url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}
resp = requests.post(url,data=real_data,headers=headers)
print(resp.text)

response=requests.post(url=url,data=real_data,headers=headers)
print("response.text",response.text)




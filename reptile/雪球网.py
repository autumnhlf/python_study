import requests
import random
url = 'https://xueqiu.com/'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
# 代理
proxy=[
    {'http':'113.124.94.2:9999'},
    {'http':'123.169.38.218:9999'},
    {'http':'114.231.8.116:8888'}
]

proxy = random.choice(proxy)
res = requests.get(url,headers=headers,proxies=proxy)
# 获取cookies
cookies = res.cookies
# print(dict(cookies))

url_api = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=529130&size=15'

res_api = requests.get(url_api,headers=headers,proxies=proxy,cookies=cookies)
print(res_api)
# 自动获取解码格式
# res.encoding = res.apparent_encoding
# data = res.text

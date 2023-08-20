import requests
import random

url_sesssion = 'https://xueqiu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
# 代理
proxy = [
    {'http': '113.124.94.2:9999'},
    {'http': '123.169.38.218:9999'},
    {'http': '114.231.8.116:8888'}
]

proxy = random.choice(proxy)

# 创建一个session对象
session = requests.session();
res_session = session.get(url_sesssion, headers=headers, proxies=proxy);

# 访问异步加载的地址 携带cookies
url_api = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=529130&size=15'

res = session.get(url_api, headers=headers, proxies=proxy);
print(res)
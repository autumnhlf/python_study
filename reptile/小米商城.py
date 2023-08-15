import random
import requests
from lxml import etree

url = 'https://app.mi.com/catTopList/0?page=1'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
# 代理
proxy=[
    {'http':'113.124.94.2:9999'},
    {'http':'123.169.38.218:9999'},
    {'http':'114.231.8.116:8888'}
]

proxy = random.choice(proxy)
res = requests.get(url,headers=headers,proxies=proxy)
# 自动获取解码格式
res.encoding = res.apparent_encoding
data = res.text
# print(data)
tree = etree.HTML(data)

img_list = tree.xpath('//ul[@class="applist"]/li/a/img/@data-src')
print(img_list)


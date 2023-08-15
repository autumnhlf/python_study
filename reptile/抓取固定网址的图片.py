import os.path
import time
import requests
from lxml import etree
import random


url = 'https://www.qqtn.com/article/article_335841_1.html'
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

# //*[@id="content"]
img_list = tree.xpath('//div[@id="content"]/p/img/@src')
print(img_list)

path = 'img'

if not os.path.exists(path):
    os.mkdir(path)
i = 0
for img in img_list:
    print(img)
    # 进行图片的请求   注意 要加上 ‘res = ’ 否则图片打不开
    res = requests.get(img,headers=headers,proxies=proxy)
    with open(os.path.join(path,str(i)+'.jpg'),'wb') as f:
        f.write(res.content)
    time.sleep(0.5)
    i+=1

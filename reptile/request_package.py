import os
import random
import time

import requests
from lxml import etree

# 通过链接获取页面
def getRequest(url,headerstype=False,proxytype=False):
    '''
    # 通过链接获取页面
    :param url:             页面url地址
    :param headerstype:     是否添加请求头
    :param proxytype:       是否添加代理
    :return:
    '''
    if headerstype:
        pc_agent = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
            "Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0"
        ]
        headers = {
            'User-Agent': random.choice(pc_agent)
        }
    else:
        headers = False
    if proxytype:
        # 代理
        proxy = [
            {'http': '222.74.73.202:42055'},
            {'http': '183.236.123.242:8060'},
            {'http': '182.34.36.17:9999'},
            {'http': '58.20.184.187:9091'},
            {'http': '221.236.167.178:9000'},
            {'http': '182.34.32.217:9999'}
        ]
        proxy = random.choice(proxy)
    else:
        proxy = False


    res = requests.get(url, headers=headers, proxies=proxy)
    # 自动获取解码格式
    res.encoding = res.apparent_encoding
    return res

def getHTML(url,xpathstr,headerstype=False,proxytype=False):
    '''
    # 获取页面html
    :param url:             页面url地址
    :param headerstype:     是否添加请求头
    :param proxytype:       是否添加代理
    :param xpathstr:        xpathstr
    :return:
    '''
    # 通过链接获取页面数据
    res = getRequest(url, headerstype, proxytype)


    data = res.text
    # print(data)
    tree = etree.HTML(data)
    # 获取数据
    datastr_list = tree.xpath(xpathstr)
    return datastr_list




# 将获取的图片资源存储到本地
def store_data(path,data_list):
    '''
    # 将获取的图片资源存储到本地
    :param path:             需要存储的路径
    :param data_list:        数据 img[0]:名称  img[1]:地址
    :return:
    '''
    # 判断路径是否存在，不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)

    for img in data_list:
        # 进行图片的请求   注意 要加上 ‘res = ’ 否则图片打不开
        res = getRequest(img['url'], True, True)
        with open(os.path.join(path, str(img['name']) + '.jpg'), 'wb') as f:
            f.write(res.content)
        time.sleep(0.5)
    return 'success'
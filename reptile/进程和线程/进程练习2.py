import time
import requests
from multiprocessing import Queue,Process
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

# 多进程抓取斗图

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

def get_img_src(url,q):
    '''
    进程1：负责提取页面中所有的img的下载地址
    将图片的下载地址通过队列，传输给另一个进程进行下载
    :param url:
    :param q:
    :return:
    '''

    resp = requests.get(url,headers=headers)
    tree = etree.HTML(resp.text)
    srcs = tree.xpath()
    for src in srcs:
        q.put(src.strip())
    resp.close()

def download_img(q):
    '''
    将图片的下载地址从队列中提取出来，进行下载
    :param q:
    :return:
    '''
    with ThreadPoolExecutor(20) as t:
        while 1:
            try:
                s = q.get(timeout=20)
                t.submit(download_one,s)
            except Exception as e:
                print(e)

def download_one():
    pass




















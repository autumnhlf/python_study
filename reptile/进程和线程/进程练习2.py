import os
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

def download_one(s):
    '''
    下载
    :param s:
    :return:
    '''
    resp = requests.get(s,headers=headers)
    file_name = s.split('/')[-1]
    # 创建文件夹  img
    path = 'img/斗图网'

    if not os.path.exists(path):
        os.mkdir(path)

    with open(f"img/{file_name}",mode="wb") as f:
        f.write(resp.content)
    print("一张图片下载完成！！！",file_name)
    resp.close()

if __name__ == '__main__':
    t1 = time.time()
    # 两个进程必须使用同一队列，否则数据传输不了
    q = Queue()
    p_list = []
    for i in range(1,11):
        url = f'https://www.pkdoutu.com/photo/list/?page={i}'
        p = Process(target=get_img_src,args=(url,q))
        p_list.append(p)
    for p in p_list:
        p.start()
    p2 = Process(target=download_img,args=(q,))
    p2.start()
    for a in p_list:
        p.join()
    p2.join()

    t2 = time.time()

    print((t2-t1)/60)





















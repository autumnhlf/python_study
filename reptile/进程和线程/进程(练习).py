import os
import random
from multiprocessing import Process,Queue
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import time
import requests

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
    'User-Agent': random.choice(pc_agent),
'Cookie':
'Hm_lvt_2fc12699c699441729d4b335ce117f40=1693050998; _agep=1693050998; _agfp=ee8a96eb8387679ae06076d23dcf3464; _agtk=2cdb2b2a2cb325b08aad764c2372795b; XSRF-TOKEN=eyJpdiI6InY0UTRFTmNHZHhmNlI2NGZHMmZaVVE9PSIsInZhbHVlIjoiQnBPcVNLdGpLcERpTEFiVHhQaXlXXC9tTE94dWNVMUFOSElDUnZvY1hBQjdPWWVMVmxlN0RMdTBpSTNPbFpMUzAiLCJtYWMiOiJmNDgyNjJjMTQxZDk5YzFmMDUwNTNiNWZkMzMzMDVmNDE5YzZkZTEyZTljNGIxODgxMWFhZWM5ZTkwOWZhOTdiIn0%3D; doutula_session=eyJpdiI6IlFZQjBwMGN0b2pOb2pIbWplbjVvXC93PT0iLCJ2YWx1ZSI6ImcxT25OWGsycHF6Umo2S1NSVWIyVUxjcUI2SkYyZDJGbDJ0cld5QStvNnd3eWFDelVVNDhFV3AwTjdBK2drOSsiLCJtYWMiOiIzOTM2ZWY1ZjNkYmM1NjBlZDkxZjQzOWU1ZTY0Y2ViYzg1NmI4YzZhY2YwZDA1ZWVmNDMxYjE0OGNlYTdjZmM0In0%3D; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1693059218'
}

# 代理
proxy=[
    {'http':'113.124.94.2:9999'},
    {'http':'123.169.38.218:9999'},
    {'http':'114.231.8.116:8888'}
]
proxya = random.choice(proxy)

def get_img_src(url,q):
    '''
    提取页面中数据
    :param url:
    :param q:
    :return:
    '''
    res = requests.get(url, headers=headers,proxies=proxya)
    tree = etree.HTML(res.text)
    img_list = tree.xpath('//div[@class="page-content text-center"]//img[@referrerpolicy="no-referrer"]/@data-backup')
    # xpathstr = '//div[@class="page-content text-center"]/div/a/img[1]/@src'
    # xpathstr = '//div[@class="page-content text-center"]//img[@referrerpolicy="no-referrer"]/@data-original'
    # xpathstr = '//div[@class="page-content text-center"]//img[@referrerpolicy="no-referrer"]/@data-backup'
    # img_list = getHTML(url, xpathstr, True, True)
    for img in img_list:
        q.put(img.strip())
    res.close()

def download_img(q):
    # 将获取的图片下载
    with ThreadPoolExecutor(10) as t:
        while 1:
            try:
                s = q.get(timeout=10)
                t.submit(download_one,s)

            except Exception as e:
                print(e)
                break

def download_one(s):
    # 下载
    res = requests.get(s,headers=headers,proxies=proxya)
    file_name = s.split('/')[-1]
    # 地址
    path = 'img/斗图网'
    # 判断路径是否存在，不存在则创建   只能创建最底层的目录，不能创建多级目录
    if not os.path.exists(path):
        os.mkdir(path)

    with open(os.path.join(path, str(file_name)), 'wb') as f:
    # with open(f'img/{file_name}',mode='wb',encoding='UTF-8') as f:
        f.write(res.content)
    print('一张图片下载完毕',file_name)
    res.close()

if __name__ == '__main__':
    t1 = time.time()
    q = Queue()

    p_list = []

    for i in range(1):
        url = f'https://www.pkdoutu.com/photo/list/?page={i}'
        p = Process(target=get_img_src,args=(url,q))
        p_list.append(p)
    for p in p_list:
        p.start()
    p2 = Process(target=download_img,args=(q,))
    p2.start()

    for p in p_list:
        p.join()
    p2.join()

    t2 = time.time()
    print('耗时：',t2-t1)











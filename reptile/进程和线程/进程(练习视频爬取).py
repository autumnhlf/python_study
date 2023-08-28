import os.path
import random
import re
import time

import requests
from concurrent.futures import ThreadPoolExecutor, wait

# 代理
proxy = [
    {'http': '114.231.46.233:8888'},
    {'http': '182.34.103.11:9999'},
    {'http': '113.121.36.114:9999'},
    {'http': '114.231.45.98:8888'},
    {'http': '182.34.18.25:9999'},
    {'http': '222.74.73.202:42055'}
]
proxy = random.choice(proxy)

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
'''

# session = requests.Session()
# session.get('https://www.99meiju.com/index.html',headers=headers)

url = 'https://www.99meiju.com/play/13198-4-0.html'

res = requests.get(url,headers=headers,proxies=proxy,verify=False)
res.encoding = 'UTF-8'
data = res.text
with open('jiujiu.html','w',encoding='UTF-8') as f:
    f.write(data)

'''


'''
with open('jiujiu.html','r',encoding='UTF-8') as f:
    data = f.read()
# now="https://v4.szjal.cn/20191003/emVicKUk/index.m3u8"
rese = re.search('now="(.+?index.m3u8)"',data).group(1)

print(rese)
res = requests.get(rese,headers=headers,proxies=proxy)
print(res.text)
with open('m3u8_one.text','w',encoding='UTF-8') as f:
    f.write(res.text)
'''
'''
with open('m3u8_one.text','r',encoding='UTF-8') as f:
    data = f.read()

str = data.split('/',1)[-1]
# https://b4.szjal.cn/ppvod/533395D95C9842A809F802487C178DAC.m3u8
url1 = 'https://b4.szjal.cn/'+str
res = requests.get(url1,headers=headers,proxies=proxy)
print(res.text)
with open('m3u8_two.text','w',encoding='UTF-8') as f:
    f.write(res.text)
'''
# 下载单个视频
def download_one_video(url,i,path):
    t1 = time.time()
    print(url,i,'开始下载')
    res = requests.get(url,headers=headers,proxies=proxy)
    with open(os.path.join(path,f'{i}.ts'),'wb')as f:
        f.write(res.content)
        t2 = time.time()
    print(url, i, '完成下载','耗时：',t2-t1)

def download_all_videos():
    path = 'ts'
    with open('m3u8_two.text','r',encoding='UTF-8') as f:
        data = f.readlines()
    # 创建线程池
    pool = ThreadPoolExecutor(20)
    tasks = []
    a = 0
    for i in data:
        # 提取视频的地址
        if i.startswith('#'):
            continue
        else:
            # 去除结尾的换行符
            url = 'https://b4.szjal.cn'+i.strip()
            print(url)
            tasks.append(pool.submit(download_one_video,url,a,path))
        a += 1
    # 集体等待线程执行完毕
    wait(tasks)

# 处理m3u8文件的url问题
def do_m3u8_url(path,m3u8_filename='m3u8_two.text'):
    # 这里还没处理key的问题
    if not os.path.exists(path):
        os.mkdir(path)

    with open(m3u8_filename,mode='r',encoding='UTF-8')as f:
        data = f.readlines()

    fw = open(os.path.join(path,m3u8_filename),'w',encoding='UTF-8')
    abs_path = os.getcwd()
    i=0
    for line in data:
        if line.startswith('#'):
            fw.write(line)
        else:
            fw.write(f'{abs_path}/{path}/{i}.ts\n')
            i+=1



def merge(path,filename='output'):
    '''
    进行ts文件合并 解决视频音频不同步的问题
    :param filePath:
    :param filename:
    :return:
    '''
    # 根据当前文件名排序
    # file_list = sorted(os.listdir(filePath),key=lambda x:int(x.split('.')[0]))
    # # print(file_list)
    #
    # str = '|'.join([f'{filePath}/{i}' for i in file_list]).strip('|')
    # cmd = f'ffmpeg -i "concat:{str}" -c copy -bsf:a aac_adtstoasc -movflags +faststart {filename}.mp4'
    # os.system(cmd)
    os.chdir(path)
    cmd = f'ffmpeg -i index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)

if __name__ == '__main__':
    # download_all_videos();
    # do_m3u8_url('ts')
    path = 'ts'
    merge(path,'越狱')




















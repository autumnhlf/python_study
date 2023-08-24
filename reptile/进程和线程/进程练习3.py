import urllib.request
import urllib.parse
import json
from multiprocessing import Process


# 肯德基
import requests
def get_kfc(num):

    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    form_data={
        'cname':'',
        'pid':'',
        'keyword':'南京',
        'pageIndex':num,
        'pageSize':10,
    }
    # 对表单数据转码
    formdata = urllib.parse.urlencode(form_data).encode('UTF-8')
    # 发送post请求
    res = urllib.request.Request(url,data=formdata,headers=headers)
    response = urllib.request.urlopen(res)
    # 返回json数据，转换为字典
    data = json.loads(response.read().decode('UTF-8'))
    for i in data['Table1']:
        print(i)


if __name__ == '__main__':
    for i in range(1,5):
        Process(target=get_kfc,args=(i,)).start()


















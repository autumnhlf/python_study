import re
import time

import requests
from reptile.request_package import getHTML

def printstr(datastr_list):
    for datastr in datastr_list:
        print(datastr.xpath('./span[1]/text()'), end='--')
        print(datastr.xpath('./span[2]/text()'), end='--')
        print(datastr.xpath('./span[3]/text()'), end='--')
        print(datastr.xpath('./span[4]/text()'), end='--')
        print(datastr.xpath('./span[5]/text()'))


url = 'http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index.html'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
res = requests.get(url,headers=headers)
# 自动获取解码格式
res.encoding = res.apparent_encoding
data = res.text
# xpathstr = '//ul[@class="list-con"]/li'
# datastr_list = getHTML(url,xpathstr,True,True)
# printstr(datastr_list)

til_num = int(re.search(r'var countPage = (.*?)//共多少页',data).group(1))
tol_num = int(re.search(r'var countPage = (?P<page>\d+)//共多少页',data).group('page'))



for a in range(3):
    page_num = input('请输入要抓取的页码：')
    if bool(page_num)==False:
        if a == 2:
            print('对不起，你的机会已使用完！')
        else:
            print(f'请输入正确的页码，你的机会还有{2 - a}次')
        continue
    else:
        page_num = int(page_num)
        if page_num <= 0 or page_num > tol_num:
            if a == 2:
                print('对不起，你的机会已使用完！')
            else:
                print(f'请输入正确的页码，你的机会还有{2 - a}次')
            continue
        if (page_num > 0 and page_num <= tol_num):
            # 循环
            for i in range(page_num):
                # 第一页和其他页面地址不一样，需要区分
                if i == 0:
                    url = f'http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index.html'
                else:
                    url = f'http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index_{i}.html'

                # xpath
                xpathstr = '//ul[@class="list-con"]/li'
                # 获取数据
                datastr_list = getHTML(url, xpathstr, True, True)
                # 打印数据
                printstr(datastr_list)
                time.sleep(1)
            break









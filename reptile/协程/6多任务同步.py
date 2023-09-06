import time


def run(url):
    print(f'开始请求{url}的数据')
    time.sleep(2)
    print(f'结束请求{url}的数据')
    data = url + '的抓取数据'
    return data


if __name__ == '__main__':
    url_list = ['douyin','baidu','guge']
    for i in url_list:
        run(i)

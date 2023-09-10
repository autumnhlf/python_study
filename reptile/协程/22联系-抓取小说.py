import asyncio
import os.path

import aiofiles
import aiohttp
from bs4 import BeautifulSoup
import requests


def get_page_source(url):
    '''
    返回html页面
    :param url:
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding='UTF-8'
    return response.text


def parse_page_source(source):
    '''
    解析读取页面
    :param source:
    :return:
    '''
    book_list = []
    soup = BeautifulSoup(source,'html.parser')
    a_list = soup.find_all('div',attrs={'class':'mulu-list quanji'})
    for a in a_list:
        a_list = a.find_all_next('a')
        for href in a_list:
            chapter_url = href['href']
            book_list.append(chapter_url)
    return book_list


def get_book_name(book_page):
    book_num = book_page.split('/')[-1].split('.')[0]
    book_chapter_name = book_page.split('/')[-2]
    return book_num,book_chapter_name


async def aio_download_one(chapter_url, signal):
    number,c_name = get_book_name(chapter_url)
    # 如果出现异常，会重新请求十次，有一次成功就行
    for c in range(10):
        try:
            # 控制协程的并发数量
            async with signal:
                async with aiohttp.ClientSession() as session:
                    async with session.get(chapter_url)as resp:
                        page_source = await resp.text()
                        soup = BeautifulSoup(page_source,'html.parser')
                        chapter_name = soup.find('h1').text
                        p_content = soup.find('div',attrs={'class':'neirong'}).find_all('p')
                        content = [p.text+'\n' for p in p_content]
                        chapter_content = '\n'.join(content)
                        if not os.path.exists(f'{book_name}/{c_name}'):
                            os.makedirs(f'{book_name}/{c_name}')
                        async with aiofiles.open(f'{book_name}/{c_name}/{number}/{chapter_name}.txt',mode="w",encoding='UTF-8' )as f:
                            await f.write(chapter_content)
                        print(chapter_url,'下载success')
                        return ''
        except Exception as e:
            print(e)
            print(chapter_url,'下载faild,正在重试')
    return chapter_url



async def aio_download(href_list):
    tasks = []
    # 开启并发控制10
    semapore = asyncio.Semaphore(10)
    for h in href_list:
        tasks.append(asyncio.create_task(aio_download_one(h,semapore)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    url = 'https://www.51shucheng.net/daomu/guichuideng'
    book_name = 'guichuideng'
    if not os.path.exists(book_name):
        os.makedirs(book_name)
    source = get_page_source(url)
    href_list = parse_page_source(source)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aio_download(href_list))
    loop.close()

# D:\Personal\git\python\study\reptile\协程\guichuideng
# D:\Personal\git\python\study\reptile\协程\guichuideng/huangpizifen/2668/第34章
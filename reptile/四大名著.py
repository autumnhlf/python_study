import os
import random
import time
import re
from bs4 import BeautifulSoup

from reptile.request_package import getRequest, getHTML


# url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
#
# res = getRequest(url,True,True)
#
# soup = BeautifulSoup(res.text,'lxml')
#
# div = soup.find_all('div',class_='book-item')
#
# for i in div:
#     # print(i.text.replace('\n',''))
#     # print(i.get_text().replace('\n',''))
#     name = i.get_text().replace('\n', '')
#     href = 'https://www.shicimingju.com' + i.a['href']
#     print(name,end=' ')
#     print(href)





# https://www.shicimingju.com/book/sanguoyanyi.html

def get_html(url):
    res = getRequest(url, True, True)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def get_book(soup):
    div = soup.find_all('div', class_='book-item')
    # 存储书的字典{书名：书链接}
    book_dict = {}
    for i in div:
        name = i.get_text().replace('\n', '')
        href = 'https://www.shicimingju.com' + i.a['href']
        text = re.sub('《|》', '', name)
        book_dict[text] = href
    return book_dict

def get_book_detail(book_html):
    '''
    获取四大名著章节 标题 href
    :param book_html: 当前章节的html内容
    :return:
    '''
    div = book_html.find_all('div',class_='book-mulu')
    mulu_dict = {}
    for i in div:
        mulu_hrefs = i.find_all('a')
        for a in mulu_hrefs:
            # 获取章节标题
            name = a.get_text()
            # 获取章节url
            href = a['href']
            mulu_dict[name] = 'https://www.shicimingju.com' + href
    return mulu_dict
    # xpathstr = '//div[@class="book-mulu"]/ul/li/a/text()'
    # img_list = getHTML(book_url, xpathstr, True, True)
    # for i in img_list:
    #     print(i)

def get_book_chapter_detail(chapter_title,chapter_html):
    dict = {}
    div = chapter_html.find('div', class_='chapter_content')
    text = div.text
    dict[chapter_title]=text
    return dict;

def save_contents(title,book_contents,book_path):
    '''
    存储文本文件
    :param title: 章节名称
    :param book_contents: 内容
    :param book_path: 路径
    :return:
    '''
    # 判断路径是否存在，不存在则创建
    if not os.path.exists(book_path):
        os.mkdir(book_path)

    for c in book_contents:
        path = os.path.join(book_path,title+'.text')
        with open(path,'a',encoding='UTF-8') as f:
            f.write(book_contents[c])
            print(f"{title}下载完成！！！")




if __name__ == '__main__':
    url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
    books = get_book(get_html(url))
    for book_name in books:
        book_url = books[book_name]
        book_html = get_html(book_url)
        book_dict = get_book_detail(book_html)
        for title,url in book_dict.items():
            # 获取具体章节内容
            contents = get_book_chapter_detail(title,get_html(url))
            # 存储路径
            path = 'text/'+book_name
            # 下载
            save_contents(title,contents,path)
            time.sleep(random.randint(1,3))



# https://www.shicimingju.com/book/sanguoyanyi/1.html
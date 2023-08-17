import requests

url='https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=40&count=20&selected_categories=%7B%22%E7%B1%BB%E5%9E%8B%22:%22%22,%22%E5%9C%B0%E5%8C%BA%22:%22%22%7D&uncollect=false&tags=&playable=true'
headers = {
'Referer':'https://movie.douban.com/explore',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
# 代理
proxy=[
    {'http':'113.124.94.2:9999'},
    {'http':'123.169.38.218:9999'},
    {'http':'114.231.8.116:8888'}
]

res = requests.get(url, headers=headers, proxies=False)
items = res.json()['items']
# print(items)

for i in items:
    # 封面
    img = i['pic']['large']
    # 标题
    title = i['title']
    # 评论
    comment = i['comment']['comment']
    # id
    id = i['id']

    
    print(img,end='  ---  ')
    print(title,end='  ---  ')
    print(comment)

# https://movie.douban.com/subject/34925298/
# https://movie.douban.com/subject/26636816/


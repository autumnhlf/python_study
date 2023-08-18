from reptile.request_package import getHTML, store_data

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

xpathstr = '//div[@class="book-mulu"]/ul/li/a/text()'
img_list = getHTML(url,xpathstr,True,True)

for i in img_list:
    print(i)

from reptile.request_package import getHTML, store_data

url = 'https://pic.netbian.com'
xpathstr = '//ul[@class="clearfix"]/li/a/span/img'
img_list = getHTML(url,xpathstr,True,True)
list = []
for img in img_list:
    src = url + str(img.xpath('@src')[0])
    alt = img.xpath('@alt')[0]
    print(src,end=" --- ")
    print(alt)
    dict = {
        'name':alt,
        'url':src
    }
    list.append(dict)

path='img'
# 将图片信息储存到本地  这边添加时加了 time.sleep
a = store_data(path,list)
print(a)
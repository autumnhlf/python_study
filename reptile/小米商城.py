from reptile.request_package import getHTML


url = 'https://app.mi.com/catTopList/0?page=1'
xpathstr = '//ul[@class="applist"]/li/a/img/@data-src'
img_list = getHTML(url,xpathstr,True,True)

for img in img_list:
    print(img)
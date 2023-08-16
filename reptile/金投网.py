from reptile.request_package import getHTML

url = 'https://cang.cngold.org/c/2022-06-14/c8152503.html'
xpathstr = '//table[@border="1"]/tbody/tr'

datastr_list = getHTML(url,xpathstr,True,True)
i = 1;
for datastr in datastr_list:
    if(i!=1):
        print(datastr.xpath('./td[1]/text()'), end='--')
        print(datastr.xpath('./td[2]/text()'), end='--')
        print(datastr.xpath('./td[3]/text()'))
    i+=1
    # print(datastr.xpath('./td[1]/text()')+','+ datastr.xpath('./td[2]/text()')+','+datastr.xpath('./td[3]/text()'))
# print(datastr_list)
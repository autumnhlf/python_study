import scrapy


# 声明了一个类，继承scrapy的Spider
class XiaoyouxiSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'xiaoyouxi'
    # 你当前这个爬虫允许访问的域名是什么， 只要不符合下面这个规则的域名的url,scrapy自动帮你屏蔽
    allowed_domains = ['4399.com']
    # 起始url,第一个要访问的url
    start_urls = ['http://4399.com/']


    # 下面的parse是默认的解析数据位置 -》主要负责第一个url的解析工作
    def parse(self, response):
        # print(response.text)

        li_list = response.xpath("//div[@class='tm_fun h_3 ']/ul/li")
        data_list=[]
        for i in li_list:
            name = i.xpath('./a/text()').extract_first()
            img = i.xpath('./a/img/@lz_src').extract_first()
            # data_list.append(name,'https:'+img)
            # 可以返回数据，而不打断函数的执行 比return好
            yield {
                "name":name,
                "imgurl":'https:'+img
            }




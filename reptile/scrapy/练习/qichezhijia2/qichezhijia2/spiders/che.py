import scrapy
# 连接提取器
from scrapy.linkextractors import LinkExtractor
from scrapy import Request


class CheSpider(scrapy.Spider):
    name = 'che'
    allowed_domains = ['che168.com']
    start_urls = ['http://www.che168.com/nanjing/list/#pvareaid=100945']

    def parse(self, response, **kwargs):
        print(response.url)
        if response.url != 'http://www.che168.com/cheerror.html':
            href_list = LinkExtractor(restrict_xpaths=(".//div[@id='listpagination']/a"))
            hrefs = href_list.extract_links(response)
            for a in hrefs:
                # print(a.url)
                yield Request(url=a.url, callback=self.parse)
        # 1 获取每个详情页的url 访问
        # 连接提取器
        # 创建一个提取器
        # le = LinkExtractor(restrict_xpaths=("//ul[@class='viewlist_ul']/li/a"))
        # links = le.extract_links(response)
        # for i in links:
        #     print(i.url,i.text) #打印一个对象时，实际上在执行它的__repr__或者__str__
        #
        #     yield Request(i.url,callback=self.callback_detail)

        # 2 获取分页的url 访问
        # href_list = LinkExtractor(restrict_xpaths=(".//div[@id='listpagination']/a"))
        # hrefs = href_list.extract_links(response)
        # for a in hrefs:
        #     # print(a.url)
        #     yield Request(url=a.url, callback=self.parse)

    def callback_detail(self,res,**kwargs):
        name = res.xpath("//h3[@class='car-brand-name']/text()").extract_first()
        print(name)


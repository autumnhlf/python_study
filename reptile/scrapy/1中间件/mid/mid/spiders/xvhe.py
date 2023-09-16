import scrapy


class XvheSpider(scrapy.Spider):
    name = 'xvhe'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response,**kwargs):
        res = response.xpath(".//title//text()").extract()
        print(res)

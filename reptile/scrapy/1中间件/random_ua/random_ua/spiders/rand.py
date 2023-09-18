import scrapy


class RandSpider(scrapy.Spider):
    name = 'rand'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print(response.request.headers['User-Agent'])

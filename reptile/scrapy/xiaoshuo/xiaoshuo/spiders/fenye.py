import scrapy
from scrapy import Request
from urllib.parse import urljoin


class FenyeSpider(scrapy.Spider):
    name = 'fenye'
    allowed_domains = ['17k.com']
    start_urls = ['https://www.17k.com/all/book/2_0_0_0_0_0_0_0_1.html']

    # start_requests() 在爬虫开始的时候，给引擎传递第一个请求对象
    # 可以自己随意更改第一个请求的设计逻辑
    # def start_requests(self):
    #     for i in range(1,23):
    #         url = f'https://www.17k.com/all/book/2_0_0_0_0_0_0_0_{i}.html'
    #         yield Request(url)


    def parse(self, response,**kwargs):
        print(response.url)
        # name_list = response.xpath("//td[@class='td3']/span/a/text()").extract()
        # for i in name_list:
        #     print(i)


        # table_list = response.xpath("//tbody/tr[@class='bg0' or @class='bg1']")
        #
        # for i in table_list:
        #
        #     name = i.xpath("./td[@class='td3']//text()").extract()
        #     a = "".join(name).strip()
        #     print(a)

        a_list = response.xpath("//div[@class='page']/a")
        for a in a_list:
            href = a.xpath("./@href").extract_first()
            if href.startswith('javascript'):
                continue
            # print(href)
            url = response.urljoin(href)
        #     print(href,url)
            # 拼接url
            # url = urljoin(response.url, href)
            # print(url,href)
            # scrapy的调度器中有一个过滤器，可以去除重复的url
            # 如果不需要调度器的过滤行为 dont_filter=True
            yield Request(url,callback=self.parse)

















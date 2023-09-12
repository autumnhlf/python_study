import scrapy


class NameSpider(scrapy.Spider):
    name = 'name'
    allowed_domains = ['4399.com']
    start_urls = ['http://4399.com/']

    def parse(self, response):
        li_list = response.xpath("//div[@class='tm_fun h_3 ']/ul/li")
        for i in li_list:
            name = i.xpath('./a/text()').extract_first()

            # data_list.append(name,'https:'+img)
            # 可以返回数据，而不打断函数的执行 比return好
            yield {
                "name": name,
            }
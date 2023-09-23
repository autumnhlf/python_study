from scrapy import Request

import scrapy


class CheSpider(scrapy.Spider):
    name = 'che'
    allowed_domains = ['che168.com']
    start_urls = ['http://www.che168.com/nanjing/list/#pvareaid=100945']

    def parse(self, response,**kwargs):
        print(response.url)
        # print(response.text)
        res = response.xpath("//ul[@class='viewlist_ul']/li")
        for i in res:
            # print(i)

            href = i.xpath("./a/@href").extract_first()
            href_url = response.urljoin(href)
            # name = i.xpath("./a/div/img/@alt").extract_first()
            # url = i.xpath("./a/div/img/@src").extract_first()
            # img_url = response.urljoin(url)
            # print(href_url)

            # 发送请求到详情页
            yield Request(href_url,callback=self.callback_detail)
        href_list = response.xpath("//div[@id='listpagination']/a/@href").extract()
        for a in href_list:
            if a.startswith('javascript'):
                continue
            page_url = response.urljoin(a)

            yield Request(url=page_url,callback=self.parse)
            # print("page_url",page_url)

    def callback_detail(self,res,**kwargs):

        print("地址",res.url)
        name = res.xpath("//h3[@class='car-brand-name']/text()").extract_first()
        # 判断是否为空
        # any  如果队列中任何一个为真，就是真  ===》or
        # all  如果队列中任何一个为假，就是假  ===》and
        if any([name]):
            if name:
                name = name.strip()
            print(f"{name}===>>{res.url}")


        # if name is not None :
        #     print(f"{name}===>>{res.url}")

        # if(name=='none'):
        #     return
        #
        # if(name.strip()==''):
        #     name = res.xpath("//h3[@class='car-brand-name']/text()").extract()[1].strip()
        # else:
        #     name = name.strip()
        # print(f"{name}===>>{res.url}")



























import scrapy


class ShuangseqiuSpider(scrapy.Spider):
    name = 'shuangseqiu'
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://view.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs&type=50&dpc=1']

    def parse(self, response,**kwargs):
        res = response.xpath("//tbody[@id='cpdata']/tr")
        for i in res:
            # extract_first
            riqi = i.xpath("./td[1]/text()").extract_first()
            lan = i.xpath("./td[@class='chartball02']/text()").extract_first()


            # redNumstr = i.xpath("./td[@class='chartball01' or @class='chartball20']")
            # aa.append(datastr)
            # for a in redNumstr:
            #     str = a.xpath("./text()").extract_first()
            #     aa.append(str)
            hong = i.xpath("./td[@class='chartball01' or @class='chartball20']/text()").extract()

            # 存储数据
            # 将数据返给管道
            yield {
                "riqi":riqi,
                "hong": hong,
                "lan": lan,

            }




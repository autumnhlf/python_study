import scrapy
from urllib.parse import urljoin
from scrapy.http.request import Request


class JiaSpider(scrapy.Spider):
    name = 'jia'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/shouchaobao/']

    def parse(self, response,**kwargs):
        print(response.url)
        li_list = response.xpath("//ul[@class='pic-list2  clearfix']/li")
        # print(li_list)
        for li in li_list:

            href = li.xpath("./a/@href").extract_first()
            if href.endswith(".exe"):
                continue

            src = li.xpath("./a/img/@src").extract_first()
            name = li.xpath("./a/img/@alt").extract_first()

            # 拼接url
            url = urljoin(response.url,href)
            print(href,url, name, src)
            # 请求 发出去 ，必须走引擎-》调度器-》引擎-》下载器
            # scrapy发送请求的固定逻辑，此时这个请求出去了 回来之后
            # 如果没有其他的参数的话，也会自定调用parse
            # 告诉引擎这个请求发出后，回调地址
            yield Request(url,callback=self.callback_two)

    def callback_two(self,res,**kwargs):
        # 处理详情页数据
        img_url = res.xpath("//img[@id='bigImg']/@src").extract_first()
        # print('详情页',img_url)
        # 将图片交给管道保存
        yield {
            "img_url":img_url
        }





# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 爬虫中间件
class MidSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# 下载中间件
class MidDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    # 它是scrapy引擎在使用这个类的时候 是需要创建该类的对象的
    # 引擎在创建你需要的这个类的对象的时候 不是常规的 类名()
    # 而是通过调用类中的from_crawler来创建对象的
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        # 引擎 信号 连接
        crawler.signals.connect(s.zhangsan, signal=signals.spider_opened)
        # 上面代码逻辑是：在spider_opened的时候，自动运行spider_opened

        crawler.signals.connect(s.lisi, signal=signals.spider_closed)

        return s

    # process 处理
    # request 请求
    # 被执行的时机：请求从引擎到下载器之前
    def process_request(self, request, spider):
        print("我是process_request，我在发送请求的时候，你能看见我")
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: 不对请求做拦截，继续向后执行
        # - return 响应对象 不走下载器了，直接返回响应内容了，不走下载器
        # - return 请求对象  会给引擎传递一个请求对，不走下载器

        return None

    # process 处理
    # response 响应
    # 被执行的时机：响应从下载器到引擎之前
    def process_response(self, request, response, spider):
        print("我是process_response，我在响应回来之后，你能看见我")
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object 正常情况
        # - return a Request object  返回一个请求对象，给引擎一个请求对象
        # - or raise IgnoreRequest
        return response

    # 处理错误
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def zhangsan(self, spider):
        print('我是张三')
        spider.logger.info('Spider opened: %s' % spider.name)
    def lisi(self, spider):
        print('我是李四')
        spider.logger.info('Spider opened: %s' % spider.name)

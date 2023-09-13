# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request


# class TupianPipeline:
#     def process_item(self, item, spider):
#         return item

# scrapy提供的图片下载功能
class imgPipeline(ImagesPipeline):


    # 更换以下内容
    def get_media_requests(self, item, info):# 用于发送网络请求
        img_url = item['img_url']
        # 请求对象传值的最佳方案：meta
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Referer":"https://desk.zol.com.cn/shouchaobao/"
        }
        yield Request(img_url,headers=header,meta={"zhoujielun":img_url})

    # 完成路径处理
    def file_path(self, request, response=None, info=None, *, item=None):
        #需要返回文件路径的字符串
        zhoujielun = request.meta['zhoujielun']
        file_path = zhoujielun.split('/')[-1]
        return f"fengjun/img/{file_path}"

    def item_completed(self, results, item, info):
        # 最后收尾工作
        return item



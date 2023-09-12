# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 管道  管道的使用必须在setting里面开启
class YouxiPipeline:
    # item 数据
    # process 处理
    def process_item(self, item, spider):
        print('我是管道，看到的东西：',item)
        with open("data.csv",mode="a",encoding="UTF-8")as f:
            f.write(f"{item['name']},{item['imgurl']}\n")

        return item

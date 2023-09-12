# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DayouxiPipeline:
    def process_item(self, item, spider):
        print('我是DayouxiPipeline管道，看到的东西：', item)
        with open("aaa.csv", mode="a", encoding="UTF-8") as f:
            f.write(f"{item['name']}\n")
        # 将数据传给下个管道
        return item

class VipPipeline:
    def process_item(self, item, spider):
        print('我是VipPipeline管道，看到的东西：', item)
        with open("aaa.csv", mode="a", encoding="UTF-8") as f:
            f.write(f"{item['name']}\n")
        # 将数据传给下个管道
        return item


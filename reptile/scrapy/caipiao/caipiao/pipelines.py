# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class CaipiaoPipeline:

    def open_spider(self,spider):
        print('open')
        self.f = open("caipiao2.csv", mode="a", encoding="UTF-8")

    def close_spider(self,spider):
        self.f.close()
        print('close')

    def process_item(self, item, spider):
        with open("caipiao3.csv",mode="a",encoding="UTF-8")as f:
            f.write(f"{item['riqi']},{item['hong']},{item['lan']}\n")
        self.f.write(f"{item['riqi']},{item['hong']},{item['lan']}\n")
        self.f.write(item['riqi'])
        self.f.write(",")
        self.f.write("_".join(item['hong']))
        self.f.write(item['lan'])
        self.f.write("\n")
        return item


class CaipiaoPipeline_MYSQL:
    def open_spider(self, spider):
        # 1 建立连接
        self.conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",database="v2ex")


    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):

        try:
            # 2 游标
            cur = self.conn.cursor()
            # 3 写入数据
            sql = "INSERT INTO caipiao( riqi, hong, lan) VALUES ( %s, %s, %s)"
            cur.execute(sql,(item['riqi'],"_".join(item['hong']),item['lan']))
            # 4 提交事务
            self.conn.commit()
        except Exception as e:
            print(e)
            # 5如果报错，回滚
            self.conn.rollback()

        print('success')
        return item

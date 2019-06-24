# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .settings import *

class LjspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(
            MYSQL_HOST, MYSQL_USER, MYSQL_PWD,
            MYSQL_DB, charset=MYSQL_CHAR
        )
        self.cursor = self.db.cursor()
    def process_item(self,item,spider):
        ins = 'insert into ljtable values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        List = [
            item['title'].strip(),
            item['familyname'].strip(),
            item['housestyle'].strip(),
            item['size'].strip(),
            item['direction'].strip(),
            item['renovation'].strip(),
            item['lift'].strip(),
            item['address'].strip(),
            item['price'].strip(),
            item['unit_price'].strip()
        ]
        self.cursor.execute(ins,List)
        self.db.commit()
        return item
    def close_mysql(self,spider):
        self.cursor.close()
        self.db.close()


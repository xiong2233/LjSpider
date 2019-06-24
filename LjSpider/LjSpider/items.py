# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #标题
    title = scrapy.Field()
    #小区名
    familyname = scrapy.Field()
    #房屋样式
    housestyle = scrapy.Field()
    #房屋大小
    size = scrapy.Field()
    #房屋朝向
    direction = scrapy.Field()
    #装修状况
    renovation = scrapy.Field()
    #有无电梯
    lift = scrapy.Field()
    #地址
    address = scrapy.Field()
    #价格
    price = scrapy.Field()
    #单价
    unit_price = scrapy.Field()


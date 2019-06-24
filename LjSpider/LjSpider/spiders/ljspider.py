# -*- coding: utf-8 -*-
import scrapy
from LjSpider.items import LjspiderItem


class LjspiderSpider(scrapy.Spider):
    name = 'ljspider'
    allowed_domains = ['cq.lianjia.com']
    start_urls = ['https://cq.lianjia.com/ershoufang/']
    baseurl = 'https://cq.lianjia.com/ershoufang/'

    def parse(self, response):
        for i in range(100):
            url = self.baseurl + "pg" + str(i+1)
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parse_one_link
            )
    def parse_one_link(self,response):
        rel = response.xpath('//ul[@class="sellListContent"]//li//div[@class="info clear"]')
        print(len(rel))
        for info in rel:
            item = LjspiderItem()
            item['title'] = info.xpath('./div[@class="title"]//a/text()').extract()[0]
            item['familyname'] = info.xpath('./div[@class="address"]//div[@class="houseInfo"]//a/text()').extract()[0]
            infoall = info.xpath('./div[@class="address"]//div[@class="houseInfo"]/text()').extract()[0]
            list = infoall.split('|')
            item['housestyle'] = list[1]
            item['size'] = list[2]
            item['direction'] = list[3]
            item['renovation'] = list[4]
            if len(list) == 6:
                item['lift'] = list[5]
            else:
                item['lift'] = "暂无数据"
            first = info.xpath('./div[@class="flood"]//div[@class="positionInfo"]/text()').extract()[0]
            second = info.xpath('./div[@class="flood"]//div[@class="positionInfo"]//a/text()').extract()[0]
            item['address'] = first + second
            item['price'] = info.xpath('./div[@class="priceInfo"]//div[@class="totalPrice"]//span/text()').extract()[0] + "万"
            item['unit_price'] = info.xpath('./div[@class="priceInfo"]//div[@class="unitPrice"]//span/text()').extract()[0]
            yield item


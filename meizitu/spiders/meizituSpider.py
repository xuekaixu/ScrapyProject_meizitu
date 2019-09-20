# -*- coding: utf-8 -*-
import scrapy
from meizitu.items import MeizituItem
from scrapy.crawler import CrawlerProcess


class meizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = []
    start_urls = ['http://www.meizitu.net.cn']

    def parse(self, response):
        item = MeizituItem()
        item['image_urls'] = response.xpath('//img//@src').extract()
        yield item
        new_url = response.xpath('.//li[@class="next"]//@href').extract_first()
        if new_url:
            yield scrapy.Request(new_url, callback=self.parse)


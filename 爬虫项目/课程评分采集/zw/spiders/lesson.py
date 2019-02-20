# -*- coding: utf-8 -*-
import scrapy
from zw.items import ZwItem
from scrapy.http import Request


class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        item=ZwItem()
        item["title"]=response.xpath("//ol[@class='breadcrumb']/li[@class='active']/text()").extract()
        item["link"]=response.xpath("//ul[@class='nav nav-tabs']/li[@class='active']/a/@href").extract()
        item["stu"] = response.xpath("//span[@class='course-view']/text()").extract()
        yield  item
        for i in range(2,9):
            url='https://edu.hellobi.com/course/'+str(i)
            yield Request(url,callback=self.parse)


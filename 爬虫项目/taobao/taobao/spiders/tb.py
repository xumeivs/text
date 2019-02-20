# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from taobao.items import TaobaoItem
import re
import urllib.request


class TbSpider(CrawlSpider):
    name = 'tb'
    allowed_domains = ['taobao.com']

    start_urls = ['http://www.jd.com/']
    heard = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        try:

            item = TaobaoItem()
            #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()
            thisurl=response.url
            pat='item.jd.com/(.*?).html'
            id=re.search(pat,thisurl)
            if(x):
                id=re.compile(pat).findall(thisurl)[0]
                title=response.xpath('//html/head/title/text()').extact()
                print(id)
                print(title)
            else:
                pass
        except Exception as e:
            print(e)
        return item
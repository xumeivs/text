# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import urllib.request
from baike.items import BaikeItem

class BkSpider(CrawlSpider):
    name = 'bk'
    allowed_domains = ['baike.baidu.com']
    header={'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    start_urls = ['http://baike.baidu.com/']


    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        try:
            item = BaikeItem()
            thisurl=response.url
            pat='https://baike.baidu.com/item/(.*?)'
            x=re.search(pat,thisurl)
            if(x):
                data=urllib.request.urlopen(thisurl).read().decode('utf-8')
                pat2='<h1 >(.*?)</h1>'
                item['id']=re.compile(pat2).findall(data)[0]
                item['ciurl']='https://baike.baidu.com/item/'+str(item['id]'])
            else:
                pass
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
            return item
        except Exception as e:
            print(e)

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib.request
from fenxi.items import FenxiItem
import re
import pymysql

class FxSpider(CrawlSpider):
    name = 'fx'
    allowed_domains = ['doubannv.net']
    header={'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    start_urls = ['http://www.doubannv.net/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        try:
            item = FenxiItem()
            thisurl=response.url
            pat='http://www.doubannv.net/group/(.*?).html'
            x=re.search(pat,thisurl)
            if(x):
                id=re.compile(pat).findall(thisurl)[0]
                commenturl='http://www.doubannv.net/e/public/ViewClick/?classid=1&id='+str(id)+'&addclick=1'
                pat2="'(.*?)'"
                upurl='http://www.doubannv.net/e/public/ViewClick/digg.php?classid=1&id='+str(id)+'&down=5'
                pat3="'(.*?)'"
                data=urllib.request.urlopen(commenturl).read().decode('utf-8','ignore')
                data2=urllib.request.urlopen(upurl).read().decode('utf-8','ignore')
                comment=re.compile(pat2).findall(data)
                up=re.compile(pat2).findall(data2)
                #print(id)
                #print(comment)
                #print(up)

                for i in range(0,len(id)):
                    for j in range(0,len(comment)):
                        comment=comment[j]
                        for z in range(0,len(up)):
                            up=up[z]
                            conn=pymysql.connect(host='127.0.0.1',user='root',passwd='13579zheng',db='douban',charset='utf8')
                            sql="insert into `fx`(`id`,`comment`,`up`)values('"+id+"','"+comment+"','"+up+"')"
                            conn.query(sql)
                        conn.commit()
                    conn.close()
                    print('ok')

            else:
                pass

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
            return item
        except Exception as e:
            print(e)

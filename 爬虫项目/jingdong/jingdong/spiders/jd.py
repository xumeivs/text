# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import  re
import urllib.request
from jingdong.items import JingdongItem
import pymysql




class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com']
    header={'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


    start_urls = ['http://www.taobao.com/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        try:
            item = JingdongItem()
            #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()

            thisurl=response.url
            pat='&id=(.*?)&'
            x=re.search(pat,thisurl)
            if(x):
                item['thisid']=re.compile(pat).findall(thisurl)[0]
                item['title']=response.xpath("//html/head/title/text()").extract()
                #item['shop'] = response.xpath("//div[@class='name']/a/@title").extract()
                #item['shoplink'] = response.xpath("//div[@class='name']/a/@href").extract()
                print(item['title'])
                #print(item['shop'])
                #print(item['shoplink'])
                commenturl='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv3424&productId='+str(item['thisid'])+'&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
                priceurl='https://p.3.cn/prices/mgets?callback=jQuery2250603&type=1&area=1_72_4137_0&pdtk=&pduid=741599701&pdpin=&pin=null&pdbp=0&skuIds=J_'+str(item['thisid'])+'&ext=11000000&source=item-pc'
                data1=urllib.request.urlopen(commenturl).read().decode('utf-8','ignore')
                data2 = urllib.request.urlopen(priceurl).read().decode('utf-8','ignore')
                pat2='"commentCount":(.*?),'
                #pat3='"productId":(.*?),'
                pat4='"goodRate":(.*?),'
                pat5='"op":"(.*?)"'
                item['commentcount']=re.compile(pat2).findall(data1)
                #priductID = re.compile(pat3).findall(data1)
                item['goodrate'] = re.compile(pat4).findall(data1)
                item['pricel'] = re.compile(pat5).findall(data2)
                #print(commentcount)
                #print(goodrata)
                #print (pricel)

                for i in range(0, len(item["thisid"])):

                    thisid = item["thisid"][i]
                    for j in range(0, len(item["title"])):

                        title = item["title"][j]
                        for z in range(0, len(item["shop"])):

                            shop = item["shop"][z]
                            for c in range(0, len(item["shoplink"])):

                                shoplink= item["shoplink"][c]
                                for x in range(0, len(item["commentcount"])):

                                    commentcount = item["commentcount"][x]
                                    for y in range(0, len(item["goodrate"])):

                                        goodrate = item["goodrate"][y]
                                        for u in range(0, len(item["pricel"])):

                                            pricel = item["pricel"][u]
                                            conn = pymysql.connect(host="127.0.0.1", user="root", passwd="13579zheng",
                                           db="shuju", charset="utf8")
                                            sql = "insert into `book`(`thisid`,`title`,`shop`,`shoplink`,`commentcount`,`goodrate`,`pricel`) values('" + thisid + "','" + title + "','" + shop + "','" + shoplink + "','" + commentcount + "','" + goodrate + "','" + pricel + "')"
                                            conn.query(sql)
                                            conn.commit()  # 记得commit
                                        conn.close()
      
                else:
                    pass
        '''
            else:
                pass
            return item
        except Exception as e:
            print(e)






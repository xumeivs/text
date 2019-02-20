# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''

class JingdongPipeline(object):
    def process_item(self, item, spider):

        def process_item(self, item, spider):

            for i in range(0, len(item["thisid"])):
                thisid = item["thisid"][i]
                for j in range(0, len(item["title"])):
                    title = item["title"][j]
                    for z in range(0, len(item["shop"])):
                        dianjia = item["shop"][z]
                        for c in range(0, len(item["shoplink"])):
                            dianjialink = item["shoplink"][c]
                            for x in range(0, len(item["commentcount"])):
                                jiage = item["commentcount"][x]
                                for y in range(0, len(item["goodrate"])):
                                    commentcountstr = item["goodrate"][y]
                                    for u in range(0, len(item["pricel"])):
                                        goodrate = item["pricel"][u]




                                    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="13579zheng",
                                                           db="shuju", charset="utf8")
                                    sql = "insert into `book`(`thisid`,`title`,`shop`,`shoplink`,`commentcount`,`goodrate`,`pricel`) values('" + thisid + "','" + title + "','" + shop+ "','" + shoplink + "','" + commentcount + "','" + goodrate + "','" + pricel + "')"
                                    #sql="insert into book(thisid,title,shop,shoplink,commentcount,goodrate,pricel) values ('"+thisid+"','"+title+"','"+shop+"','"+shoplink+"','"+commentcount+"','"+goodrate+"','"+pricel+"')"
                                    conn.query(sql)
                                    conn.commit()  # 记得commit
                                conn.close()

                                return item

'''


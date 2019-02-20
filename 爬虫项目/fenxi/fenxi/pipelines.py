# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''

class FenxiPipeline(object):
    def process_item(self, item, spider):
        for i in range(0, len(item['id'])):
            id=item['id'][i]
            for j in range(0, len(item['comment'])):
                comment=item['comment']
                comment=comment[j]
                for z in range(0, len(item['up'])):
                    up = item['up']
                    up=up[z]
                    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='13579zheng', db='douban',
                                           charset='utf8')
                    sql = "insert into `fx`(`id`,`comment`,`up`)values('" + id + "','" + comment + "','" + up + "')"
                    conn.query(sql)
                conn.commit()
            conn.close()
        return item
'''
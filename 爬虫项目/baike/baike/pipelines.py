# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaikePipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item['ciurl'])):
            ciurl = item['ciurl'][i]
            for j in range(0,len(item['id'])):
                id=item['id'][j]
                res = requests.get(ciurl)
                soup = BeautifulSoup(res.text, 'html.parser')
                file = open(r'E:/测试/百度百科/'+str(id)+'.txt','a')
                for news in soup.select('.cm_fb'):
                    a = news.select('a')[0].text
                    a_href = news.select('a')[0]['href']
                    file.writelines(a)
                    file.writelines('\n')  # 写入并换行
                    file.writelines(a_href)
                    file.writelines('\n')  # 写入并换行
                    file.close  # 关闭链接


        return item

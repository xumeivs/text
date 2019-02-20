# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    thisid=scrapy.Field()
    title=scrapy.Field()
    shop=scrapy.Field()
    shoplink=scrapy.Field()
    commentcount=scrapy.Field()
    goodrate=scrapy.Field()
    pricel=scrapy.Field()

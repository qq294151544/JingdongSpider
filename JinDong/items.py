# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JindongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goods_info = scrapy.Field()
    # goods_price = scrapy.Field()
    goods_link = scrapy.Field()
    goods_price = scrapy.Field()
    goods_price_url=scrapy.Field()
# class JindongPriceItem(scrapy.Item):
#     goods_price = scrapy.Field()

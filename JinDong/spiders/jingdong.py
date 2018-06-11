# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from JinDong.items import JindongItem


class JingdongSpider(CrawlSpider):
    name = 'jingdong'
    allowed_domains = ['list.jd.com','p.3.cn']
    start_urls = ['https://list.jd.com/list.html?cat=670,671,672&page=1']
    price_url = 'https://p.3.cn/prices/mgets?&skuIds=J_{}%2&pduid=15286332332502030043335'
#/list.html?cat=670,671,672&page=3&sort=sort_totalsales15_desc&trans=1&JL=6_0_0
    rules = [
        # 提取职位列表页的链接，发送请求并交给回调函数解析，同时继续响应继续跟进提取链接
        Rule(LinkExtractor(allow=r"cat=670,671,672&page=\d+"), callback="parse_page", follow=True),
    ]

    def parse_page(self, response):
        node_list = response.xpath('//*[@id="plist"]/ul/li')
        # with open('index.html','w') as f:
        #     f.write(response.body)
        for node in node_list:
            item = JindongItem()
            item['goods_info'] = node.xpath('./div/div[3]//em/text()').extract_first()
            item['goods_link'] = node.xpath('./div/div[3]/a/@href').extract_first()
            stu_id = node.xpath('./div/@data-sku').extract_first()
            item['goods_price_url'] = self.price_url.format(stu_id)
            # print item['goods_price_url']
            yield scrapy.Request(url=item['goods_price_url'], meta={'obj': item}, callback=self.parse_price)

    def parse_price(self, response):
        item = response.meta['obj']
        print item
        # print response.body
        item['goods_price'] = json.loads(response.body)[0]['p']
        # print item(type)
        yield item

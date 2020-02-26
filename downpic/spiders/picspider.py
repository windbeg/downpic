# -*- coding: utf-8 -*-
import scrapy

from downpic.items import DownpicItem

class PicspiderSpider(scrapy.Spider):
    name = 'picspider'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/sousuo-201309-0-complex-all-0-all-all-1-0-0-0-0-0-0-all-all.html']

    def parse(self, response):
        item_list=response.xpath("//div/div[@class='imgshow clearfix']/div[@class='swipeboxEx']/div[@class='list']")
        # print('尝试！！')
        for i_item in item_list:
        	item=DownpicItem()	
        	item['image_urls']=i_item.xpath(".//a/img[@class='lazy']/@data-original").extract_first()
        	item['image_dir']=i_item.xpath(".//a/img[@class='lazy']/@alt").extract_first()
        	yield item
        	# print(item)


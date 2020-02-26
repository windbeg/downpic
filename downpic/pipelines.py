# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class DownpicPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item

    def get_media_requests(self, item, info):
        # print('我要看的内容：',item['image_urls'])
        # for image_url in item['image_urls']:
        image_url = "http:" + item['image_urls']
        yield scrapy.Request(image_url,meta={'item':item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        '''
         图片路径设置
        '''
        item = request.meta['item']
        img_name = os.path.basename(item['image_urls'])

        index = item['image_dir'].find('（')
        if index == -1:
            index = item['image_dir'].find('(')
        if not index == -1:
            item['image_dir'] = item['image_dir'][:index]
        filename = u'{}/{}'.format(item['image_dir'], img_name)
        return filename
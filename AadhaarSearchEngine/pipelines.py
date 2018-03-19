# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import  logging


class SespiderPipeline(object):
    def __init__(self):
        self.file = open('urls.txt', 'wb')

    def process_item(self, item, spider):
        self.file.write(item['url']+'\n')
        return item

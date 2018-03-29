# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from news.items import NewsItem
import datetime
import urllib.parse
import socket

class NytSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://www.nytimes.com']

    rules = (
        Rule(LinkExtractor(allow=(r'/[0-9][0-9][0-9][0-9]/+[0-9][0-9]/+[0-9][0-9]+/+')),
            callback='parse_item', follow=True),
        #Rule(LinkExtractor(restrict_xpaths='//li[contains(@class,"SearchResults-item-3k02W")]'),
         #   callback='parse_item'),
        #Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"headline")]'),
         #   callback='parse_item'),
        )


    def parse_item(self, response):
        #create the loader
        l = ItemLoader(item=NewsItem(), response=response)
        #load fields using xpath
        l.add_xpath('title', '//*[@itemprop="headline"]/text()')
        l.add_xpath('author', '//*[@class="byline-author"]/text()')
        l.add_xpath('article', '//*[@class="story-body-text story-content"]/text()')
        l.add_xpath('dop', '//*[@class="dateline"]/text()')
            

        #housekeeping fields
        l.add_value('url', response.url)
        #l.add_value('project', self.settings.get('BOT_NAME'))
        #l.add_value('spider', self.name)
        #l.add_value('server', socket.gethostname())
        #l.add_value('date', datetime.datetime.now())
        return l.load_item()

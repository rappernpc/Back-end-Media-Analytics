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
#from selenium import webdriver 



class NytSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://spiderbites.nytimes.com/2015/']

    rules = (
        Rule(LinkExtractor(allow=('2015'),deny=('classified' ,'style', 'gst', 'key-rates', 'search', 'section', 'slideshow', 'mobile', 'imagepages', 'interactive')),callback='parse_link', follow=True,),)
        #Rule(LinkExtractor(restrict_xpaths=('//*[@id="headlines" or @id="mainContent"]')),
        #    callback='parse_item', follow=True),)
        #Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"headline")]'),
         #   callback='parse_item'),
    #

    
    #def __init__(self, *a, **kw):
        #super(NytSpider, self).__init__(*a, **kw)
        #self.driver = webdriver.Chrome()
    
    def parse_link(self, response):

           
        #create the loader
        l = ItemLoader(item=NewsItem(), response=response)
        #load fields using xpath
        l.add_xpath('title', '//*[@itemprop="headline" or @class="balancedHeadline"]/text()')
        l.add_xpath('author', '//*[@class="byline-author" or @class="author creator"]/text()')
        l.add_xpath('article', '//*[@class="story-body-text story-content" or @class="css-18sbwfn"]/text()')
        l.add_xpath('dop', '//*[@itemprop="dateModified" or @class="css-pnci9ceqgapgq0"]/text()')
        l.add_xpath('section', '//*[@id="kicker"]/span/a/text()')
        
        
        #housekeeping fields
        l.add_value('url', response.url)
        #l.add_value('project', self.settings.get('BOT_NAME'))
        #l.add_value('spider', self.name)
        #l.add_value('server', socket.gethostname())
        #l.add_value('date', datetime.datetime.now())
        #l.add_value('url', response.url)
        return l.load_item()

            
           
        
        
      
        




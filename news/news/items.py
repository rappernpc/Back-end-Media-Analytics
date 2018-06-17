# -*- coding: utf-8 -*-
import scrapy
from scrapy.item import Item, Field  

class NewsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #Primary Fields
    title = Field()
    author = Field()
    article = Field()
    section = Field()

    #calculated fields
    images = Field()
    location = Field()

    #Housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()       

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class PricescrapyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class marketPriceItem(Item):
    market_name = Field()
    price_history = Field()
    remark_info = Field()
    link = Field()

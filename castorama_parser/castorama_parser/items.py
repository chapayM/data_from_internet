# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectParserCastoramaItem(scrapy.Item):
    good_name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    images = scrapy.Field()
    _id = scrapy.Field()
    #product_characteristics_keys = scrapy.Field()
    #product_characteristics_values = scrapy.Field()


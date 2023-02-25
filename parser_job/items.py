# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectParserHhItem(scrapy.Item):
    name = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    currency = scrapy.Field()
    tax = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()


class ProjectParserSjItem(scrapy.Item):
    name = scrapy.Field()
    #salary = scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    currency = scrapy.Field()
    period = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()
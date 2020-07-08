# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookDetailsItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    Book_title=scrapy.Field()
    Rating=scrapy.Field()
    Price=scrapy.Field()


    pass

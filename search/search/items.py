import scrapy


class SearchItem(scrapy.Item):
    keyword = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    timestamp = scrapy.Field()

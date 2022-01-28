import scrapy


class EntrySpider(scrapy.Spider):
    name = 'entry'
    allowed_domains = ['google.com']
    start_urls = ['http://google.com/']

    def parse(self, response):
        pass

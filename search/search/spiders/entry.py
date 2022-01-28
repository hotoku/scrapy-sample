import scrapy


class EntrySpider(scrapy.Spider):
    name = "entry"
    allowed_domains = ["google.com"]
    def __init__(self, query="", *args, **kwargs):
        super(EntrySpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"http://google.com/search?q={query}"]
        print(f"{query=}")


    def parse(self, response):
        print(response.body)

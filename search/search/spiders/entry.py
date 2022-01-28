import scrapy


class EntrySpider(scrapy.Spider):
    name = "entry"
    allowed_domains = ["google.com"]

    def __init__(self, query="", *args, **kwargs):
        super(EntrySpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"http://google.com/search?q={query}"]

    def parse(self, response):
        xpath = "//a/parent::div[contains(@class, 'kCrYT')]"
        nodes = response.xpath(xpath)
        for node in nodes:
            url = node.xpath("a").attrib["href"]
            yield response.follow(url, self.print_response)

    def print_response(self, response):
        print(response)

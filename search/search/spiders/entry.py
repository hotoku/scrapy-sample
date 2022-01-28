from datetime import datetime

import scrapy
from scrapy.http.response import Response
from scrapy.http.response.html import HtmlResponse

from ..items import SearchItem


class EntrySpider(scrapy.Spider):
    name = "entry"
    allowed_domains = ["google.com"]

    def __init__(self, query="", *args, **kwargs):
        super(EntrySpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"http://google.com/search?q={query}"]
        self.query = query

    def parse(self, response: Response):
        xpath = "//a/parent::div[contains(@class, 'kCrYT')]"
        if not isinstance(response, HtmlResponse):
            return
        nodes = response.xpath(xpath)
        date_b: bytes = response.headers["Date"]  # type: ignore
        date_s = date_b.decode()
        timestamp = datetime.strptime(date_s, "%a, %d %b %Y %H:%M:%S GMT")

        for i, node in enumerate(nodes):
            rank = i + 1
            url = node.xpath("a").attrib["href"]
            yield response.follow(
                url,
                self.print_response,
                cb_kwargs={
                    "timestamp": timestamp,
                    "rank": rank
                })

    def print_response(self, response: Response, timestamp: datetime, rank: int):
        if isinstance(response, HtmlResponse):
            url = response.url
            title = response.xpath("//title/text()").get()
            return SearchItem(
                url=url,
                title=title,
                keyword=self.query,
                timestamp=timestamp,
                rank=rank
            )
        return None

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from sqlitedict import SqliteDict
import scrapy

from .items import SearchItem


@dataclass
class Key:
    keyword: str
    rank: int

    def to_str(self) -> str:
        return f"{self.rank}/{self.keyword}"

    @staticmethod
    def parse(s: str) -> Key:
        n = s.find("/")
        keyword = s[(n+1):]
        rank = int(s[:n])
        return Key(keyword, rank)


@dataclass
class Value:
    title: str
    url: str
    timestamp: datetime


class SaveToSqlitePipeline:
    def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        if not isinstance(item, SearchItem):
            return item
        with SqliteDict("db.sqlite", autocommit=True) as dic:
            key = Key(item["keyword"], item["rank"]).to_str()
            value = Value(item["title"], item["url"], item["timestamp"])
            if not key in dic:
                ret = []
            else:
                ret = dic[key]
            ret.append(value)
            dic[key] = ret
        return item

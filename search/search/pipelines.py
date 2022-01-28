import sqlite3

from .items import SearchItem


class SaveToSqlitePipeline:
    def process_item(self, item, spider):
        if isinstance(item, SearchItem):
            con = sqlite3.connect("db.sqlite")
            return item
        return item

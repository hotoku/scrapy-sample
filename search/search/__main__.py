from .pipelines import Key
from sqlitedict import SqliteDict

with SqliteDict("db.sqlite") as dic:
    for k, v in dic.items():
        key = Key.parse(k)
        print(key, ":", v)

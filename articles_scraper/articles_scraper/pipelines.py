# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import sqlite3
import json
import os
from datetime import datetime


class ArticlesScraperPipeline:
    def process_item(self, item, spider):
        return item


class SQLitePipeline:
    def open_spider(self, spider):
        path = os.path.dirname(os.path.abspath(__file__))
        db = os.path.abspath(os.path.join(path, '../../db.sqlite3'))
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles_article (
                id INTEGER PRIMARY KEY,
                title TEXT,
                body TEXT,
                url TEXT UNIQUE,
                publication_date TEXT,
                author TEXT,
                image_urls TEXT,
                entities TEXT
            )
        ''')

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        print('''
            INSERT OR IGNORE INTO articles_article (title, body, url, publication_date, author, image_urls, entities) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['title'],
            item['body'],
            item['url'],
            item['publication_date'],
            item['author'],
            json.dumps(item['image_urls']),
            json.dumps(item['entities'])
        ))
        self.cursor.execute('''
            INSERT OR IGNORE INTO articles_article (title, body, url, publication_date, author, image_urls, entities) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['title'],
            item['body'],
            item['url'],
            item['publication_date'],
            item['author'],
            json.dumps(item['image_urls']),
            json.dumps(item['entities'])
        ))
        print('----------------------------------------------------------')
        self.conn.commit()
        return item

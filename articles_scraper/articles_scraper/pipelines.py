# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import sqlite3
import json
from datetime import datetime


class ArticlesScraperPipeline:
    def process_item(self, item, spider):
        return item


# class SQLitePipeline:
#
#     def process_item(self, item, spider):
#         # Convert publication_date to a datetime object if it's a string
#         if isinstance(item['publication_date'], str):
#             item['publication_date'] = datetime.fromisoformat(item['publication_date'])
#
#         # Save item to the Django model
#         article, created = Article.objects.update_or_create(
#             url=item['url'],
#             defaults={
#                 'title': item['title'],
#                 'body': item['body'],
#                 'publication_date': item['publication_date'],
#                 'author': item['author'],
#                 'image_urls': json.loads(item['image_urls']),
#                 'entities': json.loads(item['entities']),
#             }
#         )
#         print(article)
#         print('-----------------------------------------------!!')
#         print(created)
#         return item


class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('db.sqlite3')
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
        self.cursor.execute('''
            INSERT OR REPLACE INTO articles_article (title, body, url, publication_date, author, image_urls, entities) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['title'],
            item['body'],
            item['url'],
            item['publication_date'],
            item['author'],
            json.dumps(item['image_urls']),
            json.dumps(item['entities'])
        ))
        self.connection.commit()
        return item
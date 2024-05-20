import scrapy
from ..items import ArticleItem
from datetime import datetime
import re


class RestOfWorldSpider(scrapy.Spider):
    name = 'rest_of_world'
    allowed_domains = ['restofworld.org']
    start_urls = ['https://restofworld.org/series/the-rise-of-ai/']

    def parse(self, response):
        # Extract article links
        article_links = response.css('article a::attr(href)').getall()
        for link in article_links:
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        item = ArticleItem()
        item['title'] = response.css('h1::text').get()
        item['body'] = ' '.join(response.css('article p::text').getall())
        item['url'] = response.url
        item['publication_date'] = response.css('time::attr(datetime)').get()
        item['author'] = response.css('.author a::text').get()
        item['image_urls'] = response.css('article img::attr(src)').getall()
        # Add NER extraction here (see below)
        yield item

    # def parse_date(self, date_string):
    #     # 2024-05-20T10:30:00Z
    #     return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
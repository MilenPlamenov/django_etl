import scrapy
from ..items import ArticleItem
from datetime import datetime


class CapitalBriefSpider(scrapy.Spider):
    name = 'capital_brief'
    allowed_domains = ['capitalbrief.com']
    start_urls = ['https://www.capitalbrief.com/technology/']

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
        item['publication_date'] = self.parse_date(response.css('time::attr(datetime)').get())
        item['author'] = response.css('.author a::text').get()
        item['image_urls'] = response.css('article img::attr(src)').getall()
        # Add NER extraction here
        yield item

    # def parse_date(self, date_string):
    #     # 2024-05-20T10:30:00Z
    #     return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")

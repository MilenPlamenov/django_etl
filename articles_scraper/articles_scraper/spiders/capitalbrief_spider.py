import scrapy
from ..items import ArticleItem
from datetime import datetime
from scrapy.exceptions import DropItem
import jsonschema
from jsonschema import validate
import spacy


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
        item['title'] = response.css('h2 a::text').get()
        item['body'] = response.css('article p::text').get()
        item['url'] = response.css('article h2 a').attrib.get('href')
        item['publication_date'] = response.css('time::attr(datetime)').get()
        item['author'] = response.css('span.author::text').get()
        item['author'] = item['author'].replace('\xa0', ' ') if item['author'] else 'No author'
        item['image_urls'] = response.css('article img::attr(src)').get()
        # Add NER extraction here
        # TODO
        item['entities'] = response.css('article img::attr(src)').get()  # for tests
        yield item

    def validate_item(self, item):
        schema = {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "body": {"type": "string"},
                "url": {"type": "string"},
                "publication_date": {"type": "string", "format": "date-time"},
                "author": {"type": "string"},
                "image_urls": {"type": "array", "items": {"type": "string"}},
                "entities": {
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": [
                            {"type": "string"},
                            {"type": "string"}
                        ]
                    }
                }
            },
            "required": ["title", "body", "url", "publication_date", "author"]
        }
        try:
            validate(instance=item, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            raise DropItem(f"Invalid item: {e.message}")
        return item


from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    url = models.URLField(unique=True)
    publication_date = models.DateTimeField()
    author = models.CharField(max_length=255)
    image_urls = models.JSONField()
    entities = models.JSONField()

    def __str__(self):
        return self.title

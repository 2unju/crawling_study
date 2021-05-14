from django.db import models

# Create your models here.
class NewsData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
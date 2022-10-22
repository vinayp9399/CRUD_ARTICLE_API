from django.db import models


class Article_details(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Publish_date = models.CharField(max_length=200)

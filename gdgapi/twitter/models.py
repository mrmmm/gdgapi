from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)


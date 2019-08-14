from django.db import models

class Tweets(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.CharField(max_length=45)
    tweet = models.TextField()
    username = models.CharField(max_length=100)
    retweet_count = models.IntegerField()
    location = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    def __str__(self):
        return self

from django.shortcuts import render
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from . import user_info
from .models import Tweets
import json
import requests

def home(request):
    return render(request, 'home.html')

def search(request):
    str = Tweets.objects.filter()
    return render(request, 'home.html')


class TwitterStreamer():
    def stream_tweets(self, tweets_file, hash_tag):
        listener = StdOutListener(tweets_file)
        auth = OAuthHandler(user_info.API_KEY, user_info.API_SECRET)
        auth.set_access_token(user_info.ACCESS_TOKEN, user_info.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag)


class StdOutListener(StreamListener):
    #class for printing tweets.

    def __init__(self, tweets_file):
        self.tweets_file = tweets_file

    def on_data(self, data):
        list1 = dict(json.loads(data))
        obj = Tweets()
        obj.created_at = self.post(list1["created_at"])
        obj.id = self.post(list1["id"])
        obj.tweet = self.post(list1["text"])
        obj.location =self.post(list1["location"])
        obj.place = self.post(list1["place"])
        obj.save()
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    hash_tag = ['Narendra Modi']
    #tweets_file = 'tweets.json'
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(tweets_file, hash_tag)



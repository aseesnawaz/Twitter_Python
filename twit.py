import dataset
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

count = 0;
ckey = ''
csecret = ''
atoken = ''
asecret = ''

db = dataset.connect("sqlite:///tweets.db")
tags = []

class listener(StreamListener):

    def on_status(self, data):
        if data.retweeted:
            return
        text = data.text
        retweets = data.retweet_count
        loc = data.user.location
        hashtags = data.entities.get('hashtags')
        if not hashtags:
            return
        for i in range(len(hashtags)):
            tags.append(hashtags[i]['text'].lower())

        table = db["tweets"]
        table.insert(dict(
                user_location=loc,
                text=text,
                retweet_count=retweets,
                tags = str(tags)
            ))
        del tags[:]

    def on_error(self, data):
        if data == 420:
            return False

def gatherTwitterData():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(locations=[-125,25,-65,48], async=False)
    time.sleep(10000)
    twitterStream.disconnect()

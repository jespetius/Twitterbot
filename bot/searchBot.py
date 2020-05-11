import tweepy
import os
import time
from dotenv import load_dotenv
load_dotenv()

# Tunnistusobjektin luominen
auth = tweepy.OAuthHandler(os.getenv('twitter_consumer_key'),
                       os.getenv('twitter_consumer_secret'))
# Access tokenien asettaminen
auth.set_access_token(os.getenv('twitter_access_token'),
                      os.getenv('twitter_access_token_secret'))
# API-objektin luominen ja auth informaation puskeminen
api = tweepy.API(auth)

#annetaan mitä haetaan ja monta kappaletta
hashtag = "#opetuslapaset"
tweetnumber = 1

#etsitään äsken annetuilla ehdoilla
tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

#retweet jos löytyy vastaavia tweettejä
def searchBot():
    for tweet in tweets:
        try: 
            tweet.retweet()
            print("Retweet tehty!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchBot()
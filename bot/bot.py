import tweepy
import os
import time
from dotenv import load_dotenv
load_dotenv()
import pyowm
from weather import fetchWeather

# Tunnistusobjektin luominen
auth = tweepy.OAuthHandler(os.getenv('twitter_consumer_key'),
                       os.getenv('twitter_consumer_secret'))
# Access tokenien asettaminen
auth.set_access_token(os.getenv('twitter_access_token'),
                      os.getenv('twitter_access_token_secret'))
# API-objektin luominen ja auth informaation puskeminen
api = tweepy.API(auth)
FILE_NAME = 'last_seen.txt'

#lähettää sää tiedotteen
#api.update_status(fetchWeather())



#hae viimeksi luettu tweetti .txt
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

#ota talteen viimeisin tweetti
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return
    
#etsi tweetit jossa on mainittu api, eli twitterkäyttäjä ja vastaa, tykkää ja retweet
def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if "#opetuslapaset" in tweet.full_text.lower():
            print(str(tweet.id)+ ' - ' + tweet.full_text) 
            api.update_status("@" + tweet.user.screen_name + ' ' + fetchWeather(), tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)
#pitää elossa
while True:
    reply()
    time.sleep(69)
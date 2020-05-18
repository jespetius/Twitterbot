import tweepy
import os
import time
from dotenv import load_dotenv
load_dotenv()
import pyowm
import requests, json
from key import key

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
#api.update_status("testi")


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
def reply1():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        print(str(tweet.id)+ ' - ' + tweet.full_text) 
        s = tweet.full_text.lower()
        weatherCity = s.replace('@jespetiusb ', '')
        print(weatherCity)
        return str(weatherCity)
        

def fetchWeather():

    degree_sign = u'\N{DEGREE SIGN}'
    city = reply1()
    city1 = str(city)
    city2 = city1.replace('@jespetiusb ', '')
    
    owm = pyowm.OWM(key)
    url='http://api.openweathermap.org/data/2.5/weather?q='+city2+'&appid=' + key

    r =requests.get(url)
    time.sleep(5)
    x = r.json()

    if x["cod"]== "404":

        output="Anna oikea kaupunki"

    else:
    
        observation = owm.weather_at_place(city1)
        
        weather = observation.get_weather()
        
        temperature = weather.get_temperature('celsius')['temp']
       
        wind = weather.get_wind()['speed']
       
        humidity = weather.get_humidity()
       
        status = weather.get_detailed_status()
       
        answer = city1 + '\n '  + str(status) + '\n temperature ' +  str(temperature) +degree_sign + 'C\n wind ' + str(wind) + ' m/s\n humidity '+ str(humidity)+' %'
        output = str(answer)
        print(output)

    return output









def reply2():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):


        
        #päivittää, tykkää, jakaa
        api.update_status("@" + tweet.user.screen_name + ' ' + fetchWeather(), tweet.id)
        
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        
        store_last_seen(FILE_NAME, tweet.id)
    




#pitää elossa
while True:
    reply1()
    reply2()
    time.sleep(69)



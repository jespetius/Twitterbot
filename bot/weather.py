import tweepy
import os
import time
from dotenv import load_dotenv
load_dotenv()
import requests, json
import pyowm
import time
from key import *

# Tunnistusobjektin luominen
auth = tweepy.OAuthHandler(os.getenv('twitter_consumer_key'),
                       os.getenv('twitter_consumer_secret'))
# Access tokenien asettaminen
auth.set_access_token(os.getenv('twitter_access_token'),
                      os.getenv('twitter_access_token_secret'))
# API-objektin luominen ja auth informaation puskeminen
api = tweepy.API(auth)
FILE_NAME = 'last_seen.txt'


def fetchWeather():

    degree_sign = u'\N{DEGREE SIGN}'

    owm = pyowm.OWM(key)

    #observation = owm.weather_at_zip_code('00740', 'FI')
    observation = owm.weather_at_place('Helsinki')
    weather = observation.get_weather()

    temperature = weather.get_temperature('celsius')['temp']

    wind = weather.get_wind()['speed']

    humidity = weather.get_humidity()

    status = weather.get_detailed_status()

    answer = 'Helsinki \n '  + str(status) + '\n temperature ' +  str(temperature) +degree_sign + '\n windspeed ' + str(wind) + '\n humidity '+ str(humidity)
    output = str(answer)
    #api.update_status('testi')
    return output

print(fetchWeather())


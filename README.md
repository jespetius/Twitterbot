## Twitterbot
Tämä on lopputyö kurssille Ohjelmistokehityksen teknologioita SWD4TN023-3006
Tarkoituksena olisi tehdä botti twitteriin käyttäen pythonia.
Botti hakee säätietoja ja päivittää niitä tietyin väliajoin.
Botti on tarkoitus laittaa omalle palvelimelle toimimaan. 


## Twitter keys

Jotta twitterin API:a voi hyödyntää, tarvitsee sinne avaimet. Ne on kätevä hakea https://developer.twitter.com/en.

## Toteutus

käyttäen pythonin tweepy-kirjastoa. Sen dokumentaatio löytyy täältä. http://docs.tweepy.org/en/latest/
Esimerkkejä tweepyn käytöstä
``` sh
#lähettää tweetin
api.update_status("testi")

```

käytössä openweathermap josta haetaan säätietoja. Apuna käytin PyOWM kirjastoa. Esimerkki Openweathermapin käytöstä:
``` sh
    #openweathermap avain
    owm = pyowm.OWM(key)

    #paikka jonka sää halutaan
    observation = owm.weather_at_place('Helsinki')
    weather = observation.get_weather()
    
    #säätietoja
    temperature = weather.get_temperature('celsius')['temp']

    wind = weather.get_wind()['speed']

    humidity = weather.get_humidity()

    status = weather.get_detailed_status()

```

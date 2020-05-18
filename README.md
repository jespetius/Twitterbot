## Twitterbot
Tämä on lopputyö kurssille Ohjelmistokehityksen teknologioita SWD4TN023-3006
Tarkoituksena olisi tehdä botti twitteriin käyttäen pythonia.
Botti hakee säätietoja ja päivittää niitä tietyin väliajoin. 
Botin olisi tarkoitus vastata käyttäjän antamaan kaupunkiin sen säätiedolla.
Botti on tarkoitus laittaa omalle palvelimelle toimimaan.


Botin käyttäminen on seuraavanlaista:

- joka tunti laittaa säätiedotteen Helsingistä

- joka minuutti tarkistaa, onko laitettu tweettiä botille ja tarvitaanko säätietoja. 
 

## Twitter ja OpenWeatheMap keys

Jotta twitterin API:a voi hyödyntää, tarvitsee sinne avaimet. Ne on kätevä hakea https://developer.twitter.com/en.

OpenWeatherMap avaimen voi hakea täältä https://openweathermap.org/
## Toteutus

Työssä käytetään pythonin tweepy-kirjastoa. Sen dokumentaatio löytyy täältä. http://docs.tweepy.org/en/latest/
Esimerkkejä tweepyn käytöstä
``` sh
#lähettää tweetin
api.update_status("testi")




```

käytössä myös openweathermap josta haetaan säätietoja. Apuna käytin PyOWM kirjastoa. Esimerkki Openweathermapin käytöstä:
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
## Käyttö 

Laita ensiksi koodi pyörimään komennolla:
``` sh
python bot.py
```
Twitterissä laita tweetti : @JespetiusB <Kaupunki>
    
 Tähän kuva

## Miksi valitsin aiheen

Valitsin aiheen, koska minua kiinnosti twitterin hyödyntäminen. Kieleksi valitsin pythonin, koska olimme käyneet sitä tällä kurssilla ja 
halusin syventyä siihen vielä lisää. 


## Kehitysideat
Jos löytyy bugeja tai tulee mieleen jotain muuta kehitysideaa, ne voi laittaa [tänne](https://github.com/jespetius/Twitterbot/issues).



## Yhteystiedot

Jesperi Kuula - jesperi.kuula@myy.haaga-helia.fi

#haetaan twitteravaimet piilosta
from config import getApi
import os

#api
api = getApi()

#yksi tweetti
def postStatus(update):
    status = api.PostUpdate(update)
    print(status)

postStatus("Hi, im a bot")

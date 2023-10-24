import json

from dotenv import load_dotenv
import os
load_dotenv()
import random

stopwords = [] # your list with json objects (dicts)

import pywhatkit
with open('./dicts/fr-FR/stopwords.json') as json_file:
   stopwords = json.load(json_file)

from pykeyboard import PyKeyboard

k = PyKeyboard()

def manage_music(details, new_sentence):
    if details == "play":
        query = new_sentence
    
        for keyword in stopwords:
            query = query.replace(' ' + keyword + ' ', ' ').replace(keyword + " ", "")
        print(query)
        os.system("killall -9 'Google Chrome'")
        pywhatkit.playonyt(query)
        print('Song has opened in your browser.')
        return "success", False
    else:
        os.system("killall -9 'Google Chrome'")
        return "success", False


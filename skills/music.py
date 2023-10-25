import json
from dotenv import load_dotenv
import os
import random
import pywhatkit
from pykeyboard import PyKeyboard

# Load environment variables from a .env file
load_dotenv()

# Create an empty list for stopwords
stopwords = []

# Load a list of stopwords from a JSON file
with open('./dicts/fr-FR/stopwords.json') as json_file:
    stopwords = json.load(json_file)

# Create a PyKeyboard object for keyboard control
k = PyKeyboard()

# Define a function to manage music
def manage_music(details, new_sentence):
    if details == "play":
        query = new_sentence

        # Remove stopwords from the query
        for keyword in stopwords:
            query = query.replace(' ' + keyword + ' ', ' ').replace(keyword + " ", "")
        print(query)

        # Kill any running Google Chrome processes
        os.system("killall -9 'Google Chrome'")

        # Use pywhatkit to play a YouTube video based on the query
        pywhatkit.playonyt(query)

        print('Song has opened in your browser.')
        return "success", False
    else:
        # Kill any running Google Chrome processes
        os.system("killall -9 'Google Chrome'")
        return "success", False

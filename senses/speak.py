# Text to speech functions
# => takes sentence(String) as input
# => return audio output

import pyttsx3

engine = pyttsx3.init()

print(engine.setProperty('voice',"french+f1"))

def speak (sentence):
    engine.say(sentence)
    return engine.runAndWait()

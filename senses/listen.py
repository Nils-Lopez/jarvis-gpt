# Speech to text functions
# => takes sentence (audio) as input
# => return sentence (text) as output

import speech_recognition as sr
from dotenv import load_dotenv
import os
load_dotenv()

recognizer = sr.Recognizer() #Init speech recognition

micro = sr.Microphone() #Use default mic as input (add index as params for specific one, found using sr.Microphone.list_microphone_names())

def listen ():
    try:
        with micro as source:
            recognizer.adjust_for_ambient_noise(source)
            recognizer.pause_threshold = 0.7
            recognizer.non_speaking_duration = 0.5
            audio_data = recognizer.listen(micro)
        result = recognizer.recognize_google(audio_data, language=os.getenv("LANGUAGE"))
        print("eared: ",result) 
        return result
    except sr.UnknownValueError:
        return "error"
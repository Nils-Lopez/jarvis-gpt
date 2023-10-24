# Speech to text functions
# => takes sentence (audio) as input
# => return sentence (text) as output

import speech_recognition as sr

recognizer = sr.Recognizer() #Init speech recognition

micro = sr.Microphone() #Use default mic as input (add index as params for specific one, found using sr.Microphone.list_microphone_names())

def listen ():
    with micro as source:
        print('Listening...')
        audio_data = recognizer.listen(source)
    result = r.recognize_google(audio_data, language="fr-FR")
    return result
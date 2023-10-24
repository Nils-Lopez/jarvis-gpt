# Text to speech functions
# => takes sentence(String) as input
# => return audio output

from dotenv import load_dotenv
import os
import playsound
import json
import random 
import google.cloud.texttospeech as tts
from google.oauth2 import service_account

load_dotenv()

credentials = service_account.Credentials.from_service_account_file(os.getenv('GOOGLE_KEY_PATH'))

errors_data = [] # your list with json objects (dicts)

with open('./dicts/fr-FR/errors.json') as json_file:
   errors_data = json.load(json_file)

success_data = [] # your list with json objects (dicts)

with open('./dicts/fr-FR/success.json') as json_file:
   success_data = json.load(json_file)

thinking_data = [] # your list with json objects (dicts)

with open('./dicts/fr-FR/thinking.json') as json_file:
   thinking_data = json.load(json_file)
   
def text_to_wav(voice_name: "fr-FR-Neural2-A", text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient(credentials=credentials)
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = f"{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')

def speak (sentence):
    new_sentence = sentence
    if "error" in sentence:
        for error in errors_data:
            if error == sentence:
                new_sentence = random.choice(errors_data[error])
    if "success" in sentence:
        new_sentence = random.choice(success_data)
    if "thinking" in sentence:
        new_sentence = random.choice(thinking_data)
    text_to_wav(os.getenv("LANGUAGE") + "-Neural2-E", new_sentence)
    return playsound.playsound(os.getenv("LANGUAGE") + "-Neural2-E.wav")  

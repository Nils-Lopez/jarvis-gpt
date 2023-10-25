# Text to speech functions
# These functions are responsible for generating speech audio from text using Google Text-to-Speech.

# Import necessary modules and libraries
from dotenv import load_dotenv
import os
import playsound
import json
import random 
import google.cloud.texttospeech as tts
from google.oauth2 import service_account

# Load environment variables from a .env file
load_dotenv()

# Load Google Cloud service account credentials from the specified file path
credentials = service_account.Credentials.from_service_account_file(os.getenv('GOOGLE_KEY_PATH'))

# Initialize empty lists to store JSON data
errors_data = []  # A list to store JSON objects related to errors
success_data = []  # A list to store JSON objects related to success
thinking_data = []  # A list to store JSON objects related to thinking

# Load error JSON data from the 'errors.json' file in the 'fr-FR' folder
with open('./dicts/fr-FR/errors.json') as json_file:
   errors_data = json.load(json_file)

# Load success JSON data from the 'success.json' file in the 'fr-FR' folder
with open('./dicts/fr-FR/success.json') as json_file:
   success_data = json.load(json_file)

# Load thinking JSON data from the 'thinking.json' file in the 'fr-FR' folder
with open('./dicts/fr-FR/thinking.json') as json_file:
   thinking_data = json.load(json_file)
   
# Define a function to convert text to speech in WAV format
def text_to_wav(voice_name: "fr-FR-Neural2-A", text: str):
    # Extract language code from the voice name
    language_code = "-".join(voice_name.split("-")[:2])
    
    # Define input, voice, and audio configuration parameters
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    # Create a TextToSpeechClient instance with credentials
    client = tts.TextToSpeechClient(credentials=credentials)

    # Generate speech from the input text
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    # Define the filename for the generated speech
    filename = f"{voice_name}.wav"
    
    # Save the generated speech to a WAV file
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')

# Define a function to speak a sentence
def speak(sentence):
    new_sentence = sentence
    
    # Check if the sentence contains "error" and replace with a random error message
    if "error" in sentence:
        for error in errors_data:
            if error == sentence:
                new_sentence = random.choice(errors_data[error])
    
    # Check if the sentence contains "success" and replace with a random success message
    if "success" in sentence:
        new_sentence = random.choice(success_data)
    
    # Check if the sentence contains "thinking" and replace with a random thinking message
    if "thinking" in sentence:
        new_sentence = random.choice(thinking_data)
    
    # Convert the modified sentence to speech and play it
    text_to_wav(os.getenv("LANGUAGE") + "-Neural2-E", new_sentence)
    return playsound.playsound(os.getenv("LANGUAGE") + "-Neural2-E.wav")  

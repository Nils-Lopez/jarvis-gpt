---
# JARVIS Voice Assistant

Welcome to JARVIS Voice Assistant, an open-source, highly customizable voice assistant powered by the state-of-the-art ChatGPT and Google Text-to-Speech (TTS) technologies. This versatile assistant empowers you to create your own voice-controlled AI companion with remarkable capabilities, such as natural language understanding, language translation, and music playback. Moreover, you can expand its linguistic capabilities by translating the provided French dictionaries into other languages of your choice.

## Introduction

JARVIS Voice Assistant is designed to be your digital assistant, enabling you to interact with your computer using natural language. Whether you want to ask questions, control your applications, or simply enjoy music, JARVIS can be configured to cater to your needs.

## Features

- **Speech Recognition and Natural Language Processing:** JARVIS leverages ChatGPT's sophisticated natural language understanding to respond intelligently to your voice commands.

- **Google Text-to-Speech (TTS):** Enjoy lifelike and engaging responses, thanks to Google TTS technology, which brings your assistant's voice to life.

- **Music Playback:** JARVIS can also play your favorite music. Just ask, and it will handle the rest.

- **Multilingual Support:** Customize JARVIS by translating the provided French dictionaries into your preferred language.

### Setup Steps

Follow these precise steps to set up your JARVIS Voice Assistant:

1. **Installation**
    - Install PyAudio to enable microphone input.
    - Clone the JARVIS Voice Assistant repository to your local machine.
    - Configure your Google TTS App and download the necessary JSON keys to enable TTS functionality.

2. **Install Requirements**
    - Execute the command `pip install -r requirements.txt` to install all required Python dependencies.

3. **Configure Environment Variables**
    - Set the following environment variables in your system:
        - `LANGUAGE=fr-FR`: Configure your desired base language (e.g., `en-US` for English).
        - `OPEN_AI_APIKEY=XA********YZ`: Replace with your OpenAI GPT-3 API key.
        - `GOOGLE_KEY_PATH=google-key.json`: Provide the path to your Google TTS JSON key file.

Ensure that you replace the placeholders with your actual values where specified.



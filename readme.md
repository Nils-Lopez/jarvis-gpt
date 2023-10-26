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
    - Clone the JARVIS Voice Assistant repository to your local machine.
    
    ```shell
    git clone https://github.com/Nils-Lopez/jarvis-gpt.git
    ```
2. **Install Requirements**
    - Execute the following command to install all required Python dependencies.
    ```shell
    pip install -r requirements.txt
    ```
    - (Some dependencies may need some additional setup steps, in that case follow the provided steps by the terminal)

3. **Configure Environment Variables**
    - Set the following environment variables in your system:
        - `LANGUAGE=fr-FR`: Configure your desired base language (e.g., `en-US` for English).
        - `OPEN_AI_APIKEY=XA********YZ`: Replace with your OpenAI API key. [OpenAI API Key Setup](#openai-api-key-setup)
        - `GOOGLE_KEY_PATH=google-key.json`: Provide the path to your Google TTS JSON key file. [Link to Google TTS App Initialization](#google-tts-app-initialization)

Ensure that you replace the placeholders with your actual values where specified.
   

## Google TTS App Initialization

To enable Google Text-to-Speech (TTS) functionality in your JARVIS Voice Assistant, you need to create a Google Cloud Project and obtain the necessary credentials. Follow these steps:

1. **Create a Google Cloud Project:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one. Make sure you have billing enabled for the project.

2. **Enable the Text-to-Speech API:**
   - In the Google Cloud Console, navigate to the project you created/selected.
   - In the left-hand menu, click on "APIs & Services" > "Library."
   - In the search bar, type "Text-to-Speech API" and select it.
   - Click the "Enable" button to enable the Text-to-Speech API for your project.

3. **Create Service Account Credentials:**
   - In the Google Cloud Console, go to "APIs & Services" > "Credentials."
   - Click on the "Create credentials" dropdown and select "Service Account Key."
   - Follow the prompts to create a new service account. Give it a name and role (e.g., "Text-to-Speech Service").
   - For the role, you can choose "Project" > "Editor" for a broad set of permissions. Adjust this based on your project's requirements.

4. **Generate a JSON Key File:**
   - After creating the service account, you will be prompted to create a JSON key. Click "Create key."
   - This will download a JSON file that contains the necessary credentials for using Google TTS. Save this JSON file to your local machine.
  
## OpenAI API Key Setup

To enable JARVIS Voice Assistant's natural language understanding and processing capabilities, you need to obtain an API key from OpenAI. Follow these steps to get your OpenAI API key:

1. **Sign Up or Log In to OpenAI:**
   - If you don't already have an OpenAI account, you can sign up for one at [OpenAI's website](https://www.openai.com/signup/).
   - If you already have an account, log in.

2. **Access Your API Keys:**
   - Once you're logged in, navigate to your account settings or dashboard to find your API keys. This may be labeled as "API Keys" or "Developer Settings."

3. **Create a New API Key:**
   - If you don't already have an API key, create a new one. Typically, you'll need to provide a name for the key.

4. **Copy Your API Key:**
   - Once the key is created, copy it to your clipboard. This key is required to access OpenAI's GPT-3 capabilities.





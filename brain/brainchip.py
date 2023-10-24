import openai
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPEN_AI_APIKEY')

def ask_gpt(new_sentence):
    response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Réponds à cette question comme si tu étais Jarvis, un assistant personnel futuriste, réponds en moins de 20 mots, toujours avec des commentaires de geek, finis chaque phrase par une référence de la culture geek"},
                        {"role": "user", "content": new_sentence}
              ])
    
    return response.choices[0].message.content, False


from senses.speak import speak
from senses.listen import listen

from brain.cortex import understand_sentence
from brain.brainchip import ask_gpt

from skills.lights import manage_lights
from skills.music import manage_music

tasks = {
    "light": manage_lights,
    "music": manage_music,
    "gpt": ask_gpt
}

def main ():
    while True:
        print('ready for instructions..')
        sentence = listen()
        if "jarvis" in sentence.lower(): #check if wakeword has been said
            filtered_sentence = sentence.lower().replace("jarvis", "")
            task, details, new_sentence = understand_sentence(filtered_sentence) #analyze sentence for task
            if task:
                if task == "gpt":
                    response, error = tasks[task](filtered_sentence)
                else:
                    response, error = tasks[task](details, new_sentence)
                    if response:
                        speak(response)
                    else: #error while executing task
                        speak(error)
            else: #task not found
                speak("unkown-action-error")
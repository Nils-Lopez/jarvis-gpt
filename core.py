# Import various modules and functions
from senses.speak import speak
from senses.listen import listen
from brain.cortex import understand_sentence
from brain.brainchip import ask_gpt
from skills.lights import manage_lights
from skills.music import manage_music
from dotenv import load_dotenv
import os
from random import randrange
import playsound

# Load environment variables from a .env file
load_dotenv()

# Create a dictionary mapping tasks to their corresponding functions
tasks = {
    "light": manage_lights,
    "music": manage_music,
    "gpt": ask_gpt
}

# Print a starting message and display the language used
print("===========================")
print('Starting JARVIS v0.1')
print('Language used: ', os.getenv('LANGUAGE'))

# Define the main function
def main():
    while True:
        print('ready for instructions..')
        sentence = listen()

        # Check if the wake word "jarvis" is said in the sentence
        if ("jarvis" in sentence.lower() or "service" in sentence.lower()) and len(sentence) > 7:

            # Remove the wake word from the sentence
            filtered_sentence = sentence.lower().replace("jarvis", "").replace("service", "")

            # Analyze the sentence to determine the task
            task, details, new_sentence = understand_sentence(filtered_sentence)

            # Play a sound effect to indicate Jarvis is listening
            playsound.playsound("./sound-effects/droid" + str(randrange(1, 6)) + ".mp3")

            if task:
                if task == "gpt":
                    # Execute the GPT-3 task
                    response, error = tasks[task](filtered_sentence)
                    if response:
                        # Kill any running Google Chrome processes and speak the response
                        os.system("killall -9 'Google Chrome'")
                        speak(response)
                    else:  # Error occurred while executing the task
                        print(error)
                        speak(error)
                else:
                    if task == "music" and details == "play":
                        speak("Je cherche et lance la musique patientez quelques instants.")

                    # Execute the task with details and the modified sentence
                    response, error = tasks[task](details, new_sentence)
                    if response:
                        speak(response)
                    else:  # Error occurred while executing the task
                        print(error)
                        speak(error)
            else:  # Task not found
                speak("unknown-action-error")

# Call the main function to start Jarvis
main()

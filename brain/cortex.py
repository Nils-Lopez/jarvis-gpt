import json

# Create an empty list to store JSON data
tasks_data = []

# Open a JSON file containing tasks
with open('./dicts/fr-FR/tasks.json') as json_file:
    tasks_data = json.load(json_file)

# Define a function to understand a given sentence
def understand_sentence(sentence):
    # Initialize default values for task and details
    task = "unknown-action-error"
    details = []
    new_sentence = sentence

    # Check if the sentence contains keywords matching known tasks
    for tasks in tasks_data:
        for task_name in tasks:
            if task_name != "details" and any(keyword in sentence for keyword in tasks[task_name]):
                # If a keyword matches, update the task and details
                task = task_name
                details = tasks["details"]
                # Remove the found keyword from the sentence
                for keyword in tasks[task_name]:
                    if keyword != "mets":  # Ensure the keyword is not "mets"
                        new_sentence = new_sentence.replace(' ' + keyword + ' ', ' ').replace(keyword + " ", "")

    # If a task has been found
    if task != "unknown-action-error":
        # Check if there are sub-tasks for the main task
        for task_spec_name in details:
            if any(keyword in sentence for keyword in details[task_spec_name]):
                # Remove the found keyword from the sentence
                for keyword in details[task_spec_name]:
                    new_sentence = new_sentence.replace(' ' + keyword + ' ', ' ').replace(keyword + " ", "")
                # Update the details with the found sub-task
                details = task_spec_name
                break
        # If details is a string, return the task, details, and the modified sentence
        if isinstance(details, str):
            return task, details, new_sentence
        # Otherwise, return default values to indicate GPT-3 should be used
        else:
            return "gpt", False, False
    else:
        # If no task was found
        return "gpt", False, False
        

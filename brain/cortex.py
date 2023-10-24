import json

tasks_data = [] # your list with json objects (dicts)

with open('./dicts/fr-FR/tasks.json') as json_file:
   tasks_data = json.load(json_file)

def understand_sentence (sentence):
    task = "unknown-action-error"
    details = []
    new_sentence = sentence
    # Check for known task in our list
    for tasks in tasks_data:
        for task_name in tasks:
            if task_name != "details" and any(keyword in sentence for keyword in tasks[task_name]): 
                task = task_name
                details = tasks["details"]
                # Delete found keyword from sentence
                for keyword in tasks[task_name]:
                    new_sentence = new_sentence.replace(' ' + keyword + ' ', ' ')
    if task != "unknown-action-error":
        # Check for known subtask in subtask list
        for task_spec_name in details:
            if any(keyword in sentence for keyword in details[task_spec_name]): 
                # Delete found keyword from sentence
                for keyword in details[task_spec_name]:
                    new_sentence = new_sentence.replace(' ' + keyword + ' ', ' ').replace(keyword + " ", "")
                details = task_spec_name
                break
        if isinstance(details, str):
            return task, details, new_sentence
        else:
            return "gpt"
    else:
        return "gpt"
        

import json,os
from datetime import datetime

json_path = 'tasks.json'


#Reading all the tasks from json 
def read():

    if (not os.path.isfile(json_path)) or os.path.getsize(json_path) == 0:
        with open (json_path, 'w') as f:
            f.write("[]")

    with open(json_path, 'r') as f:
        tasks = json.load(f)
    return tasks


#Adding a task to the json
def add(description):
    tasks = read()
    task_id = 1
    if tasks:
        task_id = tasks[-1]["id"]+1
    task = {
        "id":task_id,
        "description":description,
        "status":"todo",
        "created-at":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated-at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)

    with open(json_path, 'w') as f:
        json.dump(tasks, f, indent=2)


#Updating the tasks
def update_task(task_id, description):
    tasks = read()
    task_to_update = ""
    for task in tasks:
        if task["id"] == task_id:
            task_to_update = task
            break
    if task_to_update:
         task_to_update["description"]=description
         task_to_update["updated-at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         with open(json_path, 'w') as f:
            json.dump(tasks, f, indent=2)
            
#update the status
def update_status(task_id, status):
    if status == "mark-in-progress":
        status = "in-progress"
    elif status == "mark-done":
        status = "done"
    else:
        return

    tasks = read()
    for task in tasks:
        if task["id"] == task_id:
            task["status"]=status
            task["updated-at"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(json_path, 'w') as f:
                json.dump(tasks, f, indent=2) 


#list all
def list(status=""):
    tasks = read()
    print(f"\n ID. Task Status")
    print("------------------------------------------------------------------")
    if not status:
        for task in tasks:
            emoji = emoji_gen(task["status"])
            print(f"\n {task["id"]}. {task["description"]} {task["status"].upper()} {emoji}")

    if status =="todo":
        for task in tasks:
            emoji = emoji_gen(task["status"])
            if task["status"] =="todo":
                print(f"\n {task["id"]}. {task["description"]} {task["status"].upper()} {emoji}")

    elif status == "in-progress":
        for task in tasks:
            emoji = emoji_gen(task["status"])
            if task["status"] =="in-progress":
                print(f"\n {task["id"]}. {task["description"]} {task["status"].upper()} {emoji}")

    elif status == "done":
        for task in tasks:
            emoji = emoji_gen(task["status"])
            if task["status"] =="done":
                print(f"\n {task["id"]}. {task["description"]} {task["status"].upper()} {emoji}")


def emoji_gen(status="todo"):
    if status == "in-progress":
        return "🟡"
    elif status =="done":
        return "🟢"
    return "🔴"

def delete_task(task_id):
    task_to_delete = ""
    tasks = read()
    for task in tasks:
        if task["id"] == task_id:
            task_to_delete = task
    if task_to_delete:
        tasks.remove(task_to_delete)
        with open(json_path, "w") as f:
            json.dump(tasks, f, indent=2)
        return "Task deleted!"
    return "Task doesn't exist"



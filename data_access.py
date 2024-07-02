from models.task import Task

TASKS_FILE = 'data/tasks.txt'

def load_tasks():
    tasks =[]
    try:
        with open(TASKS_FILE, 'r+') as file:
            for line in file:
                tasks.append(line.__str__())
    except FileExistsError:
        print("File does not exist")
    return tasks

def save_tasks(task_list):
    with open (TASKS_FILE, 'w') as file:
        for task in task_list:
            file.write(f"{task}\n")

def add_task(task):
    task_list = load_tasks()
    task_list.append(task)
    save_tasks(task_list)

def view_tasks():
    with open('task.txt', 'r') as file:
        tasks = file.readlines()
        for task in tasks:
            print(task)

def delete_task(task):
    try:
        task.delete(task)
        print("Task deleted successfully.")
    except ValueError:
        print("Task not found.")           

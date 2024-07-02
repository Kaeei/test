
class Task:
    def __init__(self, id, name, description, status, view, delete):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.view = view
        self.delete = delete
    
    def __str__(self):
        return f"Task id: {self.id}, Name: {self.name}, Description: {self.description}, Status: {self.status}, View: {self.view}, delete: {self.delete}"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def display_tasks(self):
        for task in self.tasks:
            print(task)
 
# Create a task manager object
task_manager = TaskManager()

# Create some tasks with all required arguments
task1 = Task(1, "Task 1", "Total tasks left to do", "Pending", "View1", "Delete1")
task2 = Task(2, "Task 2", "Task can not be done too busy", "Uncompleted", "View2", "Delete2")
task3 = Task(3, "Task 3", "Not in today, someone else to complete", "In Progress", "View3", "Delete3")

# Add tasks to the task manager
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

# Display all tasks
task_manager.display_tasks()

# Remove a task
task_manager.remove_task(2)

# Display all tasks again
task_manager.display_tasks()

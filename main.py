
# from models.task import Task
# from data.data_access import save_tasks, load_tasks, add_task, view_tasks, delete_task

# def main():
#     while True:
#         print("\nTask Manager")
#         print("1. Add Task")
#         print("2. View Task")
#         print("3. Load Tasks")
#         print("4. view tasks")
#         print("5.delete tasks")
#         print("6. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#                 id = input("Please enter a number: ")
#                 task_name = input("Enter task name: ")
#                 descripition = input("Enter task description: ")
#                 status = input("Completion status: ")
#                 view_tasks = input("All tasks shown")
#                 delete_task = input("task removed")
#                 task = Task(id, task_name, descripition, status, view_tasks, delete_task)
#                 add_task(task)
#         elif choice == "2":
#             task = input("Enter task to save: ")
#             save_tasks(task)
#         elif choice == "3":
#             load_tasks()
#         elif choice == "4":
#             view_tasks()
#         elif choice == "5":
#             task = input("Enter task to delete: ")
#             delete_task(task)    
#         elif choice == "6":
#             exit("Goodbye")
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()


from models.task import Task
from data.data_access import save_tasks, load_tasks, add_task, view_tasks, delete_task

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Save Task")
        print("3. Load Tasks")
        print("4. View Tasks")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter choice: ")
#User is inputing choices
        if choice == "1":
            id = input("Please enter a ID number: ")
            task_name = input("Enter task name: ")
            description = input("Enter task description: ")
            status = input("Completion status: ")
            view_task = input("All saved tasks shown")
            delete_task = input("selected task removed")
            task = Task(id, task_name, description, status, view_task, delete_task)
            add_task(task)
        elif choice == "2":
            task = input("Enter task to save: ")
            save_tasks(task)
        elif choice == "3":
            load_tasks()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            task = input("Enter task to delete: ")
            delete_task(task)    
        elif choice == "6":
            exit("Goodbye")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
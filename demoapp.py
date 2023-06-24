tasks = []

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def complete_task(task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
    else:
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' completed.")

while True:
    command = input("\nCommand [show/add/complete/exit]: ")
    if command == "show":
        show_tasks()
    elif command == "add":
        task = input("Enter task: ")
        add_task(task)
    elif command == "complete":
        task_index = int(input("Enter task index to complete: "))
        complete_task(task_index)
    elif command == "exit":
        break
    else:
        print("Invalid command.")

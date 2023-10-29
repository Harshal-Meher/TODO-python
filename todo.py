# To-Do List Application in Python

# Create an empty list to store tasks
tasks = []

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to mark a task as complete
def complete_task():
    list_tasks()
    task_number = int(input("Enter the task number you completed: "))
    if 1 <= task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task number. Please try again.")

# Function to remove a task
def remove_task():
    list_tasks()
    task_number = int(input("Enter the task number you want to remove: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number. Please try again.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

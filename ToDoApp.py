# ...........................
# TO-DO LIST PROJECT
# DecodeLabs - Project 1
# ............................

# Empty list to store tasks
tasks = []
# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    # Add task to list
    tasks.append(task)
    print("Task added successfully!\n")

# Function to view tasks
def view_tasks():
    # Check if list is empty
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("\nYour Tasks:")
        # Loop through all tasks
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

# Function to remove a task
def remove_task():
    # Check if tasks exist
    if len(tasks) == 0:
        print("No tasks to remove.\n")
        return
    # Show tasks first
    view_tasks()
    try:
        task_number = int(input("Enter task number to remove: "))
        # Remove selected task
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed}' removed successfully!\n")
    except:
        print("Invalid task number.\n")

# ....................Main program loop................
while True:
    print("..........................")
    print("  To-Do List ")
    print("..........................\n")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    # Menu conditions
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Thank you for using To-Do List App!")
        break
    else:
        print("Invalid choice. Try again.\n")
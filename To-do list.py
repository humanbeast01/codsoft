# To-Do List Program

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

# Function to view all tasks
def view_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Function to delete a task
def delete_task():
    task_number = int(input("Enter the task number to delete: "))
    try:
        del tasks[task_number - 1]
        print("Task deleted!")
    except IndexError:
        print("Invalid task number!")

# Main program loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice! Please try again.")

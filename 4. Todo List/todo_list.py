# List to store all tasks.
# Each task is a dictionary:
# {
#     "task": "Task name",
#     "done": False
# }
tasks = []


# Display the main menu
def show_menu():
    print("\n ----- TO-DO List -------")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


# Add a new task to the list
def add_task():
    print("Add Task Start")

    # Ask the user to enter a task
    task = input("Enter task: ")

    # Store the task as a dictionary
    # "task" -> task description
    # "done" -> completion status (False = not completed)
    tasks.append({"task": task, "done": False})

    print(f"Task '{task} added!'")
    print("Add Task End")


# Display all tasks
def view_task():

    # Check whether the task list is empty
    if not tasks:
        print("No tasks yet!")
        return

    print("\nYour Tasks:")

    # enumerate() gives:
    # index -> task number
    # task -> dictionary containing task information
    #
    # start=1 means numbering starts at 1 instead of 0.
    for index, task in enumerate(tasks, start=1):

        # Display check mark if task is completed
        # Otherwise display a blank space
        status = "✅" if task["done"] else " "

        # Example output:
        # 1. Learn Python [✅]
        print(f"{index}. {task['task']} [{status}]")


# Mark a task as completed
def mark_done():

    # Show all tasks first
    view_task()

    # Stop if there are no tasks
    if not tasks:
        return

    try:
        # User enters task number (1,2,3...)
        # Convert it to list index (0,1,2...)
        index = int(input("Enter task number to mark done: ")) - 1

        # Check whether the index exists
        if 0 <= index < len(tasks):

            # Update the "done" value to True
            tasks[index]["done"] = True

            print("Marked as done!")
        else:
            print("Invalid number!")

    # Handle invalid input (letters, symbols, etc.)
    except ValueError:
        print("Please enter a valid number.")


# Delete a task
def delete_task():

    # Show all tasks first
    view_task()

    if not tasks:
        return

    try:
        # Convert task number to list index
        index = int(input("Enter task number to delete: ")) - 1

        # Verify the index is valid
        if 0 <= index < len(tasks):

            # Remove the task from the list
            removed = tasks.pop(index)

            # removed is the deleted dictionary
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number!")

    except ValueError:
        print("Please enter a valid number")


# Main program loop
# Keep showing the menu until the user exits
while True:

    # Display menu
    show_menu()

    # Get user's choice
    choice = input("Choose an option (1-5): ")

    # Call the corresponding function
    if choice == '1':
        add_task()

    elif choice == '2':
        view_task()

    elif choice == '3':
        mark_done()

    elif choice == '4':
        delete_task()

    elif choice == '5':
        print("Good bye!")
        break

    # Handle invalid menu choice
    else:
        print("Invalid choose. Try Again")
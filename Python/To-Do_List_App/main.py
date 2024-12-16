# %%
"""
(Beginner)
To-Do List App: Create a simple command-line to-do list application where users can add, remove, and mark tasks as done.

What to achieve:
1. Crud operations (Create, Read, Update, Delete).
2. Repeat loop.
3. App logic function; 
    Displays options: Create tasks, View tasks, Update tasks, Delete tasks. 
    Takes input and handles error logic.
4. Create tasks function;
    Creates and Stores tasks.
    Limits tasks to 10.
    Checks if "Tasks.txt" file exceeds maximum allowed of 10.
    Option to save tasks to file.
5. View tasks function: 
6. Update tasks function: 
7. Delete tasks function: (TO-DO)
8. Additional functionality: 
    mark tasks as completed (TO-DO)
    Add functionality to see date/time of task creation.

Changes being made:
    12/15/2024: 
        Adding classes to implement Object Oriented Programming (OOP)
        Created modules for CRUD operations and utility operations
"""

# %%
# Logic function
class app_logic:

    def __init__(self) -> None:
        pass


# %%
def display():
    # Displays options
    print("To-Do List App by Ikenna Nicholas Ikwuka")
    print("1. Create new tasks")
    print("2. View tasks")
    print("3. Update tasks")
    print("4. Delete tasks")
    print("5. Quit")

    # Loop to take input and catch errors
    while True:
        # Validate user input and implements error handling.
        try:
            choice = int(input("What do you want to do?: "))

            if choice in range(1, 6):  # Checks input in range of 1 ~ 5
                return choice
            else:
                print("Invalid Input. Input a value from range 1 ~ 5")
        # Throw raised error or any unchecked errors
        except ValueError:  # Catches and displays ValueError for invalid types.
            print("Invalid Input. Input a number")
        except Exception as e:  # Catches and displays unexpected error.
            print(f"Unexpected error: {e}")


# %%
# Main function
def main():
    choice = app_logic()
    task_list = []
    match choice:
        case 1:
            task_list = create_tasks()
            print(f"Hi from main {task_list}")
            # save = input("Do you want to save your tasks?")
        case 2:
            update_tasks()
        case 3:
            ViewTasks()
        case 4:
            DeleteTasks()
        case 5:
            print("Thanks for using the app.")


# Starts here
main()

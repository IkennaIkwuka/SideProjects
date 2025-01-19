from src.main2 import TodolistApp

print("\nProgram starts...\n")

# Displays options
prompt = """
To-Do List App by Ikenna Nicholas Ikwuka
Here are the options: 
1. Add a task.
2. View your tasks.
3. Update a task.
4. Remove a task.
5. Quit the program.

"""


def main() -> None:
    app = TodolistApp()

    # Loop to take input and catch errors
    while (user_input := input(prompt + "What do you chose:")) != "5":
        if user_input.isdigit():
            match user_input := int(user_input):
                case 1:
                    app.add_tasks()
                case 2:
                    app.view_tasks()
                case 3:
                    app.update_tasks()
                case 4:
                    app.remove_tasks()
                case _:
                    print("Error: Invalid range.")
        else:
            print("Error: Invalid input\nHint: 'Q' to quit.")
    print("Thanks for using the app, Goodbye.")
    app.save_tasks()


if __name__ == "__main__":
    main()

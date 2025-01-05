from main import TODOLISTAPP

print("\nProgram starts...\n")

# Displays options
prompt_action_to_take = """
To-Do List App by Ikenna Nicholas Ikwuka
Here are the options: 
1. Add a task.
2. View your tasks.
3. Update a task.
4. Remove a task.
5. Save tasks.
6. Quit the program.

"""


def main() -> None:
    app = TODOLISTAPP()

    # Loop to take input and catch errors
    while (user_input := input(prompt_action_to_take + "What do you chose:")) != "6":
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
                case 5:
                    app.save_tasks()
                    break
                case _:
                    print("Error: Invalid range")
        else:
            print("Error: Invalid Integer")
    print("Thanks for using the app, Goodbye")


if __name__ == "__main__":
    main()

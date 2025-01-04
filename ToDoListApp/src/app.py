import main as mn

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
    # Loop to take input and catch errors
    while (user_input := input(prompt_action_to_take + "What do you chose:")) != "6":
        if user_input.isdigit():
            match user_input := int(user_input):
                case 1:
                    mn.add_tasks()
                case 2:
                    mn.view_tasks()
                case 3:
                    mn.update_tasks()
                case 4:
                    mn.remove_tasks()
                case 5:
                    # mn.save_tasks()
                    ...
                case _:
                    print("Error: Invalid range")
        else:
            print("Error: Invalid Integer")
    print("Thanks for using the app, Goodbye")


if __name__ == "__main__":
    main()

from ToDoListApp.src.main import App


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

What do you chose: 
"""

# Loop to take input and catch errors
while (user_input := input(prompt_action_to_take)) != "6":
    if user_input.isdigit():
        match user_input := int(user_input):
            case 1:
                App.add_tasks()
            case 2:
                App.view_tasks()
            case 3:
                App.update_tasks()
            case 4:
                App.remove_tasks()
            case 5:
                App.quit_program()
            case _:
                print("Error: Invalid range")
    else:
        print("Error: Invalid Integer")

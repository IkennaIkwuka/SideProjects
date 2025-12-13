# TODOLIST APP

import textwrap
from utils.python import interminal_text_editor, project_path_finder

CLOSING_MESSAGE = "\nClosing... Returning to menu\n"


def read_file(file):
    with open(file, "r") as f:
        yield from f


def write_to_file(file, tasks: list[str]):
    with open(file, "w") as f:
        for val in tasks:
            f.write(f"{val}\n")


class ToDoListApp:
    def __init__(self, task_file):
        self.task_file = task_file

        self.tasks_list = [line.strip() for line in read_file(task_file)]

    def run(self):
        self.control_hub()

    def control_hub(self):
        menu = """
        ToDoList App
        
        1. View Tasks
        
        2. Add Tasks
        
        3. Remove Tasks
        
        4. Edit Tasks
        """

        print(textwrap.dedent(menu))

        methods = (
            self.view_tasks,
            self.add_tasks,
            self.remove_tasks,
            self.edit_tasks,
        )

        while True:
            prompt_input = input(
                "\nWhat do you want to do? ('q' to Quit, 'm' for Menu)\n\n>   "
            ).strip()

            print()

            if not prompt_input:
                print("Input cannot be empty")
                continue

            if prompt_input.lower() == "q":
                print("Closing Todo List App, goodbye!...")
                break

            if prompt_input.lower() == "m":
                print(textwrap.dedent(menu))
                continue

            try:
                user_input = int(prompt_input)
            except ValueError:
                print(f"'{prompt_input}' is invalid. Please choose between '1' ~ '4'\n")
                continue

            if user_input in range(1, 5):
                methods[user_input - 1]()  # calls the selected method
                print()
            else:
                print(f"'{user_input}' is invalid. Please choose between '1' ~ '4'\n")

        write_to_file(self.task_file, self.tasks_list)

    def view_tasks(self):
        if len(self.tasks_list) == 0:
            print("You have no tasks to view, create some.\n")
            return

        print("Viewing tasks list...\n")

        for idx, val in enumerate(self.tasks_list, start=1):
            print(f"{idx}. {val}\n")

    def add_tasks(self):
        while True:
            user_input = input("\nTask to add ('q' to Quit)\n\n>    ").strip()

            if not user_input:
                print("input cannot be empty")
                continue

            if user_input.lower() == "q":
                print(CLOSING_MESSAGE)
                return

            if user_input in self.tasks_list:
                print(f"\nTask: '{user_input}' already exists.")
                continue

            self.tasks_list.append(user_input)

            print(f"\n'{user_input}' has been added to task list")

    def remove_tasks(self):
        if len(self.tasks_list) == 0:
            print("Cannot remove task as there are no tasks, create some.\n")
            return

        while True:
            prompt_input = input(
                "\nIndex of task to remove ('-1' to remove all, '0' to view tasks, 'q' to Quit)\n\n>    "
            ).strip()

            if prompt_input.lower() == "q":
                print(CLOSING_MESSAGE)
                return

            try:
                user_input = int(prompt_input)
            except ValueError:
                print(f"\n'{prompt_input}' is invalid. Please provide a valid index")
                continue

            if user_input == 0:
                self.view_tasks()
                continue

            if user_input == -1:
                self.tasks_list.clear()
                print("\nAll tasks have been cleared. Returning to menu...")
                return

            if user_input not in range(1, len(self.tasks_list) + 1):
                print(f"\n'{user_input}' is invalid. Please provide a valid index")
                continue

            val = self.tasks_list[user_input - 1]

            self.tasks_list.pop(user_input - 1)

            print(f"\nTask: '{val}' has been removed")

    def edit_tasks(self):
        if len(self.tasks_list) == 0:
            print("There are no tasks to edit, create some.\n")
            return

        while True:
            prompt_input = input(
                "\nIndex of task to edit ('0' to view tasks, 'q' to Quit)\n\n>    "
            ).strip()

            if not prompt_input:
                print("Input cannot be empty")
                continue

            if prompt_input.lower() == "q":
                print(CLOSING_MESSAGE)
                return

            try:
                user_input = int(prompt_input)
            except ValueError:
                print(f"\n'{prompt_input}' is invalid. Please provide a valid index")
                continue

            if user_input == 0:
                self.view_tasks()
                continue

            if user_input not in range(1, len(self.tasks_list) + 1):
                print(f"\n'{user_input}' is invalid. Please provide a valid index")
                continue

            updated_task = interminal_text_editor(
                f"\nEditing Task {user_input}: ", self.tasks_list[user_input - 1]
            )

            self.tasks_list[user_input - 1] = updated_task

            print(f"\nTask {user_input} updated to: '{updated_task}'")


# main method to run program
def run_app():
    task_file = project_path_finder(__file__, "docs", "Tasks.txt")
    app = ToDoListApp(task_file)
    app.run()


if __name__ == "__main__":
    run_app()
    ...

# TODOLIST APP

from pathlib import Path
import textwrap
from utils.python import project_path

TASK_FILE = project_path(__file__, "docs", "Tasks.txt")


def read_file(file: Path | str):
    """
    The function `read_file` reads a file line by line and yields each line as a string.

    :param file: The `file` parameter in the `read_file` function can accept either a `Path` object or a
    string representing the file path
    :type file: Path | str
    """
    with open(file, "r") as f:
        for line in f:
            yield line


def write_to_file(file: Path | str, list: list[str]):
    """
    The function writes a list of strings to a file, with each string on a new line.

    :param file: The `file` parameter in the `write_to_file` function is the path to the file where you
    want to write the list of strings. It can be either a `Path` object or a string representing the
    file path
    :type file: Path | str
    :param list: The `list` parameter in the `write_to_file` function is a list of strings that you want
    to write to the specified file. Each string in the list will be written to the file on a new line
    :type list: list[str]
    """

    with open(file, "w") as f:
        for val in list:
            f.write(f"{val}\n")


class ToDoListApp:
    def __init__(self):
        self.tasks_list = [line.strip() for line in read_file(TASK_FILE)]

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

        while True:
            user_input = input(
                "\nWhat do you want to do? ('q' to Quit)\n\n>   "
            ).strip()

            print()

            if user_input in ["Q", "q"]:
                print("Closing Todo List App, goodbye!...")
                break

            methods = (
                self.view_tasks,
                self.add_tasks,
                self.remove_tasks,
                self.edit_tasks,
            )

            error_msg = f"'{user_input}' is invalid. Please choose between '1' ~ '4'\n"

            if user_input.isdigit():
                user_input = int(user_input)

                if user_input in range(1, 5):
                    methods[user_input - 1]()  # calls the selected method

                    if len(self.tasks_list) >= 10:
                        print(textwrap.dedent(menu))
                    print()

                else:
                    print(error_msg)

            else:
                print(error_msg)

        write_to_file(TASK_FILE, self.tasks_list)

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

            if user_input in ["Q", "q"]:
                print("\nClosing... Returning to menu\n")
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
            prompt = input(
                "\nTask index to remove ('-1' to remove all, '0' to view tasks, 'q' to Quit)\n\n>    "
            ).strip()

            if prompt in ["Q", "q"]:
                print("\nClosing... Returning to menu\n")
                return

            try:
                user_input = int(prompt)
            except ValueError:
                print(f"\n'{prompt}' is invalid. Please provide a valid index")
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
        list_length = len(self.tasks_list)

        if list_length == 0:
            print("There are no tasks to edit.\n")
            return

        prompt = (
            "Provide the index of the task you would like to edit ('Q' to quit)\n: "
        )

        while True:
            user_input = input(prompt).strip()

            if user_input == "Q" or user_input == "q":
                print("Closing 'Edit Tasks' returning to menu...\n")
                return

            if (user_input != "Q" or user_input != "q") and not user_input.isdigit():
                print(
                    f"'{user_input}' is invalid. Please give a valid input ('Q' to quit)\n"
                )
                continue

            index = int(user_input)

            if index - 1 not in range(list_length):
                print(
                    f"'{index}' is invalid. Please give a valid index 1 ~ {list_length} ('Q' to quit)\n"
                )
                continue

            updated_task = input(
                f"You are now editing Task: '{index}. {self.tasks_list[index - 1]}' to ...\n: "
            )
            print(
                f"Task: '{index}. {self.tasks_list[index - 1]}' has been updated to '{updated_task}'\n"
            )

            self.tasks_list[index - 1] = updated_task

            prompt = "Edit another task? ('Q' to Quit)...\n: "

            with open(TASK_FILE, "w") as f:
                for i in self.tasks_list:
                    f.write(f"{i}\n")


# main method to run program
def run():
    ToDoListApp()


if __name__ == "__main__":
    run()

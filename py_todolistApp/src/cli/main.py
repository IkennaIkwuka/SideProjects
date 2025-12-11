# TODOLIST APP

import textwrap
from utils.python import project_path

TASK_FILE = project_path(__file__, "docs", "Tasks.txt")


def read_file(file):
    """
    Read a file line by line.
    This is a generator function that reads a file and yields each line,
    allowing for memory-efficient processing of large files.
    Args:
        file (str): The path to the file to be read.
    Yields:
        str: Each line from the file, including the newline character.
    Example:
        >>> for line in read_file('example.txt'):
        ...     print(line.strip())
    """

    with open(file, "r") as f:
        for line in f:
            yield line


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
            user_input = input("\nWhat do you want to do? ('q' to Quit)\n>   ").strip()

            print()

            if user_input in ["Q", "q"]:
                print("Closing Todo List App, goodbye!...")
                return

            methods = (
                self.view_tasks,
                self.add_tasks,
                self.remove_tasks,
                self.edit_tasks,
            )

            error_msg = f"'{user_input}' is invalid. Please choose between '1' ~ '4' ('q' to Quit)\n"

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

    def view_tasks(self):
        if len(self.tasks_list) == 0:
            print("You have no tasks to view, create some.\n")
            return

        print("Viewing tasks list...\n")

        for idx, val in enumerate(self.tasks_list, start=1):
            print(f"{idx}. {val}\n")

    def add_tasks(self):
        while True:
            user_input = input("\nTask to add ('q' to Quit)\n>    ").strip()

            if user_input in ["Q", "q"]:
                print("\nClosing... Returning to menu\n")
                return

            if user_input in self.tasks_list:
                print(f"\nTask: '{user_input}' already exists.")
                continue

            self.tasks_list.append(user_input)

            print(f"\n'{user_input}' has been added to task list")

    def remove_tasks(self):
        list_length = len(self.tasks_list)

        if list_length == 0:
            print("Cannot remove task as there are no tasks.\n")
            return

        prompt = "Give the index of the task you would like to remove ('0' to remove all tasks, 'Q' to quit)\n: "

        while True:
            user_input = input(prompt).strip()

            if user_input == "Q" or user_input == "q":
                print("Closing 'Remove Tasks' returning to menu...\n")
                return

            if (user_input != "Q" or user_input != "q") and not user_input.isdigit():
                print(
                    f"'{user_input}' is invalid. Please give a valid index ('0' to remove all tasks, 'Q' to quit)\n"
                )
                continue

            index = int(user_input)

            if index == 0:
                self.tasks_list.clear()
                print("Clearing all tasks...\n")
                print("All tasks have been cleared. Returning to menu...\n")
                return

            if index - 1 not in range(list_length):
                print(
                    f"{index} is invalid. Please give a valid index 1 ~ {list_length} ('0' to remove all tasks, 'Q' to quit)\n"
                )
                continue

            print(f"Task: '{index}. {self.tasks_list[index - 1]}' has been removed\n")

            self.tasks_list.pop(index - 1)

            prompt = "Remove more? ('0' to remove all tasks, 'Q' to quit)\n: "

            with open(TASK_FILE, "w") as f:
                for i in self.tasks_list:
                    f.write(f"{i}\n")

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

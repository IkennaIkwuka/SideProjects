# TODOLIST APP

import textwrap

from prompt_toolkit import prompt
from utils.python import project_path_finder
from py_todolistApp.src.cli.logic import AppLogic


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

        if task_file.exists():
            self.tasks_list = [line.strip() for line in read_file(task_file)]
        else:
            self.tasks_list = []

        self.logic = AppLogic(self.tasks_list)

        self.menu = textwrap.dedent("""
        ToDoList App
        
        1. View Tasks
        
        2. Add Tasks
        
        3. Remove Tasks
        
        4. Edit Tasks
        """)

        self.output_returns = {
            "quit": "\nClosing... Returning to menu\n",
            "empty": "Input cannot be empty",
            "out of range": "\nOut of index range.",
            "invalid": "\nInvalid input for index.",
            "exists": "\nTask already exists.",
        }

        self.actions = {
            1: self.view_tasks,
            2: self.add_tasks,
            3: self.remove_tasks,
            4: self.edit_tasks,
        }

    def run(self):
        self.control_hub()
        write_to_file(self.task_file, self.tasks_list)

    def control_hub(self):
        while True:
            print(self.menu)

            user_input = input(
                "\nProvide the index of what you want to do? ('q' to Quit)\n\n>   "
            ).strip()

            output = self.logic._handle_control_hub(user_input, self.actions)

            if output == "quit":
                print(self.output_returns["quit"])
                break
            elif isinstance(output, int):
                if not self.tasks_list:
                    print("There are no tasks, add some first.\n")
                    self.actions[2]()
                else:
                    self.actions[output]()
            else:
                print(self.output_returns[output])

    def view_tasks(self):
        print("\nViewing tasks list...\n")

        for idx, val in enumerate(self.tasks_list, start=1):
            print(f"{idx}. {val}\n")

    def add_tasks(self):
        while True:
            user_input = input("\nTask to add ('q' to Quit)\n\n>    ").strip()

            output = self.logic._handle_add_tasks(user_input)

            if output == "quit":
                print(self.output_returns["quit"])
                break
            elif output in self.output_returns:
                print(self.output_returns[output])
            else:
                self.tasks_list.append(output)
                print("\nTask added")

    def remove_tasks(self):
        while True:
            user_input = input(
                "\nIndex of task to remove ('d' to remove all tasks, 'v' to view all tasks, 'q' to Quit)\n\n>    "
            ).strip()

            output = self.logic._handle_remove_tasks(user_input)

            if output == "quit":
                print(self.output_returns["quit"])
                break
            elif output == "del":
                self.tasks_list.clear()
                print("\nAll tasks have been deleted.")
                break
            elif output == "view":
                self.actions[1]()
            elif isinstance(output, int):
                index = output
                self.tasks_list.pop(index - 1)
                print("\nTask removed.")
            else:
                print(self.output_returns[output])

    def edit_tasks(self):
        while True:
            user_input = input(
                "\nIndex of task to edit ('v' to view tasks, 'q' to Quit)\n\n>    "
            ).strip()

            output = self.logic._handle_edit_tasks(user_input)

            if output == "quit":
                print(self.output_returns["quit"])
                break
            elif output == "view":
                self.actions[1]()
            elif isinstance(output, int):
                index = output
                self.tasks_list[index - 1] = self._get_updated_task(index)
                print("\nTask updated.")
            else:
                print(self.output_returns[output])

    def _get_updated_task(self, index):
        while True:
            updated_task = prompt(
                f"\nEditing Task {index}: ", default=self.tasks_list[index - 1]
            )

            if not updated_task:
                self.output_returns["empty"]
            else:
                return updated_task


# main method to run program
def run_app():
    task_file = project_path_finder(__file__, "docs", "Tasks.txt")
    app = ToDoListApp(task_file)
    app.run()


if __name__ == "__main__":
    run_app()
    ...

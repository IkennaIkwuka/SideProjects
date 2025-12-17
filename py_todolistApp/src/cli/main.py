# TODOLIST APP

import textwrap

from prompt_toolkit import prompt
from utils.python import project_path_finder
from py_todolistApp.src.cli.logic import AppLogic, TaskStatus

SHELL_OUTPUTS = {
    TaskStatus.QUIT: "\nClosing... Returning to menu\n",
    TaskStatus.EMPTY: "Input cannot be empty",
    TaskStatus.OUT_OF_RANGE: "\nOut of index range.",
    TaskStatus.INVALID: "\nInvalid input for index.",
    TaskStatus.EXISTS: "\nTask already exists.",
}


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

    def run(self):
        self.hub()
        write_to_file(self.task_file, self.tasks_list)

    def hub(self):
        actions = {
            1: self.view_tasks,
            2: self.add_tasks,
            3: self.remove_tasks,
            4: self.edit_tasks,
        }
        menu = textwrap.dedent("""
        ToDoList App ('q' to Quit)
        
        1. View Tasks
        
        2. Add Tasks
        
        3. Remove Tasks
        
        4. Edit Tasks
        
        """)
        while True:
            print(menu)

            user_input = input("> ").strip()

            result = self.logic.validate_hub(user_input, actions)

            if isinstance(result, TaskStatus):
                if result == TaskStatus.QUIT:
                    print(SHELL_OUTPUTS[result])
                    break
                print(SHELL_OUTPUTS[result])
            else:
                if self.logic.force_add_tasks(result):
                    print("There are no tasks, add some first.\n")
                    self.add_tasks()
                else:
                    actions[result]()

    def view_tasks(self):
        print("\nViewing tasks list...\n")
        for idx, task in enumerate(self.tasks_list, start=1):
            print(f"{idx}. {task}\n")

    def add_tasks(self):
        while True:
            user_input = input("\nTask to add ('q' to Quit)\n\n> ").strip()

            result = self.logic.validate_add_tasks(user_input)

            if isinstance(result, TaskStatus):
                print(SHELL_OUTPUTS[result])
                if result == TaskStatus.QUIT:
                    break
            else:
                self.tasks_list.append(result)
                print("\nTask added")

    def remove_tasks(self):
        while True:
            user_input = input(
                "\nIndex to remove ('d' delete all, 'v' view tasks, 'q' to Quit)\n\n>    "
            ).strip()

            result = self.logic.validate_remove_tasks(user_input)

            if isinstance(result, TaskStatus):
                if result == TaskStatus.QUIT:
                    print(SHELL_OUTPUTS[result])
                    break

                if result == TaskStatus.DELETE_ALL:
                    self.tasks_list.clear()
                    print("\nAll tasks have been deleted.")
                    break

                if result == TaskStatus.VIEW:
                    self.view_tasks()
            else:
                self.tasks_list.pop(result - 1)
                print("\nTask removed.")

    def edit_tasks(self):
        while True:
            user_input = input(
                "\nIndex to edit ('v' view tasks, 'q' to Quit)\n\n>    "
            ).strip()

            result = self.logic.validate_edit_tasks(user_input)

            if isinstance(result, TaskStatus):
                if result == TaskStatus.QUIT:
                    print(SHELL_OUTPUTS[result])
                    break

                if result == TaskStatus.VIEW:
                    self.view_tasks()
            else:
                self.tasks_list[result - 1] = self._updated_task(result)
                print("\nTask updated.")

    def _updated_task(self, index: int):
        while True:
            updated_task = prompt(
                f"\nEditing Task {index}: ", default=self.tasks_list[index - 1]
            )

            result = self.logic.validate_updated_task(updated_task)

            if isinstance(result, TaskStatus):
                print(SHELL_OUTPUTS[result])
            else:
                return result


# main method to run program
def run_app():
    task_file = project_path_finder(__file__, "docs", "Tasks.txt")
    ToDoListApp(task_file).run()


if __name__ == "__main__":
    run_app()
    ...

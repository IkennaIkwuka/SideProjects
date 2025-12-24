# TODOLIST APP

from pathlib import Path
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


def read_file(file_path: Path):
    with open(file_path, "r") as f:
        yield from f


def save_file(file_path: Path, tasks: list[str]):
    with open(file_path, "w") as f:
        for val in tasks:
            f.write(f"{val}\n")


class ToDoListApp:
    def __init__(self, task_file: Path | str):
        self.task_file = Path(task_file)

        self.tasks = (
            [line.strip() for line in read_file(Path(task_file))]
            if self.task_file.exists()
            else []
        )

        self.logic = AppLogic(self.tasks)

    def run(self):
        actions = {
            1: self.view_tasks,
            2: self.add_tasks,
            3: self.remove_tasks,
            4: self.edit_tasks,
        }
        while True:
            print(
                textwrap.dedent("""
                ToDoList App ('q' to Quit)
                
                1. View Tasks
                
                2. Add Tasks
                
                3. Remove Tasks
                
                4. Edit Tasks
                
                """)
            )

            user_input = input("> ").strip()

            result = self.logic.validate_hub(user_input, actions)

            if isinstance(result, TaskStatus):
                if result == TaskStatus.QUIT:
                    print(SHELL_OUTPUTS[TaskStatus.QUIT])
                    return
                else:
                    print(SHELL_OUTPUTS[result])
            else:
                if self.logic.force_add_tasks(result):
                    print("\nThere are no tasks, add some first.\n")
                else:
                    actions[result]()
                    save_file(self.task_file, self.tasks)

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks to view.\n")
            return

        print("\nViewing tasks list...\n")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}\n")

    def add_tasks(self):
        while True:
            user_input = input("\nTask to add ('q' to Quit)\n\n> ").strip()

            result = self.logic.validate_add_tasks(user_input)

            if isinstance(result, TaskStatus):
                if result == TaskStatus.QUIT:
                    print(SHELL_OUTPUTS[TaskStatus.QUIT])
                    return
                else:
                    print(SHELL_OUTPUTS[result])
            elif isinstance(result, str):
                self.tasks.append(result)
                print("\nTask added\n")

    def remove_tasks(self):
        if not self.tasks:
            print("\nNo tasks to remove.\n")
            return

        while True:
            user_input = input(
                "\nIndex to remove ('d' delete all, 'v' view tasks, 'q' to Quit)\n\n>    "
            ).strip()

            result = self.logic.validate_remove_tasks(user_input)

            if isinstance(result, TaskStatus):
                if result == TaskStatus.QUIT:
                    print(SHELL_OUTPUTS[TaskStatus.QUIT])
                    return
                elif result == TaskStatus.DELETE_ALL:
                    self.tasks.clear()
                    print("\nAll tasks have been deleted.")
                    return
                elif result == TaskStatus.VIEW:
                    self.view_tasks()
                else:
                    print(SHELL_OUTPUTS[result])
            elif isinstance(result, int):
                self.tasks.pop(result - 1)
                print("\nTask removed.\n")

    def edit_tasks(self):
        if not self.tasks:
            print("\nNo tasks to edit.\n")
            return

        while True:
            user_input = input(
                "\nIndex to edit ('v' view tasks, 'q' to Quit)\n\n>    "
            ).strip()

            result = self.logic.validate_edit_tasks(user_input)

            if isinstance(result, TaskStatus):
                if result == TaskStatus.QUIT:
                    print(SHELL_OUTPUTS[TaskStatus.QUIT])
                    return
                elif result == TaskStatus.VIEW:
                    self.view_tasks()
                else:
                    print(SHELL_OUTPUTS[result])
            elif isinstance(result, int):
                self.tasks[result - 1] = self._updated_task(result)
                print("\nTask updated.\n")

    def _updated_task(self, index: int):
        while True:
            updated_task = prompt(
                f"\nEditing Task {index}: ", default=self.tasks[index - 1]
            )

            result = self.logic.validate_updated_task(updated_task)

            if isinstance(result, TaskStatus):
                print(SHELL_OUTPUTS[result])
            elif isinstance(result, str):
                return result


# main method to run program
def main():
    task_file = project_path_finder(__file__, "docs", "Tasks.txt")
    ToDoListApp(task_file).run()


if __name__ == "__main__":
    main()
    ...

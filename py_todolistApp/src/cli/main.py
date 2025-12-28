# TODOLIST APP

from pathlib import Path
from prompt_toolkit import prompt
from py_todolistApp.src.cli.logic import AppLogic, TaskStatus

MESSAGES = {
    TaskStatus.QUIT: "\nClosing... Returning to menu\n",
    TaskStatus.EMPTY: "\nInput cannot be empty",
    TaskStatus.OUT_OF_RANGE: "\nOut of index range.",
    TaskStatus.INVALID: "\nInvalid input for index.",
    TaskStatus.EXISTS: "\nTask already exists.",
}


class ToDoListApp:
    def __init__(self, file: Path | str, logic: AppLogic | None = None):
        self.file = Path(file)
        self.tasks = self._read(self.file)
        self.logic = logic or AppLogic(self.tasks)

    def _read(self, file: Path):
        if file.exists():
            return [line.strip() for line in file.read_text().splitlines()]
        return []

    def _save(self, file: Path, tasks: list[str]):
        file.write_text("\n".join(tasks))

    def run(self):
        methods = (self.view_tasks, self.add_tasks, self.remove_tasks, self.edit_tasks)

        while True:
            print(
                "\nToDoList App ('q' to Quit)\n1. View Tasks\n2. Add Tasks\n3. Remove Tasks\n4. Edit Tasks\n"
            )

            choice = input("> ").strip()

            result = self.logic.validate_hub(choice, methods)

            if result == TaskStatus.QUIT:
                print(MESSAGES[TaskStatus.QUIT])
                return

            if isinstance(result, TaskStatus):
                print(MESSAGES[result])
            else:
                methods[result - 1]()
                self._save(self.file, self.tasks)

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks to view.\n")
            return

        print("\nViewing tasks list...\n")

        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def add_tasks(self):
        while True:
            print("\nTask to add ('q' to Quit)\n\n")

            choice = input("> ").strip()

            result = self.logic.validate_add_tasks(choice)

            if result == TaskStatus.QUIT:
                print(MESSAGES[TaskStatus.QUIT])
                return

            if isinstance(result, TaskStatus):
                print(MESSAGES[result])
            else:
                self.tasks.append(result)
                print("\nTask added")

    def remove_tasks(self):
        if not self.tasks:
            print("\nNo tasks to remove.\n")
            return

        while True:
            print("\nIndex to remove ('d' delete all, 'v' view tasks, 'q' to Quit)\n\n")

            choice = input("> ").strip()

            result = self.logic.validate_remove_tasks(choice)

            if result == TaskStatus.QUIT:
                print(MESSAGES[TaskStatus.QUIT])
                return

            if result == TaskStatus.DELETE_ALL:
                print("\nAre you sure you want to delete all tasks? (y/n)\n\n")

                _choice = input("> ").strip().lower()

                _result = self.logic.delete_all_confirmation(_choice)

                if _result is True:
                    self.tasks.clear()
                    print("\nAll tasks have been deleted.")
                    return
                elif _result is False:
                    break

                print("\nInvalid input. Please enter 'y' or 'n'.")

            if result == TaskStatus.VIEW:
                self.view_tasks()
                continue

            if isinstance(result, TaskStatus):
                print(MESSAGES[result])
            else:
                self.tasks.pop(result - 1)
                print("\nTask removed.")

    def edit_tasks(self):
        if not self.tasks:
            print("\nNo tasks to edit.\n")
            return

        while True:
            print("\nIndex to edit ('v' view tasks, 'q' to Quit)\n\n")

            choice = input("> ").strip()

            result = self.logic.validate_edit_tasks(choice)

            if result == TaskStatus.QUIT:
                print(MESSAGES[TaskStatus.QUIT])
                return

            if result == TaskStatus.VIEW:
                self.view_tasks()
                continue

            if isinstance(result, TaskStatus):
                print(MESSAGES[result])
            else:
                self.tasks[result - 1] = self._updated_task(result)
                print("\nTask updated.")

    def _updated_task(self, index: int):
        while True:
            updated_task = prompt("\nEditing: ", default=self.tasks[index - 1])

            result = self.logic.validate_updated_task(updated_task)

            if isinstance(result, TaskStatus):
                print(MESSAGES[result])
            else:
                return result


# main method to run program
def main():
    from utils.python import project_path_finder

    file = project_path_finder(__file__, "docs", "Tasks.txt")
    ToDoListApp(file).run()


if __name__ == "__main__":
    main()

# TODOLIST APP

from pathlib import Path
from prompt_toolkit import prompt
from py_todolistApp.src.cli.logic import AppLogic, TaskStatus


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
        app_menu = (self.view_tasks, self.add_tasks, self.remove_tasks, self.edit_tasks)

        while True:
            print(
                "\nToDoList App ('q' to Quit)\n1. View Tasks\n2. Add Tasks\n3. Remove Tasks\n4. Edit Tasks\n"
            )

            choice = input("> ").strip()

            result = self.logic.run(choice, app_menu)

            if isinstance(result, int):
                app_menu[result - 1]()
                self._save(self.file, self.tasks)
                continue

            if result == TaskStatus.QUIT:
                print("\nExiting ToDoList App. Goodbye!\n")
                return

            print("\n" + self.logic.get_message(result))

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks to view.\n")
            return

        print("\nViewing tasks list...\n")

        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def add_tasks(self):
        while True:
            print("\nTask to add ('q' to Quit)\n")

            choice = input("> ").strip()

            result = self.logic.add_tasks(choice)

            if isinstance(result, str):
                self.tasks.append(result)
                print("\nTask added")
                continue

            if result == TaskStatus.QUIT:
                return

            if result == TaskStatus.EXISTS:
                print("\n" + self.logic.get_message(result))
                continue

            print("\n" + self.logic.get_message(result))

    def remove_tasks(self):
        if not self.tasks:
            print("\nNo tasks to remove.\n")
            return

        while True:
            print("\nIndex to remove ('d' delete all, 'v' view tasks, 'q' to Quit)\n\n")

            choice = input("> ").strip()

            result = self.logic.remove_tasks(choice)

            if isinstance(result, int):
                self.tasks.pop(result - 1)
                print("\nTask removed.")
                continue

            if result == TaskStatus.QUIT:
                return

            if result == TaskStatus.DELETE_ALL:
                if self._delete_all_confirmation():
                    self.tasks.clear()
                    print("\nAll tasks have been deleted.")
                    return
                else:
                    continue

            if result == TaskStatus.VIEW:
                self.view_tasks()
                continue

            print("\n" + self.logic.get_message(result))

    def _delete_all_confirmation(self):
        while True:
            print("\nAre you sure you want to delete all tasks? (y/n)\n")

            _choice = input("> ").strip()

            _result = self.logic.delete_all_confirmation(_choice)

            if _result == TaskStatus.INVALID:
                print("\nInvalid input. Please enter 'y' or 'n'.")
                continue

            if _result:
                return True
            else:
                return False

    def edit_tasks(self):
        if not self.tasks:
            print("\nNo tasks to edit.\n")
            return

        while True:
            print("\nIndex to edit ('v' view tasks, 'q' to Quit)\n\n")

            choice = input("> ").strip()

            result = self.logic.edit_tasks(choice)

            if isinstance(result, int):
                self.tasks[result - 1] = self._updated_task(result)
                print("\nTask updated.")
                continue

            if result == TaskStatus.QUIT:
                return

            if result == TaskStatus.VIEW:
                self.view_tasks()
                continue

            print("\n" + self.logic.get_message(result))

    def _updated_task(self, index: int):
        while True:
            updated_task = prompt("\nEditing: ", default=self.tasks[index - 1])

            _result = self.logic.updated_task(updated_task)

            if isinstance(_result, str):
                return _result

            print(self.logic.get_message(_result))


# main method to run program
def main():
    from utils.python import project_path_finder

    file = project_path_finder(__file__, "docs", "Tasks.txt")
    ToDoListApp(file).run()


if __name__ == "__main__":
    main()

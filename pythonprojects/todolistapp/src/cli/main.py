# ToDoList APP

from pathlib import Path
from prompt_toolkit import prompt
from src.cli.logic import AppLogic
from src.cli.io import TodoIO


class ToDoListApp:
    def __init__(self, file: Path | str):
        self.io = TodoIO(file)
        self.logic = AppLogic()

    def run(self):
        self.menu()
        self.io.save()

    def menu(self):
        while True:
            print(
                "\nToDoList App ('q' to Quit)\n1. Create Tasks\n2. View Tasks\n3. Remove Tasks\n4. Edit Tasks\n"
            )

            input_ = input("> ").strip()

            action = self.logic.menu(input_)

            if not action:
                continue

            if action == "q":
                print("\nExiting ToDoList App. Goodbye!\n")
                break

            if isinstance(action, int):
                match action:
                    case 1:
                        self.create_task()
                    case 2:
                        self.view_tasks()
                    case 3:
                        self.remove_tasks()
                    case 4:
                        self.edit_tasks()
                    case _:
                        pass  #

    def view_tasks(self):
        if not self.io.display_tasks():
            print("\nError: No tasks.\n")
            return None

    def create_task(self):
        while True:
            print("\nTask to add ('q' for menu)\n")

            _input = input("> ").strip()

            task = self.logic.create_tasks(_input)

            if not task:
                continue

            if task == "q":
                break

            if isinstance(task, str):
                self.io.task_stored(task)

    def remove_tasks(self):
        if not self.io.tasks:
            print("\nNo tasks to remove.\n")
            return None

        while True:
            print(
                "\nIndex to remove ('d' delete all, 'v' view tasks, 'q' for Menu)\n\n"
            )

            choice = input("> ").strip()

            index = self.logic.remove_tasks(choice)

            if not index:
                continue

            if index == "q":
                break

            if index == "d":
                if self._delete_all_confirmation():
                    self.tasks.clear()
                    print("\nAll tasks have been deleted.")
                break

            if index == "v":
                self.view_tasks()
                continue

            self.tasks.pop(index - 1)

            print("\nTask removed.")

    def _delete_all_confirmation(self) -> bool:
        while True:
            confirm = input("\nAre you sure?(y/n)\n> ").strip().lower()

            if confirm not in ["y", "n"]:
                print("\nInvalid input\n")
                continue
            return confirm == "y"

    def edit_tasks(self):
        if not self.tasks:
            print("\nNo tasks to edit.\n")
            return

        while True:
            print("\nIndex to edit ('v' view tasks, 'q' to Menu)\n\n")

            choice = input("> ").strip()

            index = self.logic.edit_tasks(choice)

            if not index:
                continue

            if index == "q":
                break

            if index == "v":
                self.view_tasks()
                continue

            self.tasks[index - 1] = self._updated_task(index)

            print("\nTask updated.")

    def _updated_task(self, index: int) -> str:
        while True:
            updated_task = prompt("\nEditing: ", default=self.tasks[index - 1])

            _result = self.logic.updated_task(updated_task)

            if not _result:
                continue

            return _result


# main method to run program
def main():
    ToDoListApp("docs/Tasks.txt").run()


if __name__ == "__main__":
    main()  # For quick testing

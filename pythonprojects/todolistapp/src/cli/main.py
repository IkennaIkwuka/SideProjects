# ToDoList APP

from pathlib import Path
from prompt_toolkit import prompt
from src.cli.logic import AppLogic
from src.cli.io import TodoIO


class ToDoListApp:
    ERROR_NO_TASKS = "\nError: No tasks.\n"

    def __init__(self, file: Path | str):
        self.io = TodoIO(file)
        self.logic = AppLogic()

    def run(self):
        self.app_menu()
        self.io.save()

    def app_menu(self):
        while True:
            print(
                "\nToDoList App ('q' to Quit)\n1. Create Tasks\n2. View Tasks\n3. Remove Tasks\n4. Edit Tasks\n"
            )

            input_ = input("> ").strip()

            action = self.logic.app_menu(input_, 4)

            if action is None:
                continue

            if action == "q":
                print("\nExiting ToDoList App. Goodbye!\n")
                break

            if isinstance(action, int):
                match action:
                    case 1:
                        self.create_tasks()
                    case 2:
                        self.view_tasks()
                    case 3:
                        self.remove_tasks()
                    case 4:
                        self.edit_tasks()
                    case _:
                        pass  #

    def view_tasks(self):
        if not self.io.get_tasks():
            print(self.ERROR_NO_TASKS)
            return None
        print("\nViewing tasks list...\n")
        self.io.display_tasks()

    def create_tasks(self):
        while True:
            print("\nTask to add ('q' app_menu)\n")

            _input = input("> ").strip()

            task = self.logic.create_tasks(_input)

            if task is None:
                continue

            if task == "q":
                break

            if isinstance(task, str):
                self.io.store_task(task)

    def remove_tasks(self):
        if not self.io.get_tasks():
            print(self.ERROR_NO_TASKS)
            return None

        while True:
            print("\nIndex to remove ('d' delete all, 'v' view tasks, 'q' Menu)\n\n")

            choice = input("> ").strip()

            index = self.logic.remove_tasks(choice)

            if index is None:
                continue

            if index == "q":
                break

            elif index == "d":
                if self._confirm_del() and self.io.clear_all():
                    print("\nAll tasks have been deleted.")
                break

            elif index == "v":
                self.view_tasks()
                continue

            if isinstance(index, int):
                self.io.delete_task(index)

    def _confirm_del(self):
        while True:
            confirm = input("\nAre you sure?(y/n)\n> ").strip().lower()

            if confirm not in ["y", "n"]:
                print("\nInvalid input\n")
                continue
            return confirm == "y"

    def edit_tasks(self):
        if not self.io.get_tasks():
            print(self.ERROR_NO_TASKS)
            return None

        while True:
            print("\nIndex to edit ('v' view tasks, 'q' Menu)\n\n")

            choice = input("> ").strip()

            index = self.logic.edit_tasks(choice)

            if index is None:
                continue

            if index == "q":
                break

            elif index == "v":
                self.view_tasks()
                continue

            if isinstance(index, int):
                self.io.edit_task_content(index, self._get_new_task(index))

    def _get_new_task(self, index):
        while True:
            updated_task = prompt(
                "\nEditing: ", default=self.io.get_tasks()[index - 1]
            ).strip()

            if not updated_task:
                print("Error: Missing input.")
                continue

            return updated_task


# main method to run program
def main():
    ToDoListApp("docs/Tasks.txt").run()


if __name__ == "__main__":
    main()  # For quick testing

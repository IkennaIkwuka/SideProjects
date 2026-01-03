# ToDoList APP

from pathlib import Path
from prompt_toolkit import prompt
from src.cli.services.logic import AppLogic


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
        self.menu()
        self._save(self.file, self.tasks)

    def menu(self):
        while True:
            print(
                "\nToDoList App ('q' to Quit)\n1. View Tasks\n2. Add Tasks\n3. Remove Tasks\n4. Edit Tasks\n"
            )

            choice = input("> ").strip()

            result = self.logic.menu(choice)

            if not result:
                continue

            if result == "q":
                print("\nExiting ToDoList App. Goodbye!\n")
                break

            match result:
                case 1:
                    self.view_tasks()
                case 2:
                    self.add_tasks()
                case 3:
                    self.remove_tasks()
                case 4:
                    self.edit_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks to view.\n")
            return

        print("\nViewing tasks list...\n")

        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def add_tasks(self):
        while True:
            print("\nTask to add ('q' for menu)\n")

            choice = input("> ").strip()

            result = self.logic.add_tasks(choice)

            if not result:
                continue

            if result == "q":
                break

            self.tasks.append(result)

            print("\nTask added")

    def remove_tasks(self):
        if not self.tasks:
            print("\nNo tasks to remove.\n")
            return

        while True:
            print("\nIndex to remove ('d' delete all, 'v' view tasks, 'q' to Quit)\n\n")

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
            if confirm == "y":
                return True
            return False

    def edit_tasks(self):
        if not self.tasks:
            print("\nNo tasks to edit.\n")
            return

        while True:
            print("\nIndex to edit ('v' view tasks, 'q' to Quit)\n\n")

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

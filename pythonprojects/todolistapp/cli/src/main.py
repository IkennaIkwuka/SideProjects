# ToDoList APP

from pathlib import Path
from prompt_toolkit import prompt
from cli.src.control import TodoControl
from cli.src.model import TodoModel
from cli.src.view import TodoView


class ToDoListApp:
    ERROR_NO_TASKS = "\nError: No tasks.\n"

    def __init__(self, file: Path | str):
        self.model = TodoModel(file)
        self.logic = TodoControl()
        self.view = TodoView()

    def run(self):
        self.app_menu()

    def app_menu(self):
        while True:
            self.view.menu()
            input_ = prompt("> ").strip()
            action = self.logic.app_menu(input_)

            if action == "q":
                print("\nExiting ToDoList App. Goodbye!\n")
                break

            if action and isinstance(action, int):
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

    def create_tasks(self):
        while True:
            self.view.console.print(
                "\nTask to add ('q' app_menu)\n", style="bold white on magenta"
            )

            str_input = input("> ").strip()
            tasks: list[str] = self.model.get_tasks()
            task = self.logic.validate_task_str(str_input, tasks)

            if task == "q":
                break

            if task and task != "q":
                self.model.store_task(task)
                self.view.success("Task added!")

    def view_tasks(self):
        tasks: list[str] = self.model.get_tasks()
        if not tasks:
            print(self.ERROR_NO_TASKS)
            return None
        self.view.show_tasks(tasks)

    def remove_tasks(self):
        while True:
            tasks: list[str] = self.model.get_tasks()
            if not tasks:
                print(self.ERROR_NO_TASKS)
                return None

            print("\nIndex to remove ('d' delete all, 'v' view tasks, 'q' Menu)\n\n")

            choice = input("> ").strip()
            index = self.logic.validate_task_index(choice, tasks)

            if index == "q":
                break
            elif index == "d":
                if self._confirm_del():
                    self.model.clear_all()
                    print("\nAll tasks have been deleted.")
                break
            elif index == "v":
                self.view_tasks()
                continue

            if isinstance(index, int):
                self.model.delete_task(index)
                print("\nTask deleted.")

    def _confirm_del(self):
        while True:
            confirm = input("\nAre you sure?(y/n)\n> ").strip().lower()

            if confirm not in ["y", "n"]:
                print("\nInvalid input\n")
                continue
            return confirm == "y"

    def edit_tasks(self):
        while True:
            tasks: list[str] = self.model.get_tasks()
            if not tasks:
                print(self.ERROR_NO_TASKS)
                return None

            print("\nIndex to edit ('v' view tasks, 'q' Menu)\n\n")

            choice = input("> ").strip()
            index = self.logic.validate_task_index(choice, tasks)
            if index == "q":
                break
            if index == "v":
                self.view_tasks()
                continue

            if isinstance(index, int):
                updated_task = prompt("\nEditing: ", default=tasks[index - 1]).strip()
                task = self.logic.validate_task_str(updated_task, tasks)

                if isinstance(task, str) and task != "q":
                    self.model.edit_task_content(index, updated_task)
                    print("\nTask updated.")


# main method to run program
def main():
    ToDoListApp("docs/Tasks.txt").run()


if __name__ == "__main__":
    main()  # For quick testing

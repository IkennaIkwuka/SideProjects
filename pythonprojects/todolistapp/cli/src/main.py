# ToDoList APP

from pathlib import Path
from prompt_toolkit import prompt
from cli.src.control import TodoControl
from cli.src.model import TodoModel
from cli.src.view import TodoView


class ToDoListApp:
    ERROR_NO_TASKS = "No tasks."

    def __init__(self, file: Path | str):
        self.model = TodoModel(file)
        self.view = TodoView()
        self.control = TodoControl(self.view)

    def run(self):
        menu_action = {
            1: self.create_tasks,
            2: self.view_tasks,
            3: self.remove_tasks,
            4: self.edit_tasks,
        }
        while True:
            self.view.menu()
            action = self.control.app_menu(prompt("> ").strip())

            if action == "q":
                print("\nExiting ToDoList App. Goodbye!\n")
                break

            if action and isinstance(action, int) and action in menu_action:
                menu_action[action]()

    def create_tasks(self):
        while True:
            self.view.action("Task to add ('q' app_menu)")

            tasks: list[str] = self.model.get_tasks()
            task = self.control.validate_task_str(prompt("> ").strip(), tasks)

            if task == "q":
                break

            if task and task != "q":
                self.model.store_task(task)
                self.view.success("Task added!")

    def view_tasks(self):
        tasks: list[str] = self.model.get_tasks()
        if not tasks:
            self.view.warning(self.ERROR_NO_TASKS)
            return None
        self.view.show_tasks(tasks)

    def remove_tasks(self):
        while True:
            tasks: list[str] = self.model.get_tasks()
            if not tasks:
                self.view.warning(self.ERROR_NO_TASKS)
                return None

            self.view.action(
                "Index to remove ('d' delete all, 'v' view tasks, 'q' Menu)"
            )

            index = self.control.validate_task_index(prompt("> ").strip(), tasks)

            if index == "q":
                break
            elif index == "d":
                if self._confirm_del():
                    self.model.clear_all()
                    self.view.success("All tasks have been deleted!")
                break
            elif index == "v":
                self.view_tasks()
                continue

            if index and isinstance(index, int):
                self.model.delete_task(index)
                self.view.success("Task deleted!")

    def _confirm_del(self) -> bool:
        while True:
            confirm = prompt("\nAre you sure?(y/n)\n> ").strip().lower()

            if confirm not in ["y", "n"]:
                self.view.warning("Invalid prompt")
                continue
            return confirm == "y"

    def edit_tasks(self):
        while True:
            tasks: list[str] = self.model.get_tasks()
            if not tasks:
                self.view.warning(self.ERROR_NO_TASKS)
                return None

            self.view.action("Index to edit ('v' view tasks, 'q' Menu)")

            index = self.control.validate_task_index(prompt("> ").strip(), tasks)
            if index == "q":
                break
            if index == "v":
                self.view_tasks()
                continue

            if isinstance(index, int):
                updated_task = prompt("\nEditing: ", default=tasks[index - 1]).strip()
                task = self.control.validate_task_str(updated_task, tasks)

                if isinstance(task, str) and task != "q":
                    self.model.edit_task_content(index, updated_task)
                    self.view.success("Task updated!")


# main method to run program
def main():
    ToDoListApp("db/tasks.sqlite").run()


if __name__ == "__main__":
    main()  # For quick testing

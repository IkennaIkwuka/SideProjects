# ToDoList APP (SQLite version)

from pathlib import Path
from prompt_toolkit import prompt
from cli.src.control import TodoControl
from cli.src.model import TodoModel
from cli.src.view import TodoView


class ToDoListApp:
    ERROR_NO_TASKS = "No tasks."

    def __init__(self, db_file: Path | str):
        self.model = TodoModel(db_file)
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

            if isinstance(action, int) and action in menu_action:
                menu_action[action]()

    # ---------------- CREATE ---------------- #

    def create_tasks(self):
        while True:
            self.view.action("Task to add ('q' Menu)")

            tasks = [t[0] for t in self.model.get_tasks()]
            task = self.control.validate_task_str(prompt("> ").strip(), tasks)

            if task == "q":
                break

            if task:
                self.model.store_task(task)
                self.view.success("Task added!")

    # ---------------- VIEW ---------------- #

    def view_tasks(self):
        tasks = self.model.get_tasks()
        if not tasks:
            self.view.warning(self.ERROR_NO_TASKS)
            return

        self.view.show_tasks(tasks)

    # ---------------- REMOVE ---------------- #

    def remove_tasks(self):
        while True:
            tasks = self.model.get_tasks()
            if not tasks:
                self.view.warning(self.ERROR_NO_TASKS)
                return

            self.view.action("Index to remove ('d' delete all, 'v' view, 'q' Menu)")

            index = self.control.validate_task_index(
                prompt("> ").strip(),
                [t[0] for t in tasks],
            )

            if index == "q":
                break
            elif index == "d":
                if self._confirm_del():
                    self.model.clear_all()
                    self.view.success("All tasks deleted!")
                break
            elif index == "v":
                self.view_tasks()
                continue

            if isinstance(index, int):
                self.model.delete_task(index)
                self.view.success("Task deleted!")

    # ---------------- EDIT / TOGGLE ---------------- #

    def edit_tasks(self):
        while True:
            tasks = self.model.get_tasks()
            if not tasks:
                self.view.warning(self.ERROR_NO_TASKS)
                return

            self.view.action(
                "Index to edit | 't' toggle complete | 'v' view | 'q' Menu"
            )

            index = self.control.validate_task_index(
                prompt("> ").strip(),
                [t[0] for t in tasks],
            )

            if index == "q":
                break
            if index == "v":
                self.view_tasks()
                continue
            if index == "t":
                index = self._ask_index(tasks, "Toggle which task?")
                if index:
                    self.model.toggle_complete(index)
                    self.view.success("Task status updated!")
                continue

            if isinstance(index, int):
                current_task = tasks[index - 1][0]
                updated_task = prompt("\nEditing: ", default=current_task).strip()

                existing_tasks = [t[0] for t in tasks]
                validated = self.control.validate_task_str(updated_task, existing_tasks)

                if isinstance(validated, str):
                    self.model.edit_task_content(index, updated_task)
                    self.view.success("Task updated!")

    # ---------------- HELPERS ---------------- #

    def _confirm_del(self) -> bool:
        while True:
            confirm = prompt("\nAre you sure? (y/n)\n> ").strip().lower()
            if confirm in ("y", "n"):
                return confirm == "y"
            self.view.warning("Invalid prompt.")

    def _ask_index(self, tasks, msg: str):
        self.view.action(msg)
        try:
            index = int(prompt("> ").strip())
            if 1 <= index <= len(tasks):
                return index
            self.view.error("Invalid task index.")
        except ValueError:
            self.view.warning("Not a number.")
        return None


def main():
    ToDoListApp("db/tasks.sqlite").run()


if __name__ == "__main__":
    main()

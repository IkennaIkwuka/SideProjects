from cli.src.view import TodoView


class TodoControl:
    def __init__(self) -> None:
        self.view = TodoView()

    def app_menu(self, action: str):
        if not action:
            self.view.warning("Missing input.")
            return None

        if action == "q":
            return "q"

        try:
            idx = int(action)
            if 1 <= idx <= 4:
                return idx
            else:
                self.view.error("Invalid task index.")
        except ValueError:
            self.view.warning("Not a number.")
        return None

    def validate_task_str(self, task: str, current_tasks: list[str]):
        if not task:
            self.view.warning("Missing input.")
            return None
        if task.lower() == "q":
            return "q"
        if task in current_tasks:
            self.view.error("Task already exists.")
            return None
        return task

    def validate_task_index(self, choice: str, current_tasks: list[str]):
        if not choice:
            return None
        if choice.lower() == "q":
            return "q"
        if choice.lower() == "d":
            return "d"
        if choice.lower() == "v":
            return "v"

        try:
            idx = int(choice)
            if 1 <= idx <= len(current_tasks):
                return idx
            else:
                self.view.error("Invalid task index.")
        except ValueError:
            self.view.warning("Not a number.")
        return None


if __name__ == "__main__":
    ...  # For quick testing

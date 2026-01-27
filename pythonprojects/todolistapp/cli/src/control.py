from cli.src.view import TodoView


class TodoControl:
    def __init__(self, view: TodoView) -> None:
        self.view = view

    def app_menu(self, uinput: str):
        if not uinput:
            self.view.warning("Missing input.")
            return None
        if uinput.lower() == "q":
            return "q"
        try:
            idx = int(uinput)
            if 1 <= idx <= 4:
                return idx
            else:
                self.view.error("Invalid task index.")
        except ValueError:
            self.view.warning("Not a number.")
        return None

    def validate_task_str(self, uinput: str, current_tasks: list[str]):
        if not uinput:
            self.view.warning("Missing input.")
            return None
        if uinput.strip().lower() == "q":
            return "q"
        if uinput in current_tasks:
            self.view.error("Task already exists.")
            return None
        return uinput

    def validate_task_index(self, uinput: str, current_tasks: list[str]):
        if not uinput:
            return None
        cmds = ["q", "d", "v", "t"]
        if uinput.strip().lower() in cmds:
            return uinput.strip().lower()
        try:
            idx = int(uinput)
            if 1 <= idx <= len(current_tasks):
                return idx
            else:
                self.view.error("Invalid task index.")
        except ValueError:
            self.view.warning("Not a number.")
        return None


if __name__ == "__main__":
    ...  # For quick testing

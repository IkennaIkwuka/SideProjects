from src.cli.models.status import TaskStatus


class AppLogic:
    def __init__(
        self, tasks: list[str] | None = None, status: TaskStatus | None = None
    ):
        self.tasks = tasks or []
        self.status = status or TaskStatus

    # ----------------------------
    # Helper methods (NEW)
    # ----------------------------

    def _is_quit(self, value: str) -> bool:
        return value.lower() == "q"

    def _is_delete_all(self, value: str) -> bool:
        return value.lower() == "d"

    def _is_view(self, value: str) -> bool:
        return value.lower() == "v"

    def _parse_index(self, value: str, menu_options: tuple | None = None):
        try:
            index = int(value)
            if 1 <= index <= len(menu_options or self.tasks):
                return index
            return self.status.OUT_OF_RANGE
        except ValueError:
            return self.status.INVALID

    # ----------------------------
    # Public validation methods
    # ----------------------------

    def menu(self, choice: str, menu_options: tuple):
        choice = choice.strip()

        if self._is_quit(choice):
            return self.status.QUIT

        return self._parse_index(choice, menu_options)

    def add_tasks(self, choice: str):
        choice = choice.strip()

        if self._is_quit(choice):
            return self.status.QUIT

        if choice in self.tasks:
            return self.status.EXISTS

        return choice or self.status.INVALID

    def remove_tasks(self, choice: str):
        choice = choice.strip()

        if self._is_quit(choice):
            return self.status.QUIT

        if self._is_delete_all(choice):
            return self.status.DELETE_ALL

        if self._is_view(choice):
            return self.status.VIEW

        return self._parse_index(choice)

    def delete_all_confirmation(self, choice: str):
        choice = choice.strip()

        if choice.lower() == "y":
            return True
        if choice.lower() == "n":
            return False
        return self.status.INVALID

    def edit_tasks(self, choice: str):
        choice = choice.strip()

        if self._is_quit(choice):
            return self.status.QUIT

        if self._is_view(choice):
            return self.status.VIEW

        return self._parse_index(choice)

    def updated_task(self, choice: str):
        choice = choice.strip()

        if choice in self.tasks:
            return self.status.EXISTS

        return choice or self.status.INVALID

    def get_message(self, status: TaskStatus) -> str:
        match status:
            case self.status.OUT_OF_RANGE:
                return "Out of range."
            case self.status.INVALID:
                return "Invalid input."
            case self.status.EXISTS:
                return "Task exists."
            case _:
                return ""


if __name__ == "__main__":
    ...  # For quick testing

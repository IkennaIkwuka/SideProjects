from enum import Enum, auto


class TaskStatus(Enum):
    EMPTY = auto()
    QUIT = auto()
    INVALID = auto()
    OUT_OF_RANGE = auto()
    EXISTS = auto()
    DELETE_ALL = auto()
    VIEW = auto()


class AppLogic:
    def __init__(self, tasks: list[str] | None = None):
        self.tasks = tasks or []

    # ----------------------------
    # Helper methods (NEW)
    # ----------------------------

    def _is_quit(self, value: str) -> bool:
        return value.lower() == "q"

    def _is_delete_all(self, value: str) -> bool:
        return value.lower() == "d"

    def _is_view(self, value: str) -> bool:
        return value.lower() == "v"

    def _parse_index(self, value: str, app_menu: tuple | None = None):
        try:
            index = int(value)
            if 1 <= index <= len(app_menu or self.tasks):
                return index
            return TaskStatus.OUT_OF_RANGE
        except ValueError:
            return TaskStatus.INVALID

    # ----------------------------
    # Public validation methods
    # ----------------------------

    def run(self, choice: str, app_menu: tuple):
        choice = choice.strip()

        if self._is_quit(choice):
            return TaskStatus.QUIT

        return self._parse_index(choice, app_menu)

    def add_tasks(self, choice: str):
        choice = choice.strip()

        if self._is_quit(choice):
            return TaskStatus.QUIT

        if choice in self.tasks:
            return TaskStatus.EXISTS

        return choice or TaskStatus.INVALID

    def remove_tasks(self, choice: str):
        choice = choice.strip()

        if self._is_quit(choice):
            return TaskStatus.QUIT

        if self._is_delete_all(choice):
            return TaskStatus.DELETE_ALL

        if self._is_view(choice):
            return TaskStatus.VIEW

        return self._parse_index(choice)

    def delete_all_confirmation(self, choice: str):
        choice = choice.strip()

        if choice.lower() == "y":
            return True
        if choice.lower() == "n":
            return False
        return TaskStatus.INVALID

    def edit_tasks(self, choice: str):
        choice = choice.strip()

        if self._is_quit(choice):
            return TaskStatus.QUIT

        if self._is_view(choice):
            return TaskStatus.VIEW

        return self._parse_index(choice)

    def updated_task(self, choice: str):
        choice = choice.strip()

        if choice in self.tasks:
            return TaskStatus.EXISTS

        return choice or TaskStatus.INVALID

    def get_message(self, status: TaskStatus) -> str:
        match status:
            case TaskStatus.OUT_OF_RANGE:
                return "Out of range."
            case TaskStatus.INVALID:
                return "Invalid input."
            case TaskStatus.EXISTS:
                return "Task exists."
            case _:
                return ""

from enum import Enum, auto


class TaskStatus(str, Enum):
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

    def _is_empty(self, value: str) -> bool:
        return not value

    def _is_quit(self, value: str) -> bool:
        return value.lower() == "q"

    def _is_delete_all(self, value: str) -> bool:
        return value.lower() == "d"

    def _is_view(self, value: str) -> bool:
        return value.lower() == "v"

    def _parse_index(self, value: str, methods: tuple | None = None):
        try:
            index = int(value)
            if 1 <= index <= len(methods or self.tasks):
                return index
            return TaskStatus.OUT_OF_RANGE
        except ValueError:
            return TaskStatus.INVALID

    # ----------------------------
    # Public validation methods
    # ----------------------------

    def validate_hub(self, choice: str, methods: tuple):
        if self._is_empty(choice):
            return TaskStatus.EMPTY

        if self._is_quit(choice):
            return TaskStatus.QUIT

        return self._parse_index(choice, methods)

    def validate_add_tasks(self, choice: str):
        if self._is_empty(choice):
            return TaskStatus.EMPTY

        if self._is_quit(choice):
            return TaskStatus.QUIT

        if choice in self.tasks:
            return TaskStatus.EXISTS

        return choice

    def validate_remove_tasks(self, choice: str):
        if self._is_empty(choice):
            return TaskStatus.EMPTY

        if self._is_quit(choice):
            return TaskStatus.QUIT

        if self._is_delete_all(choice):
            return TaskStatus.DELETE_ALL

        if self._is_view(choice):
            return TaskStatus.VIEW

        return self._parse_index(choice)

    def delete_all_confirmation(self, choice: str) -> None | bool:
        if choice.lower() == "y":
            return True
        if choice.lower() == "n":
            return False

    def validate_edit_tasks(self, choice: str):
        if self._is_empty(choice):
            return TaskStatus.EMPTY

        if self._is_quit(choice):
            return TaskStatus.QUIT

        if self._is_view(choice):
            return TaskStatus.VIEW

        return self._parse_index(choice)

    def validate_updated_task(self, choice: str):
        if self._is_empty(choice):
            return TaskStatus.EMPTY

        if choice in self.tasks:
            return TaskStatus.EXISTS

        return choice

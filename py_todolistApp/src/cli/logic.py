from enum import Enum


class TaskStatus(str, Enum):
    EMPTY = "empty"
    QUIT = "quit"
    INVALID = "invalid"
    OUT_OF_RANGE = "out of range"
    EXISTS = "exists"
    DELETE_ALL = "del"
    VIEW = "view"


class AppLogic:
    def __init__(self, tasks: list[str] | None = None):
        self.tasks = tasks or []

    def validate_hub(self, user_input: str, actions: dict):
        if not user_input.strip():
            return TaskStatus.EMPTY
        if user_input.lower() == "q":
            return TaskStatus.QUIT
        try:
            index = int(user_input)
        except ValueError:
            return TaskStatus.INVALID
        if not 1 <= index <= len(actions):
            return TaskStatus.OUT_OF_RANGE
        return index

    def force_add_tasks(self, selected_action: int):
        if not self.tasks and selected_action != 2:
            return True
        return False

    def validate_add_tasks(self, user_input: str):
        if not user_input.strip():
            return TaskStatus.EMPTY
        if user_input.lower() == "q":
            return TaskStatus.QUIT
        if user_input in self.tasks:
            return TaskStatus.EXISTS
        return user_input

    def _validate_return_index(self, user_input: str, delete_all=True):
        if not user_input.strip():
            return TaskStatus.EMPTY
        lowered = user_input.lower().strip()
        if lowered == "q":
            return TaskStatus.QUIT
        if delete_all and lowered == "d":
            return TaskStatus.DELETE_ALL
        if lowered == "v":
            return TaskStatus.VIEW
        try:
            index = int(user_input)
        except ValueError:
            return TaskStatus.INVALID
        if not 1 <= index <= len(self.tasks):
            return TaskStatus.OUT_OF_RANGE
        return index

    def validate_remove_tasks(self, user_input: str):
        return self._validate_return_index(user_input, delete_all=True)

    def validate_edit_tasks(self, user_input: str):
        return self._validate_return_index(user_input, delete_all=False)

    def validate_updated_task(self, user_input: str):
        if not user_input.strip():
            return TaskStatus.EMPTY
        if user_input in self.tasks:
            return TaskStatus.EXISTS
        return user_input

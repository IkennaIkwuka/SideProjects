# Define constants for return codes
class TaskStatus:
    EMPTY = "empty"
    QUIT = "quit"
    INVALID = "invalid"
    OUT_OF_RANGE = "out of range"
    EXISTS = "exists"
    DELETE_ALL = "del"
    VIEW = "view"


class AppLogic:
    def __init__(self, tasks: list[str] | None = None):
        self.tasks_list = tasks or []

    def _handle_control_hub(self, user_input: str, actions: dict):
        if not user_input:
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

    def _handle_add_tasks(self, user_input: str):
        if not user_input:
            return TaskStatus.EMPTY
        if user_input.lower() == "q":
            return TaskStatus.QUIT
        if user_input in self.tasks_list:
            return TaskStatus.EXISTS
        return user_input

    def _handle_remove_tasks(self, user_input: str):
        if not user_input:
            return TaskStatus.EMPTY
        if user_input.lower() == "q":
            return TaskStatus.QUIT
        if user_input.lower() == "d":
            return TaskStatus.DELETE_ALL
        if user_input.lower() == "v":
            return TaskStatus.VIEW
        if user_input in self.tasks_list:
            return TaskStatus.EXISTS
        try:
            index = int(user_input)
        except ValueError:
            return TaskStatus.INVALID
        if not 1 <= index <= len(self.tasks_list):
            return TaskStatus.OUT_OF_RANGE
        return index

    def _handle_edit_tasks(self, user_input: str):
        if not user_input:
            return TaskStatus.EMPTY
        if user_input.lower() == "q":
            return TaskStatus.QUIT
        if user_input.lower() == "v":
            return TaskStatus.VIEW
        try:
            index = int(user_input)
        except ValueError:
            return TaskStatus.INVALID
        if not 1 <= index <= len(self.tasks_list):
            return TaskStatus.OUT_OF_RANGE
        return index

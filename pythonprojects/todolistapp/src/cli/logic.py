class AppLogic:
    ERROR_NOT_A_NUMBER = "Error: Not a number."
    ERROR_OUT_OF_RANGE = "Error: Out of range."
    ERROR_MISSING_INPUT = "Error: Missing input."

    def __init__(self, tasks: list[str] | None = None):
        self.tasks = tasks or []

    def _is_quit(self, value: str) -> bool:
        return value.lower() == "q"

    def _is_delete_all(self, value: str) -> bool:
        return value.lower() == "d"

    def _is_view(self, value: str) -> bool:
        return value.lower() == "v"

    def _is_number(self, input_str: str) -> bool:
        try:
            int(input_str)
            return True
        except ValueError:
            return False

    def menu(self, choice: str):
        if not choice:
            print(self.ERROR_MISSING_INPUT)
            return

        choice = choice.strip()

        if self._is_quit(choice):
            return "q"

        if not self._is_number(choice):
            print(self.ERROR_NOT_A_NUMBER)
            return

        if not 1 <= int(choice) <= 4:
            print(self.ERROR_OUT_OF_RANGE)
            return

        return int(choice)

    def add_tasks(self, choice: str):
        if not choice:
            print(self.ERROR_MISSING_INPUT)
            return

        choice = choice.strip()

        if self._is_quit(choice):
            return "q"

        if choice in self.tasks:
            print("Task exists")
            return

        return choice

    def remove_tasks(self, choice: str):
        if not choice:
            print(self.ERROR_MISSING_INPUT)
            return

        choice = choice.strip()

        if self._is_quit(choice):
            return "q"

        if self._is_delete_all(choice):
            return "d"

        if self._is_view(choice):
            return "v"

        if not self._is_number(choice):
            print(self.ERROR_NOT_A_NUMBER)
            return

        if not 1 <= int(choice) <= len(self.tasks):
            print(self.ERROR_OUT_OF_RANGE)
            return

        return int(choice)

    def edit_tasks(self, choice: str):
        if not choice:
            print(self.ERROR_MISSING_INPUT)
            return

        choice = choice.strip()

        if self._is_quit(choice):
            return "q"

        if self._is_view(choice):
            return "v"

        if not self._is_number(choice):
            print(self.ERROR_NOT_A_NUMBER)
            return

        if not 1 <= int(choice) <= len(self.tasks):
            print(self.ERROR_OUT_OF_RANGE)
            return

        return int(choice)

    def updated_task(self, choice: str):
        if not choice:
            print(self.ERROR_MISSING_INPUT)
            return

        choice = choice.strip()

        if choice in self.tasks:
            print("Task exists")
            return

        return choice


if __name__ == "__main__":
    ...  # For quick testing

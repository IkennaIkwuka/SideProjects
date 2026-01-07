class AppLogic:
    ERROR_NOT_A_NUMBER = "Error: Not a number."
    ERROR_OUT_OF_RANGE = "Error: Out of range."
    ERROR_MISSING_INPUT = "Error: Missing input."

    def __is_quit(self, value: str) -> bool:
        return value.lower() == "q"

    def __is_delete_all(self, value: str) -> bool:
        return value.lower() == "d"

    def __is_view(self, value: str) -> bool:
        return value.lower() == "v"

    def __is_number(self, input_str: str) -> bool:
        try:
            int(input_str)
            return True
        except ValueError:
            return False

    def app_menu(self, _input: str, number_of_actions: int):
        if not _input:
            print(self.ERROR_MISSING_INPUT)
            return None

        action = _input.strip()

        if self.__is_quit(action):
            return "q"

        if not self.__is_number(action):
            print(self.ERROR_NOT_A_NUMBER)
            return None

        if not 1 <= int(action) <= number_of_actions:
            print(self.ERROR_OUT_OF_RANGE)
            return None

        return int(action)

    def create_tasks(self, _input: str):
        if not _input:
            print(self.ERROR_MISSING_INPUT)
            return None

        task = _input.strip()

        if self.__is_quit(task):
            return "q"

        return task

    def remove_tasks(self, choice: str):
        if not choice:
            print(self.ERROR_MISSING_INPUT)
            return

        choice = choice.strip()

        if self.__is_quit(choice):
            return "q"

        if self.__is_delete_all(choice):
            return "d"

        if self.__is_view(choice):
            return "v"

        if not self.__is_number(choice):
            print(self.ERROR_NOT_A_NUMBER)
            return

        return int(choice)

    def edit_tasks(self, choice: str):
        if not choice:
            print(self.ERROR_MISSING_INPUT)
            return

        choice = choice.strip()

        if self.__is_quit(choice):
            return "q"

        if self.__is_view(choice):
            return "v"

        if not self.__is_number(choice):
            print(self.ERROR_NOT_A_NUMBER)
            return

        return int(choice)


if __name__ == "__main__":
    ...  # For quick testing

class AppLogic:
    def __is_quit(self, value: str) -> bool:
        return value.lower() == "q"

    def __is_delete_all(self, value: str) -> bool:
        return value.lower() == "d"

    def __is_view(self, value: str) -> bool:
        return value.lower() == "v"

    def __is_input_missing(self, value: str):
        if not value:
            print("Error: Missing input.")
            return True
        return False

    def __is_number(self, input_str: str) -> bool:
        try:
            int(input_str)
            return True
        except ValueError:
            print("Error: Not a number.")
            return False

    def app_menu(self, value: str, number_of_actions: int):
        if self.__is_input_missing(value):
            return None

        action = value.strip()

        if self.__is_quit(action):
            return "q"

        if not self.__is_number(action):
            return None

        if not 1 <= int(action) <= number_of_actions:
            print("Error: Out of range.")
            return None

        return int(action)

    def create_tasks(self, value: str):
        if self.__is_input_missing(value):
            return None

        task = value.strip()

        if self.__is_quit(task):
            return "q"

        return task

    def remove_tasks(self, choice: str):
        if self.__is_input_missing(choice):
            return None

        choice = choice.strip()

        if self.__is_quit(choice):
            return "q"

        if self.__is_delete_all(choice):
            return "d"

        if self.__is_view(choice):
            return "v"

        if not self.__is_number(choice):
            return

        return int(choice)

    def edit_tasks(self, choice: str):
        if self.__is_input_missing(choice):
            return None

        choice = choice.strip()

        if self.__is_quit(choice):
            return "q"

        if self.__is_view(choice):
            return "v"

        if not self.__is_number(choice):
            return None

        return int(choice)


if __name__ == "__main__":
    ...  # For quick testing

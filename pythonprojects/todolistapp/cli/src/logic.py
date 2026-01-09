from cli.src.console import TodoView


class TodoLogic:
    def __init__(self, tasks: list[str]) -> None:
        self.cons = TodoView()
        self.tasks = tasks

    def __is_quit(self, value: str) -> bool:
        return value.lower() == "q"

    def __is_delete_all(self, value: str) -> bool:
        return value.lower() == "d"

    def __is_view(self, value: str) -> bool:
        return value.lower() == "v"

    def __is_task_index_invalid(self, index: int):
        if index <= 0 or index > len(self.tasks):
            print("Error: Invalid task index.")
            return True
        else:
            return False

    def __is_input_missing(self, value: str):
        if not value:
            self.cons.warning("Warning: Missing input.")
            return True
        else:
            return False

    def __is_not_number(self, input_str: str) -> bool:
        try:
            int(input_str)
            return False
        except ValueError:
            self.cons.warning("Warning: Not a number.")
            return True

    def __does_task_exist(self, task: str):
        if task in self.tasks:
            print("Error: Task already exist.")
            return True
        else:
            return False

    def app_menu(self, action: str):
        NUMBER_OF_ACTIONS = 4

        if self.__is_input_missing(action):
            return None
        if self.__is_quit(action):
            return "q"
        if self.__is_not_number(action):
            return None

        act = int(action)
        if not 1 <= act <= NUMBER_OF_ACTIONS:
            self.cons.warning("Warning: Out of range.")
            return None

        return act

    def create_tasks(self, task: str):
        if self.__is_input_missing(task):
            return None
        if self.__does_task_exist(task):
            return None
        if self.__is_quit(task):
            return "q"

        return task

    def remove_tasks(self, choice: str):
        if self.__is_input_missing(choice):
            return None
        if self.__is_quit(choice):
            return "q"
        if self.__is_delete_all(choice):
            return "d"
        if self.__is_view(choice):
            return "v"
        if self.__is_not_number(choice):
            return

        index = int(choice)
        if self.__is_task_index_invalid(index):
            return None

        return index

    def edit_tasks(self, choice: str):
        if self.__is_input_missing(choice):
            return None
        if self.__is_quit(choice):
            return "q"
        if self.__is_view(choice):
            return "v"
        if self.__is_not_number(choice):
            return None

        index = int(choice)
        if self.__is_task_index_invalid(index):
            return None

        return index

    def get_updated_task(self, task: str):
        if self.__is_input_missing(task):
            return None
        if self.__does_task_exist(task):
            return None
        return task


if __name__ == "__main__":
    ...  # For quick testing

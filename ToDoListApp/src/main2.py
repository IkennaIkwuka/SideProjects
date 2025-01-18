import os

from src.sql.dbms import DBMS

"""
The provided Python script is a To-Do List application that allows users to manage tasks by adding, viewing, updating, and removing them, with the ability to save tasks to a file and load them back when the program restarts.

# TODO Things to fix:
    Duplication error // fixed
    Methods not responding appropriately when file is full //  fixed


# TODO Things to add:
    Add a functionality that removes content in program's list that exceeds max file length // added
    functionality that prevents modification of file outside program // added
    Implement a way to ask user if the want to create a new file when file is full // not added

"""

# Check if directory exists, if not create it.
os.makedirs("docs/", exist_ok=True)


class TodolistApp(DBMS):
    def __init__(self):
        super().__init__("Tasks")
        self.tasks: list[str] = []
        self.max_length = 10
        self.__file_name = "Tasks"
        self.path_to_file: str = f"docs/{self.file_name}.txt"
        self.get_file_contents()

    @property
    def file_name(self) -> str:
        DBMS.create(self, "book", [("", "", [""])])
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name: str):
        self.__file_name: str = file_name

    def add_tasks(self):
        msg = "You have expended all your space for creating tasks, you can either view, update, or remove tasks for more space."

        if len(self.tasks) >= self.max_length:
            print(msg)
            return

        create_task: str = self.ask_for_task("Create", "Task")

        # Add task title and task description
        self.tasks.append(create_task.strip())

        print("Tasks created successfully...")

    def view_tasks(self):
        if self.is_tasks_empty("view"):
            return

        for index, task in enumerate(self.tasks, start=1):
            print(f"\nTask {index}. {task} ")

    def update_tasks(self):
        if self.is_tasks_empty("update"):
            return

        index: int = self.ask_for_index("update", len(self.tasks))

        if index == 0:
            print("Closing update tasks...")
            return

        update_task: str = self.ask_for_task("Update", "Task")

        # Update title and description
        self.tasks[int(index)] = update_task

        print("Task updated successfully...")

    def remove_tasks(self):
        if self.is_tasks_empty("remove"):
            return

        index: int = self.ask_for_index("remove", len(self.tasks))

        if index == 0:
            print("Closing remove tasks...")
            return

        # Removes tasks
        self.tasks.pop(int(index))

        print("Task deleted successfully...")

    def save_tasks(self):
        if self.is_tasks_empty("save"):
            return

        # file_name: str = self.file_name
        try:
            with open(self.path_to_file, "a") as file:
                for task in self.tasks:
                    file.writelines(f"Task. {task}\n")
            print(f"Tasks saved to {self.file_name}.txt successfully")
        except FileNotFoundError:
            print(f"Error: File {self.file_name}.txt not found")

    def get_file_contents(self):
        try:
            with open(f"{self.path_to_file}", "r") as file:
                _file: list[str] = file.readlines()

                print("File read successfully")

                if len(_file) <= self.max_length:
                    file_list = [
                        item.strip("Task.").strip()
                        for item in _file
                        if item.startswith("Task")
                    ]
                    self.tasks.extend(file_list)
                else:
                    print("File contents exceeds program limit")
                    print("Creating new file...")
                    self.create_new_file()
        except FileNotFoundError:
            print("Error: No File found")
            print("Creating new file...")
            self.create_task_file(self.file_name)

    def create_task_file(self, file_name: str):
        try:
            with open(f"docs/{file_name}.txt", "x") as file:
                file.writelines([])
            print(f"File {file_name} created successfully")
        except FileExistsError:
            print(
                f"Error: File {file_name}.txt already exist.\nHint: Use a different name"
            )

    def create_new_file(self):
        while (
            user_input := input("Please give the file a name(No spaces in between): ")
            .strip()
            .title()
        ):
            if not user_input.isalpha():
                print(f"Error: {user_input} is not a valid file name")
                continue
            self.create_task_file(user_input)
            break
        self.file_name = user_input

    def is_tasks_empty(self, func_name: str) -> bool:
        msg: str = f"You dont have any tasks, create some to {func_name}."

        if len(self.tasks) == 0:
            print(msg)
            return True
        return False

    def ask_for_task(self, method_name: str, action_word: str) -> str:
        while not (user_input := input(f"{method_name} {action_word}: ").strip()):
            print(f"{action_word} cannot be empty.")
        return user_input

    def ask_for_index(self, action_word: str, list_length: int) -> int:
        prompt: str = f"What task would you like to {action_word} or 'Q' to quit: "
        err_msg: str = f"Please choose a valid index between 1 and {list_length}."

        while (user_input := input(prompt).upper().strip()) != "Q":
            if not user_input.isdigit():
                print("Not an integer")
                continue

            user_input = int(user_input) - 1
            if user_input in range(list_length):
                return user_input
            else:
                print(err_msg)

        return 0


# Starts here
if __name__ == "__main__":
    # create_new_file()
    app = TodolistApp()
    print(app.tasks)
    ...
    # app = App(10, "cmd/docs/Tasks.txt")

import os

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


class TODOLISTAPP:
    def __init__(self):
        self.tasks: list[str] = []
        self.max_length = 10
        self.__file_name = "Tasks"
        self.path_to_file: str = f"docs/{self.file_name}.txt"
        self.get_file_contents()

    @property
    def file_name(self) -> str:
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name: str):
        self.__file_name: str = file_name

    def add_tasks(self):
        msg = "You have expended all your space for creating tasks, you can either view, update, or delete tasks for more space.\n"

        if len(self.tasks) >= self.max_length:
            print(msg)
            return

        create_task: str = self.ask_for_task("Create", "Task")

        # Add task title and task description
        self.tasks.append(create_task.strip())

        print("\nTasks created successfully...\n")

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
            print("\nClosing update tasks...\n")

        update_task: str = self.ask_for_task("Update", "Task")

        # Update title and description
        self.tasks[int(index)] = update_task

        print("\nTask updated successfully...\n")

    def remove_tasks(self):
        if self.is_tasks_empty("remove"):
            return

        index: int = self.ask_for_index("remove", len(self.tasks))

        if index == 0:
            print("\nClosing remove tasks...\n")

        # Removes tasks
        self.tasks.pop(int(index))

        print("\nTask deleted successfully...\n")

    def save_tasks(self):
        if self.is_tasks_empty("save"):
            return

        file_name: str = self.file_name
        try:
            with open(self.path_to_file, "a") as file:
                for index, task in enumerate(self.tasks, start=1):
                    file.writelines(f"Task {index}. {task}\n")
            print(f"Tasks saved to {file_name}.txt successfully")
        except FileNotFoundError:
            print(f"Error: File {file_name}.txt not found")

    def get_file_contents(self):
        try:
            with open(f"{self.path_to_file}", "r") as file:
                _file: list[str] = file.readlines()

                # if len(_file) == 0:
                #     print("No content found")
                #     return

                if len(_file) <= self.max_length:
                    self.tasks.extend(_file)
                else:
                    print("File contents exceeds program limit")
                    print("Creating new file...")
                    self.create_new_file()
            print("File read successfully")
        except FileNotFoundError:
            print("Error: No File found")
            print("Creating new file...")
            self.create_task_file()

    def create_task_file(self):
        try:
            with open(f"docs/{self.file_name}.txt", "x") as file:
                file.writelines([])
            print(f"File {self.file_name} created successfully")
        except FileExistsError:
            print(
                f"Error: File {self.file_name}.txt already exist.\nHint: Use a different name"
            )

    def create_new_file(self):
        while (
            user_input := input("Please give the file a name(No spaces in between): ")
            .title()
            .strip()
        ):
            if not user_input.isalpha():
                print(f"Error: {user_input} is not a valid file name")
                continue

            try:
                with open(f"docs/{user_input}.txt", "x") as file:
                    file.writelines([])
                print(f"File {user_input} created successfully")
                break
            except FileExistsError:
                print(
                    f"Error: File {user_input}.txt already exist.\nHint: Use a different name"
                )
        self.file_name = user_input

    def is_tasks_empty(self, func_name: str) -> bool:
        msg: str = f"You dont have any tasks, create some to {func_name}.\n"

        if len(self.tasks) == 0:
            print(msg)
            return True
        return False

    def ask_for_task(self, method_name: str, action_word: str) -> str:
        while not (user_input := input(f"{method_name} {action_word}: ").strip()):
            print(f"\n{action_word} cannot be empty.\n")
        return user_input

    def ask_for_index(self, action_word: str, list_length: int) -> int:
        prompt: str = f"What task would you like to {action_word} or 'Q' to quit: "
        err_msg: str = f"\nPlease choose a valid index between 1 and {list_length}.\n"

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
    app = TODOLISTAPP()
    print(app.tasks)
    ...
    # app = App(10, "cmd/docs/Tasks.txt")

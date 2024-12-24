"""
The below Python script defines a To-Do List application that allows users to add, view, update, and
remove tasks, with the option to quit the program and save tasks to a file.
"""

from typing import Literal
from packages import utility


class App:
    def __init__(self) -> None:
        self.task_title: list[str] = []
        self.task_desc: list[str] = []

        # Constants
        self.MAX_LENGTH = 20
        self.TASK_FILE_PATH = "python\\docs\\Tasks.txt"

        # Checks if tasks file exists and adds contents to the file list dictionary
        try:
            with open(self.TASK_FILE_PATH, "r") as file:
                file_: list[str] = file.readlines()

                # These are both lists with types list[str]
                file_title, file_description = utility.get_title_desc_length(file_)

                if (len(file_title) and len(file_description)) > self.MAX_LENGTH:
                    print("File is full")
                else:
                    self.task_title.extend(file_title)
                    self.task_desc.extend(file_description)

        except FileNotFoundError:
            print("Cannot find file\n")

    def add_tasks(self) -> None:
        if (len(self.task_title) and len(self.task_desc)) > self.MAX_LENGTH:
            print(
                "You have expended all your space for creating tasks, you can either view, update, or delete tasks for more space."
            )

            return None

        create_title_task: str = utility.ask_for_task_title("New")
        print("")
        create_description_task: str = utility.ask_for_task_description("New")

        # Add task title and task description
        self.task_title.append(create_title_task.strip())
        self.task_desc.append(create_description_task.strip())

        print("\nTasks created successfully...\n")

    def view_tasks(self) -> None:
        if (len(self.task_title) or len(self.task_desc)) == 0:
            print("You dont have any tasks, create some to view.\n")
            return None

        for index, (title, desc) in enumerate(
            zip(self.task_title, self.task_desc), start=1
        ):
            print(f"\n{index}.\tTitle: {title}\n\tDescription: {desc}\n")

    def update_tasks(self) -> None:
        if (len(self.task_title) or len(self.task_desc)) == 0:
            print("You dont have any tasks, create some to update.\n")
            return None

        index: int | Literal["Q"] = utility.ask_for_index(
            "update", len(self.task_title)
        )

        if index == "Q":
            print("\nClosing update tasks...")
            return None

        update_title_task: str = utility.ask_for_task_title("Update")
        print("")
        update_description_task: str = utility.ask_for_task_description("Update")

        # Update title and description
        self.task_title[int(index)] = update_title_task
        self.task_desc[int(index)] = update_description_task

        print("\nTask updated successfully...\n")

    def remove_tasks(self) -> None:
        if (len(self.task_title) or len(self.task_desc)) == 0:
            print("\nYou dont have any task, create some to remove.\n")
            return None

        index: int | Literal["Q"] = utility.ask_for_index(
            "remove", len(self.task_title)
        )

        if index == "Q":
            print("\nClosing remove tasks...\n")
            return None

        # Removes tasks
        self.task_title.pop(index)
        self.task_desc.pop(index)

        print("\nTask deleted successfully...\n")

    def quit_program(self) -> None:
        print("Thanks for using the app. GoodBye!")
        if (len(self.task_title) or len(self.task_desc)) == 0:
            return None

        try:
            with open(self.TASK_FILE_PATH, "a") as file1:
                with open(self.TASK_FILE_PATH, "r") as file2:
                    file_: list[str] = file2.readlines()

                    # These are both lists with types list[str]
                    file_title, file_description = utility.get_title_desc_length(file_)

                    if (len(file_title) and len(file_description)) > self.MAX_LENGTH:
                        print("File is full, Program ends successfully...")
                        return None
                    else:
                        for title, desc in zip(self.task_title, self.task_desc):
                            file1.writelines(f"Title:{title}\nDescription:{desc}\n")
                        print("Tasks saved to file, Program ends successfully...")
        except FileNotFoundError:
            print("File not found")


def main() -> None:
    print("\nProgram starts...")

    app = App()

    while True:
        # Displays options
        print("To-Do List App by Ikenna Nicholas Ikwuka")
        print("1.\tAdd a task")
        print("2.\tView your tasks")
        print("3.\tUpdate a task")
        print("4.\tRemove a task")
        print("5.\tQuit the program\n")

        # Loop to take input and catch errors
        choice: int = utility.ask_options()

        match choice:
            case 1:
                app.add_tasks()
            case 2:
                app.view_tasks()
            case 3:
                app.update_tasks()
            case 4:
                app.remove_tasks()
            case 5:
                app.quit_program()
                break


# Starts here
if __name__ == "__main__":
    main()

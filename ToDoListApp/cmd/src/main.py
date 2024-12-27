"""
The provided Python script is a To-Do List application that allows users to add, view, update, and
remove tasks, with the ability to save tasks to a file and load them back when the program restarts.

# TODO Things to fix:
    Duplication error // fixed
    Methods not responding appropriately when file is full //  fixed


# TODO Things to add:
    Add a functionality that removes content in program's list that exceeds max file length // added
    functionality that prevents modification of file outside program // not added
    Implement a way to ask user if the want to create a new file when file is full // not added

"""

from typing import Literal
from packages import utility


class App:
    def __init__(self, max_length: int, file_path: str) -> None:
        self.task_title: list[str] = []
        self.task_desc: list[str] = []
        self.max_length: int = max_length
        self.file_path: str = file_path

        # Checks if tasks file exists and adds contents to the file list dictionary
        try:
            with open(self.file_path, "r") as file:
                file_: list[str] = file.readlines(50)

                # These are both lists with types list[str]
                title_content, desc_content = utility.get_title_desc_content(file_)

                # Adds lists to program's main lists
                self.task_title.extend(title_content[0:max_length])
                self.task_desc.extend(desc_content[0:max_length])
        except FileNotFoundError:
            print(
                f"Path to file: {self.file_path} could not be found, creating a new one...\n"
            )
            with open(self.file_path, "a") as file:
                file.writelines([])

    def add_tasks(self) -> None:
        if (len(self.task_title) or len(self.task_desc)) >= self.max_length:
            print(
                "You have expended all your space for creating tasks, you can either view, update, or delete tasks for more space."
            )

            return None

        create_title_task: str = utility.ask_for_title_desc("Create", "Title")

        create_desc_task: str = utility.ask_for_title_desc("Create", "Description")

        # Add task title and task description
        self.task_title.append(create_title_task.strip())
        self.task_desc.append(create_desc_task.strip())

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
            print("\nClosing update tasks...\n")
            return None

        update_title_task: str = utility.ask_for_title_desc("Update", "Title")

        update_desc_task: str = utility.ask_for_title_desc("Update", "Description")

        # Update title and description
        self.task_title[int(index)] = update_title_task
        self.task_desc[int(index)] = update_desc_task

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
            with open(self.file_path, "a") as file1:
                with open(self.file_path, "r") as file2:
                    file_: list[str] = file2.readlines()

                # These are both lists with types list[str]
                file_title, file_desc = utility.get_title_desc_content(file_)

                if (len(file_title) or len(file_desc)) >= self.max_length:
                    print("File is full, Program ends successfully...")
                    return None

                for title, desc in zip(self.task_title, self.task_desc):
                    file_title_format = f"Title:{title}\n"
                    file_desc_format = f"Description:{desc}\n"

                    # Fixes duplication error
                    if (file_title_format or file_desc_format) in file_:
                        continue

                    file1.writelines(f"Title:{title}\nDescription:{desc}\n")

                print("Tasks saved to file, Program ends successfully...")
        except FileNotFoundError:
            print("File not found")


def main() -> None:
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
    print("\nProgram starts...\n")
    app = App(10, "cmd\\docs\\Tasks.txt")
    # main()

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

from src import utility


class App:
    def __init__(self, max_length: int, file_path: str) -> None:
        self.task_title: list[str] = []
        self.task_desc: list[str] = []
        self.max_length: int = max_length
        self.file_path: str = file_path

        read_file_msg: str = f"file path: {self.file_path} was found, appropriate content (if found) will be taken and file will be cleared"
        leftover_file_msg: str = "File has reached its limits, therefore leftover contents will be added to new file"

        self.file_path_leftover: str = "Tasks leftover.txt"

        # Checks if tasks file exists and adds contents to the file list dictionary
        try:
            with open(self.file_path, "r") as file:
                print(read_file_msg)

                file_: list[str] = file.readlines()

                title_content: list[str] = utility.get_title_content(file_)
                desc_content: list[str] = utility.get_desc_content(file_)

                self.zipped = list(zip(title_content, desc_content))

                contents: list[tuple[str, str]] = self.zipped[: self.max_length]

                leftover: list[tuple[str, str]] = self.zipped[self.max_length :]

                if len(self.zipped) <= self.max_length:
                    utility.resetting_file(contents, self.file_path)
                else:
                    print(leftover_file_msg)
                    utility.resetting_file(leftover, self.file_path_leftover)

                self.task_title.clear()
                self.task_desc.clear()

                # Adds lists to program's main lists
                self.task_title = [title for title, _ in contents]
                self.task_desc = [desc for _, desc in contents]

        except FileNotFoundError:
            print(
                f"Path to file: {self.file_path} could not be found, creating a new one...\n"
            )
            # creating file
            with open(self.file_path, "x") as file:
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

        index: None | int = utility.ask_for_index("update", len(self.task_title))

        if index is None:
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

        index: None | int = utility.ask_for_index("remove", len(self.task_title))

        if index is None:
            print("\nClosing remove tasks...\n")
            return None

        # Removes tasks
        self.task_title.pop(int(index))
        self.task_desc.pop(int(index))

        print("\nTask deleted successfully...\n")

    def quit_program(self) -> None:
        print("Thanks for using the app. GoodBye!")
        if (len(self.task_title) or len(self.task_desc)) == 0:
            return None

        if len(self.zipped) <= self.max_length:
            try:
                with open(self.file_path, "a") as file:
                    for title, desc in zip(self.task_title, self.task_desc):
                        file.writelines(f"Title:{title}\nDescription:{desc}\n")
                    print(
                        f"Tasks saved to file with path: {self.file_path}, Program ends successfully..."
                    )
            except FileNotFoundError:
                print("file not found")
        else:
            try:
                with open(self.file_path_leftover, "a") as file:
                    for title, desc in zip(self.task_title, self.task_desc):
                        file.writelines(f"Title:{title}\nDescription:{desc}\n")

                    print(
                        f"Tasks saved to file with path: {self.file_path_leftover}, Program ends successfully..."
                    )
            except FileNotFoundError:
                print("File is not found")


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
    app = App(10, "cmd/docs/Tasks.txt")
    main()

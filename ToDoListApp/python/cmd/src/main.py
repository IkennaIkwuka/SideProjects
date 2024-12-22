"""
The below Python script defines a To-Do List application that allows users to add, view, update, and
remove tasks, with the option to quit the program and save tasks to a file.
"""

from packages import utility_instance as utility


class App:
    def __init__(self) -> None:
        self.task_list = {"Title": [], "Description": []}

        # Constants
        self.TASK_TITLE = self.task_list["Title"]
        self.TASK_DESCRIPTION = self.task_list["Description"]
        self.TASKS_MAX_LENGTH = 10

    def add_tasks(self) -> None:
        if len(self.TASK_TITLE) > self.TASKS_MAX_LENGTH:
            print("You've reached the limit, you cant create anymore tasks.\n")
            return None

        create_title_task = utility.ask_for_title_task("New")

        create_description_task = utility.ask_for_description_task("New")

        # Add task title and task description
        self.TASK_TITLE.append(create_title_task)
        self.TASK_DESCRIPTION.append(create_description_task)
        print("\nTasks created successfully...")

        # Show tasks
        self.view_tasks()

    def view_tasks(self) -> None:
        if len(self.TASK_TITLE) == 0:
            print("You dont have any tasks, create some to view.\n")
            return None

        for index, (title, desc) in enumerate(
            zip(self.TASK_TITLE, self.TASK_DESCRIPTION), start=1
        ):
            print(f"\n{index}.\tTitle: {title}\n\tDescription: {desc}\n")

    def update_tasks(self) -> None:
        if len(self.TASK_TITLE) == 0:
            print("You dont have any tasks, create some to update.\n")
            return None

        index = utility.ask_for_index("update", len(self.TASK_TITLE), self.view_tasks)

        if index == "Q":
            print("\nClosing update tasks...")
            return None
        else:
            index = int(index)

        update_title_task = utility.ask_for_title_task("Update")

        update_description_task = utility.ask_for_description_task("Update")

        # Update tasks
        self.TASK_TITLE[index] = update_title_task
        self.TASK_DESCRIPTION[index] = update_description_task
        print("\nTask updated successfully...")

        # Show tasks
        self.view_tasks()

    def remove_tasks(self) -> None:
        if len(self.TASK_TITLE) == 0:
            print("\nYou dont have any task, create some to remove.\n")
            return None

        index = utility.ask_for_index("remove", len(self.TASK_TITLE), self.view_tasks)

        if index == "Q":
            print("\nClosing remove tasks...")
            return None
        else:
            index = int(index)

        # Removes tasks
        self.TASK_TITLE.pop(index)
        self.TASK_DESCRIPTION.pop(index)
        print("\nTask deleted successfully")

        # Shows tasks
        self.view_tasks()

    def quit_program(self) -> None:
        print("Thanks for using the app. GoodBye!")
        print(self.task_list)
        if len(self.TASK_TITLE) <= self.TASKS_MAX_LENGTH:
            try:
                with open("Tasks.txt", "a") as file:
                    for title, desc in zip(self.TASK_TITLE, self.TASK_DESCRIPTION):
                        file.writelines(f"Title: {title}\nDescription: {desc}\n")
            except Exception as e:
                print(f"Unexpected error: {e}")


def main() -> None:
    app = App()

    while True:
        # Displays options
        print("\nTo-Do List App by Ikenna Nicholas Ikwuka")
        print("1.\tAdd tasks")
        print("2.\tView tasks")
        print("3.\tUpdate tasks")
        print("4.\tRemove tasks")
        print("5.\tQuit the program\n")

        # Prints 'You dont have any tasks saved'
        file_task_dict = utility.get_tasks_from_file()

        # Else adds contents to task list directory
        if len(file_task_dict["Title"]) != 0:
            app.TASK_TITLE.append(file_task_dict["Title"])
        if len(file_task_dict["Description"]) != 0:
            app.TASK_DESCRIPTION.append(file_task_dict["Description"])

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

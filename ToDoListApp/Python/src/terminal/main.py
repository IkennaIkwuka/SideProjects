"""
The below Python script defines a To-Do List application that allows users to add, view, update, and
remove tasks, with the option to quit the program and save tasks to a file.
"""

from packages.utilities import utilities_instance as utility


class App:
    def __init__(self) -> None:
        self.task_list = {"Title": [], "Description": []}

        # Constants
        self.TITLE = self.task_list["Title"]
        self.DESCRIPTION = self.task_list["Description"]

    def add_tasks(self) -> None:
        if len(self.TITLE) == 10:
            print("You've reached the limit, you cant create anymore tasks.\n")
            return None

        while True:
            task_input_title = ""  # Initialize title as empty str

            if task_input_title == "":
                task_input_title: str = input("Title: ").strip()
                if not task_input_title:
                    print("\nTitle cannot be empty.\n")
                    continue

            task_input_description: str = input("Description: ").strip()
            if not task_input_description:
                print("\nDescription cannot be empty\n")
                continue

            self.TITLE.append(task_input_title)
            self.DESCRIPTION.append(task_input_description)
            print("\nTasks created successfully")
            self.view_tasks()
            break

    def view_tasks(self) -> None:
        if len(self.TITLE) == 0:
            print("You dont have any tasks, create some.\n")
            return None

        for index, (title, desc) in enumerate(
            zip(self.TITLE, self.DESCRIPTION), start=1
        ):
            print(f"\n{index}.\tTitle: {title}\n\tDescription: {desc}\n")

    def update_tasks(self) -> None:
        if len(self.TITLE) == 0:
            print("You dont have any tasks to update, create some\n")
            return None

        index = utility.ask_for_index("update", len(self.TITLE), self.view_tasks)

        if index == "Q":
            print("Closing update tasks")
            return None
        else:
            index = int(index)

        while True:
            new_task_input_title: str = input("New Title: ").strip()
            new_task_input_description: str = input("New Description: ").strip()

            if not (new_task_input_title and new_task_input_description):
                print("\nTitle and Description cannot be empty\n")
            elif not new_task_input_title:
                print("\nTitle cannot be empty.\n")
            elif not new_task_input_description:
                print("\nDescription cannot be empty\n")
            else:
                self.TITLE[index] = new_task_input_title
                self.DESCRIPTION[index] = new_task_input_description
                print("\nTask updated successfully")
                self.view_tasks()
                break

    def remove_tasks(self) -> None:
        if len(self.TITLE) == 0:
            print("You dont have any task to remove, create some.")
            return None

        index = utility.ask_for_index("update", len(self.TITLE), self.view_tasks)

        if index == "Q":
            print("Closing remove tasks")
            return None
        else:
            index = int(index)
            self.TITLE.pop(index)
            self.DESCRIPTION.pop(index)
            print("\nTask deleted successfully")
            self.view_tasks()

    def quit_program(self) -> None:
        print("Thanks for using the app. GoodBye!")

        with open("Tasks.txt", "a") as file:
            for title, description in zip(self.TITLE, self.DESCRIPTION):
                file.writelines(f"Title: {title}\n\tDescription: {description}\n\n")


app = App()


def main() -> None:
    while True:
        # Displays options
        print("\nTo-Do List App by Ikenna Nicholas Ikwuka")
        print("1.\tAdd tasks")
        print("2.\tView tasks")
        print("3.\tUpdate tasks")  
        print("4.\tRemove tasks")
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

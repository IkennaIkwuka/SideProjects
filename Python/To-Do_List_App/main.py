import packages.utility_operations as ult_ops


class ToDoListApp:
    def __init__(self) -> None:
        self.task_list = {"Title": [], "Description": []}

        # Constants
        self.TITLE, self.DESCRIPTION = (
            self.task_list["Title"],
            self.task_list["Description"],
        )

    def add_tasks(self) -> None:
        # TODO: implement a way to split the error message so that each input is checked at its time of creation.
        while True:
            task_input_title: str = input("Title: ")
            task_input_description: str = input("Description: ")

            if not task_input_title:
                print("\nTitle cannot be empty.")
            elif not task_input_description:
                print("\nDescription cannot be empty")
            else:
                self.TITLE.append(task_input_title)
                self.DESCRIPTION.append(task_input_description)
                print("\nTasks created successfully")
                self.view_tasks()
                break

    def view_tasks(self) -> bool:
        print("")
        if len(self.TITLE) == 0:
            print("You dont have any tasks, create some.\n")
            return False
        else:
            for index, (title, description) in enumerate(
                zip(self.TITLE, self.DESCRIPTION), start=1
            ):
                print(f"{index}.\tTitle: {title}\n\tDescription: {description}\n")
            return True

    def update_tasks(self) -> None:
        if self.view_tasks():
            index: int = ult_ops.ask_for_index("update")

            if 0 <= index < len(self.TITLE):
                while True:
                    new_task_input_title: str = input("New title: ")
                    new_task_input_description: str = input("New description: ")

                    if not new_task_input_title:
                        print("\nTitle cannot be empty.")
                    elif not new_task_input_description:
                        print("\nDescription cannot be empty")
                    else:
                        self.TITLE[index] = new_task_input_title
                        self.DESCRIPTION[index] = new_task_input_description
                        self.view_tasks()
                        break
            else:
                print("\nCannot find task")

    def remove_tasks(self) -> None:
        if self.view_tasks():
            index: int = ult_ops.ask_for_index("remove")

            if 0 <= index < len(self.TITLE):
                self.TITLE.pop(index)
                self.DESCRIPTION.pop(index)
                print("\nTasks deleted successfully")
                self.view_tasks()
            else:
                print("\nCannot find task")


def main() -> None:
    app = ToDoListApp()

    while True:
        # Displays options
        print("To-Do List App by Ikenna Nicholas Ikwuka")
        print("1. Add tasks")
        print("2. View tasks")
        print("3. Update tasks")
        print("4. Remove tasks")
        print("5. Quit\n")

        # Loop to take input and catch errors
        choice: int = ult_ops.ask_options()
        match choice:
            case 1:
                if len(app.TITLE) == 10:
                    print("You've reached the limit, you cant create anymore tasks.\n")
                else:
                    app.add_tasks()
            case 2:
                app.view_tasks()
            case 3:
                app.update_tasks()
            case 4:
                app.remove_tasks()
            case 5:
                print("Thanks for using the app. GoodBye!")
                break


# Starts here
if __name__ == "__main__":
    main()

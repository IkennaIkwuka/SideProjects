# Utilities
class Utility:
    def __init__(self) -> None: ...

    def ask_options(self):
        while True:
            # Validate user input and implements error handling.
            try:
                choice = int(input("What do you want to do?: "))

                if choice not in range(1, 6):  # Checks input in range of 1 ~ 5
                    print("\nInvalid Input. Input a value from range 1 ~ 5")
                else:
                    break
            # Throw raised error or any unchecked errors
            except ValueError:  # Catches and displays ValueError for invalid types.
                print("\nInvalid Input. Input a number")
        return choice

    def ask_for_index(self, action: str, list_length: int, func):
        while True:
            try:
                func()
                index = int(input(f"What task would you like to {action}: ")) - 1
                if 0 <= index < list_length:
                    return index
                else:
                    print("\nCannot find task")
            except ValueError:
                print("\nInvalid, input number")


class App:
    def __init__(self) -> None:
        self.task_list = {"Title": [], "Description": []}

        # Constants
        self.TITLE, self.DESCRIPTION = (
            self.task_list["Title"],
            self.task_list["Description"],
        )

        self.utility = Utility()

    def add_tasks(self) -> None:
        if len(self.TITLE) == 10:
            print("You've reached the limit, you cant create anymore tasks.\n")
            return None
        while True:
            task_input_title: str = input("Title: ")
            task_input_description: str = input("Description: ")

            if not task_input_title:
                print("\nTitle cannot be empty.")
            elif not task_input_description:
                print("\nDescription cannot be empty")
            elif not (task_input_title and task_input_description):
                print("Title and Description cannot be empty")
            else:
                self.TITLE.append(task_input_title)
                self.DESCRIPTION.append(task_input_description)
                print("\nTasks created successfully")
                self.view_tasks()
                break

    def view_tasks(self) -> None:
        if len(self.TITLE) == 0:
            print("You dont have any tasks, create some.\n")
            return None

        for index, (title, description) in enumerate(
            zip(self.TITLE, self.DESCRIPTION), start=1
        ):
            print(f"\n{index}.\tTitle: {title}\n\tDescription: {description}\n")

    def update_tasks(self) -> None:
        if len(self.TITLE) == 0:
            print("You dont have any tasks to update, create some\n")
            return None

        index: int = self.utility.ask_for_index(
            "update", len(self.TITLE), self.view_tasks
        )

        while True:
            new_task_input_title: str = input("New Title: ")
            new_task_input_description: str = input("New Description: ")

            if not new_task_input_title:
                print("\nTitle cannot be empty.")
            elif not new_task_input_description:
                print("\nDescription cannot be empty")
            elif not (new_task_input_title and new_task_input_description):
                print("Title and Description cannot be empty")
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

        index: int = self.utility.ask_for_index(
            "remove", len(self.TITLE), self.view_tasks
        )

        self.TITLE.pop(index)
        self.DESCRIPTION.pop(index)
        print("\nTask deleted successfully")
        self.view_tasks()

    def quit_program(self):
        print("Thanks for using the app. GoodBye!")


def main() -> None:
    app = App()

    while True:
        # Displays options
        print("\nTo-Do List App by Ikenna Nicholas Ikwuka")
        print("1. Add tasks")
        print("2. View tasks")
        print("3. Update tasks")
        print("4. Remove tasks")
        print("5. Quit\n")

        # Loop to take input and catch errors
        choice: int = app.utility.ask_options()
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

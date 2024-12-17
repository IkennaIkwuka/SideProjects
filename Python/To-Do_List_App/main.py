# %%
import packages.utility_operations as ult_ops


class to_do_list_app:
    def __init__(self) -> None:
        self.task_list = {"Title": [], "Description": []}

        # Constants
        self.TITLE, self.DESCRIPTION = (
            self.task_list["Title"],
            self.task_list["Description"],
        )
        self.EMPTY_TASKS_ERROR_MSG = "You dont have any tasks, create some."

    def add_tasks(self):
        # TODO implement a way to split the error message so that each input is checked at its time of creation.
        while True:
            task_input_title = input("Title: ")
            task_input_description = input("Description: ")

            if not (task_input_title and task_input_description):
                print("Title or Description cannot be empty.\n")
            else:
                self.TITLE.append(task_input_title)
                self.DESCRIPTION.append(task_input_description)
                self.view_tasks()
                break

    def view_tasks(self):
        if len(self.TITLE) == 0:
            print(self.EMPTY_TASKS_ERROR_MSG)
        else:
            for index, (title, description) in enumerate(
                zip(self.TITLE, self.DESCRIPTION), start=1
            ):
                print(f"\n{index}.\tTitle: {title}\n\tDescription: {description}\n")

    def update_tasks(self, new_task_input):
        self.view_tasks()
        if 0 <= new_task_input < len(self.TITLE):
            while True:
                new_task_input_title = input("New title: ")
                new_task_input_description = input("New description: ")

                if not (new_task_input_title and new_task_input_description):
                    print("Title or Description cannot be empty.\n")
                else:
                    self.TITLE[new_task_input] = new_task_input_title
                    self.DESCRIPTION[new_task_input] = new_task_input_description
                    break
        else:
            print("Cannot find task")

    def remove_task(self):
        if len(list(zip(self.TITLE, self.DESCRIPTION))) == 0:
            print(self.EMPTY_TASKS_ERROR_MSG)
        else:
            dictionary = list(zip(self.TITLE, self.DESCRIPTION))
            print(dictionary)


# %%
def main():
    app = to_do_list_app()

    while True:
        # Loop to take input and catch errors
        choice = ult_ops.display_and_ask_options()
        match choice:
            case 1:
                if len(app.TITLE) == 10:
                    print("You've reached the limit, you cant create anymore tasks.")
                else:
                    app.add_tasks()
            case 2:
                app.view_tasks()
            case 3:
                while True:
                    try:
                        new_task_input = (
                            int(input("What task would you like to update: ")) - 1
                        )
                        app.update_tasks(new_task_input)
                        break
                    except ValueError:
                        print("Invalid, input number")
            case 4:
                app.remove_task()
            case 5:
                print("Thanks for using the app. GoodBye!")
                break


# Starts here
if __name__ == "__main__":
    main()

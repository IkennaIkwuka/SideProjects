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

tasks: list[str] = []
# task_desc: list[str] = []
max_length = 10
file_path = "cmd/docs/Tasks.txt"

# read_file_msg: str = f"file path: {file_path} was found, appropriate content (if found) will be taken and file will be cleared"
# leftover_file_msg: str = """File has reached its limits, therefore leftover contents will be added to new file"""

# file_path_leftover: str = "Tasks leftover.txt"

# # Checks if tasks file exists and adds contents to the file list dictionary
# try:
#     with open(file_path, "r") as file:
#         print(read_file_msg)

#         file_: list[str] = file.readlines()

#         title_content: list[str] = tdl_utility.get_title_content(file_)
#         desc_content: list[str] = tdl_utility.get_desc_content(file_)

#         zipped = list(zip(title_content, desc_content))

#         contents: list[tuple[str, str]] = zipped[:max_length]

#         leftover: list[tuple[str, str]] = zipped[max_length:]

#         if len(zipped) <= max_length:
#             tdl_utility.resetting_file(contents, file_path)
#         else:
#             print(leftover_file_msg)
#             tdl_utility.resetting_file(leftover, file_path_leftover)

#         tasks.clear()
#         task_desc.clear()

#         # Adds lists to program's main lists
#         tasks = [title for title, _ in contents]
#         task_desc = [desc for _, desc in contents]

# except FileNotFoundError:
#     print(f"Path to file: {file_path} could not be found, creating a new one...\n")
#     # creating file
#     with open(file_path, "x") as file:
#         file.writelines([])


def add_tasks() -> None:
    msg = "You have expended all your space for creating tasks, you can either view, update, or delete tasks for more space.\n"

    if len(tasks) >= max_length:
        print(msg)
        return

    create_task: str = ask_for_task("Create", "Task")

    # Add task title and task description
    tasks.append(create_task.strip())

    print("\nTasks created successfully...\n")


def view_tasks() -> None:
    check_if_task_empty("view")

    for index, task in enumerate(tasks, start=1):
        print(f"\nTask {index}. {task} ")


def update_tasks() -> None:
    if check_if_task_empty("update") is None:
        return None

    index: int = ask_for_index("update", len(tasks))

    close_func(index, "Update")

    update_task: str = ask_for_task("Update", "Task")

    # Update title and description
    tasks[int(index)] = update_task

    print("\nTask updated successfully...\n")


def remove_tasks() -> None:
    if check_if_task_empty("remove") is None:
        return None

    index: int = ask_for_index("remove", len(tasks))

    close_func(index, "Remove")

    # Removes tasks
    tasks.pop(int(index))

    print("\nTask deleted successfully...\n")


# def save_tasks() -> None:
#     print("Thanks for using the app. GoodBye!")
#     if (len(tasks) or len(task_desc)) == 0:
#         return None

#     if len(self.zipped) <= self.max_length:
#         try:
#             with open(self.file_path, "a") as file:
#                 for title, desc in zip(self.tasks, self.task_desc):
#                     file.writelines(f"Title:{title}\nDescription:{desc}\n")
#                 print(
#                     f"Tasks saved to file with path: {self.file_path}, Program ends successfully..."
#                 )
#         except FileNotFoundError:
#             print("file not found")
#     else:
#         try:
#             with open(self.file_path_leftover, "a") as file:
#                 for title, desc in zip(self.tasks, self.task_desc):
#                     file.writelines(f"Title:{title}\nDescription:{desc}\n")

#                 print(
#                     f"Tasks saved to file with path: {self.file_path_leftover}, Program ends successfully..."
#                 )
#         except FileNotFoundError:
#             print("File is not found")


def close_func(index: int, func_name: str) -> None:
    if index == 0:
        print(f"\nClosing {func_name} tasks...\n")


def check_if_task_empty(func_name: str) -> None:
    msg: str = f"You dont have any tasks, create some to {func_name}.\n"

    if len(tasks) == 0:
        print(msg)


def ask_for_task(method_name: str, action_word: str) -> str:
    while not (user_input := input(f"{method_name} {action_word}: ").strip()):
        print(f"\n{action_word} cannot be empty.\n")
    return user_input


def ask_for_index(action_word: str, list_length: int) -> int:
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
    ...
    # app = App(10, "cmd/docs/Tasks.txt")

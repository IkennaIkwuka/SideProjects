class FileOps:
    def __init__(self) -> None:
        ...

        # Constants
        # self.FILE_TASK_TITLE = self.file_list["Title"]
        # self.FILE_TASK_DESCRIPTION = self.file_list["Description"]

    # Runs at the start of the program
    # def program_start(self):
    #     if len(self.FILE_TASK_TITLE) == 0:
    #         return None

    def get_file_state(self):
        file_list: dict[str, list[str]] = {"Title": [""], "Description": [""]}

        # Checks if tasks file exists and adds contents to the file list dictionary
        try:
            with open("Tasks.txt", "r") as file:
                for _ in file.readlines():
                    task = _.strip()
                    if task.startswith("Title"):
                        file_list["Title"].append(task)
                    if task.startswith("Description"):
                        file_list["Description"].append(task)
        except FileNotFoundError:
            print("You dont have any tasks saved\n")

        return file_list["Title"], file_list["Description"]

    def display(self):
        print("\nTo-Do List App by Ikenna Nicholas Ikwuka")
        print("\nYou have tasks in file, here are your options: \n")
        print("1.\tAdd more tasks")


# if __name__ == "__main__":
# files = FileOps()
# files.program_start()
# print(files.file_list)

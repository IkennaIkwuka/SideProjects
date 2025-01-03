"""
The `Utility` class provides methods for handling user input validation, error handling, and file content extraction in a task management program.
"""


# Utilities
class Utility:
    def __init__(self) -> None: ...

    def ask_options(self) -> int:
        while True:
            # Validate user input and implements error handling.
            try:
                choice = int(input("What do you want to do? or '5' to quit: "))

                if choice not in range(1, 6):  # Checks input in range of 1 ~ 5
                    print("\nInvalid Input. Input a value from range 1 ~ 5\n")
                else:
                    break
            # Throw raised error or any unchecked errors
            except ValueError:  # Catches and displays ValueError for invalid types.
                print("\nInvalid Input. Input a number\n")
        return choice

    def ask_for_index(self, action_word: str, list_length: int) -> None | int:
        prompt: str = f"What task would you like to {action_word} or 'Q' to quit: "

        err_msg: str = f"\nPlease choose a valid index between 1 and {list_length}.\n"

        while True:
            user_input = input(prompt).strip()

            if user_input.upper() == "Q":
                return None

            if not user_input.isdigit():
                print("invalid must be a number or 'Q' to quit")
                continue

            user_input = int(user_input) - 1

            if user_input in range(list_length):
                return user_input
            else:
                print(err_msg)

    def ask_for_title_desc(self, method_name: str, action_word: str) -> str:
        # loop for task title and description
        while True:
            user_input: str = input(f"{method_name} {action_word}: ").strip()
            print("")

            if not user_input:
                print(f"\n{action_word} cannot be empty.\n")
            else:
                return user_input

    def get_title_content(self, file_list: list[str]) -> list[str]:
        file_content: list[str] = [
            item.strip() for item in file_list if item.startswith(("Title:"))
        ]

        duplicates = set()

        title_content: list[str] = []

        for item in file_content:
            if item not in duplicates:
                title_content.append(item.strip("Title:"))
                duplicates.add(item)

        return title_content

    def get_desc_content(self, file_list: list[str]) -> list[str]:
        file_content: list[str] = [
            item.strip() for item in file_list if item.startswith(("Description:"))
        ]

        duplicates = set()

        desc_content: list[str] = []

        for item in file_content:
            if item not in duplicates:
                desc_content.append(item.strip("Description:"))
                duplicates.add(item)

        return desc_content

    # def ask_for_backup(self, file_):
    #     backup_prompt = "Would you like to create a backup (Y/N)? | Warning: Not creating a backup means if any problem arises all data will be lost!: "

    #     backup_name_prompt = "What name would you give this backup file?: "
    #     while True:
    #         backup = input(backup_prompt).strip()

    #         if backup.upper() == "Y":
    #             while True:
    #                 backup_name = input(backup_name_prompt).strip().title()
    #                 try:
    #                     with open(f"cmd/docs/{backup_name}.txt", "x") as file:
    #                         file.writelines(file_)
    #                         break
    #                 except FileExistsError:
    #                     print(
    #                         f"File at path: cmd/docs/{backup_name}.txt exists already create a new one."
    #                     )
    #             break
    #         elif backup.upper() == "N":
    #             break
    #         else:
    #             print("Invalid input")

    def resetting_file(self, zipped_list: list, file_path: str) -> None:
        with open(file_path, "w") as file:
            for title, desc in zipped_list:
                file.writelines(f"Title:{title}\nDescription:{desc}\n")


tdl_utility = Utility()

if __name__ == "__main__":
    # ult.get_title_desc_content(app.)
    # ult.ask_for_index("Update", 10)
    ...

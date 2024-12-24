"""
The `Utilities` class provides methods for asking user options and indices with input validation and
error handling.
"""


# Utilities
class Utility:
    def __init__(self) -> None: ...

    def ask_options(self):
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

    def ask_for_index(
        self,
        action_word: str,
        list_length: int,
    ):
        while True:
            index = input(f"What task would you like to {action_word} or 'Q' to quit: ")

            if not index:
                print("\nCannot be empty\n")

            elif index.isalpha():
                index = index[0].upper().strip()

                if index == "Q":
                    return index
                else:
                    print(f"\nPlease type 'Q' if you want to quit and not '{index}'\n")

            elif index.isdigit():
                index = int(index) - 1

                if index in range(list_length):
                    return index
                else:
                    print(f"\nPlease choose a valid index for task and not '{index}'\n")
            else:
                print(
                    f"Invalid input. Please choose a valid task you would like to {action_word} or 'Q' to quit and not {index}\n"
                )

    def ask_for_task_title(self, action_word: str):
        # loop for task title
        while True:
            title_input: str = input(f"{action_word} title: ")

            if not title_input:
                print("\nTitle cannot be empty.\n")
            else:
                return title_input.strip()

    def ask_for_task_description(self, action_word: str):
        # Loop for task description
        while True:
            description_input: str = input(f"{action_word} description: ")

            if not description_input:
                print("\nDescription cannot be empty\n")
            else:
                return description_input.strip()

    def get_title_desc_length(self, file_: list[str]):
        title_length: list[str] = [
            title_exist.strip("Title:")
            for title_exist in file_
            if title_exist.startswith("Title:")
        ]

        strip_title = [item.strip() for item in title_length]

        description_length: list[str] = [
            title_exist.strip("Description:")
            for title_exist in file_
            if title_exist.startswith("Description:")
        ]

        strip_desc = [item.strip() for item in description_length]

        return strip_title, strip_desc


if __name__ == "__main__":
    ult = Utility()
    # ult.get_file_state(20)
    ...

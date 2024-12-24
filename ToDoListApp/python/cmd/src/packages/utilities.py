"""
The `Utility` class provides methods for handling user input validation and error handling for
asking options, indices, task titles, and task descriptions.
"""

from typing import Literal, Union


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

    def ask_for_index(
        self,
        action_word: str,
        list_length: int,
    ) -> Union[int, Literal["Q"]]:
        while True:
            user_input = input(
                f"What task would you like to {action_word} or 'Q' to quit: "
            ).strip()

            if not user_input:
                print("\nCannot be empty. Please try again\n")
                continue

            if user_input.upper() == "Q":
                return "Q"

            if user_input.isdigit():
                user_input = int(user_input) - 1

                if user_input in range(list_length):
                    return user_input
                else:
                    print(
                        f"\nPlease choose a valid index between 1 and {list_length}.\n"
                    )
            else:
                print(
                    f"Invalid input.\nPlease choose a valid task you would like to {action_word} or 'Q' to quit.\n"
                )

    def ask_for_task_title(self, action_word: str) -> str:
        # loop for task title
        while True:
            title_input: str = input(f"{action_word} title: ").strip()

            if not title_input:
                print("\nTitle cannot be empty.\n")
            else:
                return title_input

    def ask_for_task_description(self, action_word: str) -> str:
        # Loop for task description
        while True:
            description_input: str = input(f"{action_word} description: ").strip()

            if not description_input:
                print("\nDescription cannot be empty\n")
            else:
                return description_input

    def get_title_desc_length(self, file_: list[str]) -> tuple[list[str], list[str]]:
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

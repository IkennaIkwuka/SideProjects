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

    def ask_for_title_desc(self, method_name: str, action_word: str) -> str:
        # loop for task title and description
        while True:
            user_input: str = input(f"{method_name} {action_word}: ").strip()
            print("")

            if not user_input:
                print(f"\n{action_word} cannot be empty.\n")
            else:
                return user_input

    def get_title_desc_content(self, file_) -> tuple[list[str], list[str]]:
        file_content: list[str] = [
            item.strip()
            for item in file_
            if item.startswith(("Title:", "Description:"))
        ]

        title_content: list[str] = [item.strip("Title:") for item in file_content]
        desc_content: list[str] = [item.strip("Description:") for item in file_content]

        return title_content, desc_content


if __name__ == "__main__":
    # ult = Utility()
    ...

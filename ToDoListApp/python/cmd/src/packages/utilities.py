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

    def ask_for_index(self, action_word: str, list_length: int, func):
        while True:
            func()
            index = input(
                f"What task would you like to {action_word} or 'Q' to quit: "
            ).strip()

            if index.isalpha():
                index = index[0].upper()
                if index == "Q":
                    return index
                else:
                    print(f"\nPlease type 'Q' if you want to quit and not '{index}'\n")
            elif index.isdigit():
                index = int(index) - 1
                if index in range(1, list_length + 1):
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
            title_input: str = input(f"{action_word} title: ").strip()
            if not title_input:
                print("\nTitle cannot be empty.\n")
            else:
                return title_input

    def ask_for_task_description(self, action_word: str):
        # Loop for task description
        while True:
            description_input: str = input(f"{action_word} description: ").strip()
            if not description_input:
                print("\nDescription cannot be empty\n")
            else:
                return description_input



if __name__ == "__main__":
    ...

def ask_for_title_desc(method_name: str, action_word: str) -> str:
    # loop for task title and description
    while True:
        user_input: str = input(f"{method_name} {action_word}: ").strip()
        print("")

        if not user_input:
            print(f"\n{action_word} cannot be empty.\n")
        else:
            return user_input


def test_ask_ftd(method_name, action_word):
    while not (user_input := input(f"{method_name} {action_word}: ").strip()):
        print(f"\n{action_word} cannot be empty.\n")
    return user_input


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


def test_ask_index(action_word: str, list_length: int):
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

class Example:
    def __init__(self) -> None:
        ...
    def say_name(self):
            print("Hello")
    def say_name(self,string:str):
        print(f"Hello {string}")    




if __name__ == "__main__":
    # test_ask_ftd("create", "title")
    # test_ask_index("create")
    rx = Example()
    rx.say_name("ikenna")

"""
#TODO: Things to add:
    A difficulty setting // not added
"""

# from utilities import ngg_utility
import random


class Game:
    def __init__(self, number_range: int) -> None:
        self.range: int = number_range
        self.computer_input: int = self.get_computer_input()
        self.user_input: int = self.get_user_input()

    def game_logic(self) -> str:
        if self.user_input == self.computer_input:
            return f"Congratulations!! you got it {self.computer_input} was the right answer, your input was {self.user_input}"
        else:
            return f"Not the right number {self.computer_input} is the right one, your input was {self.user_input}"

    def get_user_input(self) -> int:
        while True:
            try:
                user_input = int(
                    input("A number has been generated. Guess what it is!: ")
                )
                return user_input
            except ValueError:
                print("Error: Must be a number\n")

    def get_computer_input(self) -> int:
        computer_input: int = random.randrange(self.range)
        return computer_input


def main() -> None:
    print("\nHi!, welcome to the Number Guessing Game.\n")
    print("What difficulty would you like:\n")
    while True:
        try:
            game_range = int(
                input(
                    "Please give a number in whose range you'll guess what the correct number is:"
                )
            )
            break
        except ValueError:
            print("Error: Must be a number.")

    game = Game(game_range)

    print(game.game_logic())


if __name__ == "__main__":
    main()

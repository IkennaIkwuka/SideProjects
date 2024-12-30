"""
#TODO: Things to fix:
    Fix get_result functionality // not fixed
#TODO: Things to add:
    A game difficulty setting // not added
    A score board // not added
"""

# from utilities import ngg_utility
import random


class Game:
    def __init__(self) -> None:
        self.difficulties = (10, 30, 50, 80)

        level: int = self.set_game_difficulty()

        self.computer_input: int = random.randrange(1, self.difficulties[level])

        self.user_input: int = self.ask_user_input()

        # print(self.get_result())

    def game_logic(self) -> None:
        ...

        # dpg  = int(input(""))

    def get_result(self) -> None:
        # result: str = ""
        if self.user_input == self.computer_input:
            print(
                f"Congratulations!! you got it {self.computer_input} was the right answer, your input was {self.user_input}"
            )

        elif self.user_input < self.computer_input:
            print(f"Almost, your input was {self.user_input}")

        elif self.user_input > self.computer_input:
            print(f"Too far!, your input was {self.user_input}")

        # print(result)

    def ask_user_input(self) -> int:
        while True:
            try:
                user_input = int(
                    input("A number has been generated. Guess what it is!: ")
                )
                return user_input
            except ValueError:
                print("Error: Must be a number\n")

    def set_game_difficulty(self) -> int:
        print("What game difficulty would you like:\n")
        print("1. Easy: 1 ~ 10")
        print("2. Medium: 1 ~ 30")
        print("3. Hard: 1 ~ 50")
        print("4. Insane: 1 ~ 80")

        while True:
            try:
                game_difficulty = int(input("Choose a game difficulty: "))

                if game_difficulty in range(1, 5):
                    break
                else:
                    print("Please type between 1 ~ 4")
            except ValueError:
                print("Error: Please type a number")
        return game_difficulty


def main() -> None:
    print("\nHi!, welcome to the Number Guessing Game.\n")

    game = Game()
    game.get_result()
    # game.game_logic()

    # print(game.get_result())


if __name__ == "__main__":
    main()

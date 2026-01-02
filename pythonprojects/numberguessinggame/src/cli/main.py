#
# Number Guessing Game
#

import random
from src.cli.logic import GameLogic


class Game:
    def __init__(self, logic: GameLogic | None = None):
        self.levels = {1: 10, 2: 50, 3: 100}
        self.logic = logic or GameLogic(self.levels)

        # Initial state
        self.min_number = 1
        self.max_number = 100

    def run_game(self):
        print("\nWelcome to my Number Guessing Game.")

        while True:
            max_val = self.get_level()

            if max_val == "q":
                break

            self.min_number = 1
            self.max_number = max_val

            computer_choice = random.randint(self.min_number, self.max_number)

            self.play_round(computer_choice)

            print("\nDo you want to play again? (y/n)\n")
            again = input("> ").lower()
            if again != "y":
                break

    def get_level(self):
        while True:
            print(
                "\nChoose your difficulty(q to Quit)\n1. Easy(1-10)\n2. Hard(1-50)\n3. Insane(1-100)\n"
            )
            choice = input("> ").strip()

            result = self.logic.get_level(choice)

            if not result:
                continue

            if result == "q":
                return "q"

            return self.levels[result]

    def get_user_guess(self):
        print(f"\nGuess a number between {self.min_number} and {self.max_number}.\n")
        while True:
            choice = input("> ").strip()

            result = self.logic.get_user_guess(choice, self.min_number, self.max_number)

            if not result:
                continue

            return result

    def play_round(self, computer_choice: int):
        while True:
            user_choice = self.get_user_guess()
            if user_choice == computer_choice:
                print(f"\nCorrect!! {user_choice} was the right answer.")
                break

            if user_choice > computer_choice:
                self.max_number = user_choice - 1
                print(
                    f"\nYou're above. The correct value is between {self.min_number} and {self.max_number}"
                )
            elif user_choice < computer_choice:
                self.min_number = user_choice + 1
                print(
                    f"\nYou're below. The correct value is between {self.min_number} and {self.max_number}"
                )

            if self.min_number == self.max_number:
                print(
                    f"\nOnly one possibility left! So the answer is {computer_choice}."
                )
                break


def main():
    Game().run_game()


if __name__ == "__main__":
    main()
    ...  # for testing purposes

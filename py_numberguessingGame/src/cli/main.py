#
# Number Guessing Game
#

import random
from src.services.logic import GameLogic


class Game:
    def __init__(self, logic: GameLogic | None = None):
        self.levels = {1: 10, 2: 50, 3: 100}

        self.logic = logic or GameLogic(self.levels)

        self.min_number = 1
        self.max_number = 100

    def run_game(self):
        print("\nWelcome to my Number Guessing Game.")

        while True:
            difficulty = self.game_difficulty()

            if difficulty == "q":
                print("Closing game...")
                return

            self.max_number = difficulty

            computer_choice = self.computer_number(difficulty)

            user_choice = self.user_number(difficulty)

            if user_choice == self.min_number:
                print(f"The correct number is {self.min_number}.")
                return

            self.game_logic(user_choice, computer_choice)

            print("\nDo you want to play again? (y/n)\n")
            again = input("> ").lower()
            if again != "y":
                break

    def game_difficulty(self):
        while True:
            print("\nChoose your difficulty(q to Quit)\n1. Easy\n2. Hard\n3. Insane\n")
            choice = input("> ").strip()

            result = self.logic.game_difficulty(choice)

            if result == "q":
                return "q"

            if result == "out of Range":
                print("Out of range.")
                continue

            if result == "invalid Input":
                print("Invalid. Please enter a number")
                continue

            return self.levels[result]

    def computer_number(self, difficulty: int) -> int:
        return random.randint(1, difficulty)

    def user_number(self, difficulty: int):
        # If only one number remains, reveal it immediately
        if self.min_number == self.max_number:
            return self.min_number

        self.min_number = 1

        while True:
            print(
                f"\nGuess a number between {self.min_number} and {self.max_number}.\n"
            )
            choice = input("> ").strip()

            result = self.logic.user_number(choice, difficulty)

            if result == "out of range":
                print("\nOut of range.")
                continue

            if result == "invalid input":
                print("\nInvalid. Please enter a number")
                continue

            return result

    def game_logic(self, user_choice: int, computer_choice: int):
        while True:
            if user_choice == computer_choice:
                print(f"\nCongratulations!! {user_choice} was the right answer.")
                return

            if user_choice > computer_choice:
                self.max_number = user_choice - 1
                print(
                    f"\nYou're above. The correct value is between {self.min_number} and {self.max_number}"
                )
            else:
                self.min_number = user_choice + 1
                print(
                    f"\nYou're below. The correct value is between {self.min_number} and {self.max_number}"
                )
            # Ask for another guess
            user_choice = self.user_number(self.max_number)


def main():
    Game().run_game()


if __name__ == "__main__":
    ...  # for testing purposes

"""
#TODO: Things to fix:
    Fix game_logic functionality // fixed
#TODO: Things to add:
    A game difficulty setting // added
    A way to determine the number of users and a score board // not added
"""

import random


class Game:
    def __init__(self) -> None:
        self.game_level: int = self.set_game_difficulty()

        self.computer_input: int = self.get_computer_input(self.game_level)

    def set_game_difficulty(self) -> int:
        game_difficulties = (10, 30, 50, 80, 1000)
        game_difficulties_length = 5
        while True:
            try:
                difficulty = int(input("Choose a game difficulty: "))

                if difficulty in range(1, game_difficulties_length + 1):
                    return game_difficulties[difficulty - 1]
                else:
                    print(f"Please type between 1 ~ {game_difficulties_length}")
            except ValueError:
                print("Error: Please type a number")

    def game_logic(self) -> None:
        user_input: int | None = self.ask_user_input(
            f"A number has been generated between 1 and {self.game_level}. Guess what it is!, 'Q' to quit: "
        )

        if user_input is None:
            return None
        prompt = "Make another guess, 'Q' to quit: "
        high_value = self.game_level
        low_value: int = 0
        while True:
            if user_input == self.computer_input:
                print(
                    f"Congratulations!! you got it {self.computer_input} was the right answer, your input was {user_input}"
                )
                break
            elif user_input < self.computer_input:
                low_value: int = user_input
                print(
                    f"You're below. The correct value is between {low_value} and {high_value}"
                )
                user_input = self.ask_user_input(prompt)

            elif user_input > self.computer_input:
                high_value: int = user_input
                print(
                    f"You're above. The correct value is between {low_value} and {high_value}"
                )
                user_input = self.ask_user_input(prompt)

            if user_input is None:
                return None

    def ask_user_input(self, prompt: str) -> int | None:
        while True:
            user_input: str = input(prompt).strip().upper()

            if user_input[0] == "Q":
                return None
            elif user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input")

    def get_computer_input(self, game_level: int) -> int:
        computer_input: int = random.randrange(1, game_level)

        return computer_input


def main() -> None:
    print("\nHi!, welcome to the Number Guessing Game.\n")
    print("What game difficulty would you like:\n")
    print("1. Easy: 1 ~ 10")
    print("2. Medium: 1 ~ 30")
    print("3. Hard: 1 ~ 50")
    print("4. Insane: 1 ~ 80")
    print("5. Omo: 1 ~ 1000\n")

    game = Game()
    game.game_logic()


if __name__ == "__main__":
    main()

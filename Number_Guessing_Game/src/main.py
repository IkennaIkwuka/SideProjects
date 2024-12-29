from utilities import ngg_utility
import random


class Game:
    def __init__(self, number_range: int) -> None:
        self.range: int = number_range

    def game_logic(self)  -> None:
        if self.user_input == self.computer_input:
            print(
                f"Congratulations!! you got it {self.computer_input} was the right answer."
            )

    def user(self) -> int:
        while True:
            try:
                self.user_input = int(
                    input("A number has been generated. Guess what it is!: ")
                )
                return self.user_input
            except ValueError:
                print("Error: Must be a number\n")

    def computer(self) -> int:
        self.computer_input: int = random.randrange(self.range)
        return self.computer_input


def main() -> None:
    print("\nHi!, welcome to the Number Guessing Game.\n")
    print("What difficulty would you like:\n")
    
    game_range: int = ngg_utility.get_game_range()
    
    Game(game_range)


if __name__ == "__main__":
    main()

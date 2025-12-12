#

import random

print("Hi!, Welcome to the Number Guessing Game.")


class Game:
    def __init__(self):
        print("What game difficulty would you like?:\n  ")

        levels = {"easy": 10, "hard": 50, "insane": 100}

        for idx, (k, v) in enumerate(levels.items(), start=1):
            print(f"Level {idx}: {k.title()} (1 ~ {v})\n")

        if game_level := self.get_user_level(levels) == "q":
            print("Closing game...")
        else:
            self.game_logic(self.get_computer_input(game_level))

    def get_user_level(self, levels: dict[str, int]):
        while True:
            prompt_input = input(
                "Please choose a game difficulty number ('q' to Quit)\n\n>    "
            ).strip()

            if prompt_input.lower() == "q":
                return "q"

            try:
                user_input = int(prompt_input)
            except ValueError:
                print(f"'{prompt_input}' is not a number")
                continue

            if user_input not in range(1, len(levels.values()) + 1):
                print(f"'{prompt_input}' is not a valid difficulty number.")
            else:
                return user_input

    def get_computer_input(self, game_level: int) -> int:
        return random.randint(1, game_level)

    def game_logic(self):
        max_value = self.difficulty_level
        least_value = 1
        while True:
            user_input = (
                input(
                    f"A number has been generated between {least_value} and {max_value}. Guess what it is!, 'Q' to quit: "
                )
                .strip()
                .upper()
            )
            if (user_input != "Q") and (not user_input.isdigit()):
                print(f"{user_input} is invalid, please give a value or 'Q' to quit.")
                continue

            if user_input == "Q":
                return

            user_input = int(user_input)

            if user_input not in range(least_value, self.difficulty_level + 1):
                print(
                    f"{user_input} is not in the range of {least_value} ~ {max_value}."
                )
                continue

            if user_input == self.computer_input:
                print(
                    f"Congratulations!! you got it {user_input} was the right answer."
                )
                return

            if user_input > self.computer_input:
                max_value = user_input
                print(
                    f"You're above. The correct value is between {least_value} and {max_value}"
                )
            elif user_input < self.computer_input:
                least_value = user_input
                print(
                    f"You're below. The correct value is between {least_value} and {max_value}"
                )


def main():
    print("1. Easy: 1 ~ 10")
    print("2. Medium: 1 ~ 30")
    print("3. Hard: 1 ~ 50")
    print("4. Insane: 1 ~ 100")
    print("5. Omo: 1 ~ 1000")
    print("6. Ewo: 1 ~ 10000\n")

    game = Game()
    # game.game_logic()


if __name__ == "__main__":
    main()
    ...

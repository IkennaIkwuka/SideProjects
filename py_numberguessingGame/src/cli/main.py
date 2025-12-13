#

import random

print("Hi!, Welcome to the Number Guessing Game.")


class Game:
    def __init__(self):
        print("What game difficulty would you like?:\n  ")

        self.levels = {"easy": 10, "hard": 50, "insane": 100}

        for idx, (k, v) in enumerate(self.levels.items(), start=1):
            print(f"Level {idx}: {k.title()} (1 ~ {v})\n")

        game_level = self.get_game_level()

        if game_level == "q":
            print("Closing game...")
        else:
            computer_input = self.get_computer_number(game_level)

            while True:
                user_input = self.get_user_number(game_level)

                if self.game_logic(user_input, computer_input, game_level):
                    break

    def get_game_level(self):
        # Convert the values and keys to lists for indexing
        levels = list(self.levels.values())
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

            if user_input not in range(1, len(self.levels.values()) + 1):
                print(f"'{prompt_input}' is not a valid difficulty number.")
            else:
                return levels[user_input - 1]

    def get_computer_number(self, game_level: int) -> int:
        return random.randint(1, game_level)

    def get_user_number(self, game_level):
        while True:
            try:
                user_input = int(
                    input(
                        f"\nA number has been generated between 1 and {game_level}. Guess what it is!\n\n>    "
                    )
                )
            except ValueError:
                print("Not a number")
                continue

            if user_input not in range(1, game_level + 1):
                print(f"'{user_input}' is outside the range of 1 ~ {game_level}.")
            else:
                return user_input

    def game_logic(self, user_input, computer_input, game_level):
        if user_input == computer_input:
            print(f"Congratulations!! {user_input} was the right answer.")
            return True

        if user_input > computer_input:
            print(f"You're above. The correct value is between 1 and {user_input}")
        else:
            print(
                f"You're below. The correct value is between {user_input} and {game_level}"
            )

        return False


def main():
    # print("1. Easy: 1 ~ 10")
    # print("2. Medium: 1 ~ 30")
    # print("3. Hard: 1 ~ 50")
    # print("4. Insane: 1 ~ 100")
    # print("5. Omo: 1 ~ 1000")
    # print("6. Ewo: 1 ~ 10000\n")

    game = Game()
    # game.game_logic()


if __name__ == "__main__":
    main()
    # levels = {"easy": 10, "hard": 50, "insane": 100}
    # print(len(levels))
    # print(levels.items())
    # print(levels.keys())
    # print(levels.values())
    # print(levels.get("easy"))
    ...

#
# Logic service for the Number Guessing Game
#


class GameLogic:
    def __init__(self, levels: dict[int, int]):
        self.levels = levels

    def get_level(self, choice: str):
        choice = choice.strip()

        if choice.lower() == "q":
            return "q"

        try:
            level = int(choice)
            if not 1 <= level <= len(self.levels):
                print("Error: Please pick between a valid level")
                return
            return level
        except ValueError:
            print("Error: Please provide a number")
            return

    def get_user_guess(self, choice: str, current_min: int, current_max: int):
        try:
            value = int(choice)
            if value < current_min or value > current_max:
                print(
                    f"Error: Please make a valid guess between {current_min} and {current_max}"
                )
                return
            return value
        except ValueError:
            print("Error: Please provide a number")
            return


if __name__ == "__main__":
    ...  # for testing purposes

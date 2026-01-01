#
# Logic service for the Number Guessing Game
#


class GameLogic:
    def __init__(self, levels: dict[int, int]):
        self.levels = levels

    def game_difficulty(self, choice: str):
        choice = choice.strip()

        if choice.lower() == "q":
            return "q"

        try:
            difficulty_number = int(choice)
            if 1 <= difficulty_number <= len(self.levels):
                return difficulty_number
            return "out of Range"
        except ValueError:
            return "invalid Input"

    def user_number(self, choice: str, difficulty: int):
        try:
            value = int(choice)
            if 1 <= value <= difficulty:
                return value
            return "out of range"
        except ValueError:
            return "invalid input"

if __name__ == "__main__":
    ...  # for testing purposes
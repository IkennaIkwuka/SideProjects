#
# Logic service for the Number Guessing Game
#


class GameLogic:
    def __init__(self, game_levels: dict[int, int] ):
        self.game_levels = game_levels 

    def get_level(self, choice: str):
        choice = choice.strip()

        if choice.lower() == "q":
            return "q"

        if not self._is_number(choice):
            print("Error: Please provide a number")
            return

        if int(choice) < 1 or int(choice) > len(self.game_levels):
            print("Error: Please pick between a valid level")
            return
        return int(choice)

    def get_user_guess(self, choice: str, current_min: int, current_max: int):
        choice = choice.strip()

        if not self._is_number(choice):
            print("Error: Please provide a number")
            return

        if int(choice) < current_min or int(choice) > current_max:
            print(
                f"Error: Please make a valid guess between {current_min} and {current_max}"
            )
            return
        return int(choice)

    def _is_number(self, input_str:str):
        try:
            int(input_str)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    ...  # for testing purposes

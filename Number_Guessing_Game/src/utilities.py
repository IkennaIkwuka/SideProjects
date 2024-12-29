class Utility:
    def __init__(self) -> None: ...

    def get_game_range(self) -> int:
        while True:
            try:
                game_range = int(
                    input(
                        "Please give a number in whose range you'll guess what the correct number is:"
                    )
                )
                return game_range
            except ValueError:
                print("Error: Must be a number.")

ngg_utility = Utility()

if __name__ == "__main__":
    ...

# Number Guessing Game

Command-line number guessing game. Pick a difficulty (Easy 1-10, Hard 1-50, Insane 1-100), and try to guess the randomly generated number — each guess narrows the valid range until you find it or quit.

## How to Play

1. Choose a difficulty level (or `q` to quit).
2. Guess a number within the current range.
3. After each guess, you're told whether to go higher or lower, and the range narrows accordingly.
4. Keep guessing until you find the number, then choose whether to play again.

## Run

```bash
python3 scripts/game.py
```

## Structure

```
scripts/game.py     # entry point
src/cli/main.py      # game loop
src/cli/logic.py      # input validation
```

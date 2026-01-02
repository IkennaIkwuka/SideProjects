# Full Basic Calculator App Project

# TODO -- add a loop functionality that allows the user to write another expression to calculate or type 'q' to quit.

# ---Libs---
import textwrap  # ---lib to remove whitespace before each printed line---
from decimal import Decimal  # noqa: F401
from src.cli.logic import CalcLogic
from src.cli.utils.helpers import _twe

# SHOW_DEBUG = True
SHOW_DEBUG = False


class CalcApp:
    def __init__(self, logic: CalcLogic | None = None):
        menu = """
        Hi! This is a basic CLI Calculator
        You can carry out any of these operations with their respective symbols:
        Addition -- +
        Subtraction -- -
        Multiplication -- *
        Division -- /
        Exponentiation -- ^
        Modulus -- %
        """
        _twe(textwrap.dedent(menu))

        self.logic = logic if logic is not None else CalcLogic()

    def run(self):
        print("What do you want to calculate?\n")
        while True:
            expression = input("(`q` to quit)\n\n> ").strip()

            result = self.logic.get_expr(expression)

            if not result:
                continue

            if result == "q":
                break

            # replaces `^` with `**` as thats what python eval understands
            result = result.replace("^", "**")

            self.eval_expr(result)

    def eval_expr(self, expr: str):
        try:
            if SHOW_DEBUG:
                print(f"\nUser's expression:\n\n{expr}\n\nEvaluating...\n")
            result = eval(expr)
            print(f"\n...Successful\n\nResult = {result}\n")
        except OverflowError:
            self.fix_expr(expr)

    # method to fix overflowError
    def fix_expr(self, expr: str):
        error_msg = """
        OverflowError: Your expression ran into an overflow error.\n
        This can be due to:
            - Huge exponent.
            - Combined with true division '/'.\n
        The program will now 'fix' your expression.\n
        Wrapping operands in 'Decimal()'...\n
        """
        if SHOW_DEBUG:
            print(textwrap.dedent(error_msg))

        values = expr.split()

        for i, val in enumerate(values):
            if i % 2 == 0:
                # adds Decimal() wrap to operands to prevent overflow
                values[i] = values[i].replace(f"{val}", f"Decimal({val})")

        expr = " ".join(values)

        if SHOW_DEBUG:
            print(
                f"...Successful\n\nUser's fixed expression:\n\n{expr}\nEvaluating...\n"
            )

        result = eval(expr)

        print(f"\n...Successful\n\nResult = {result}\n\n")


def main():
    CalcApp().run()


if __name__ == "__main__":
    main()
    ...

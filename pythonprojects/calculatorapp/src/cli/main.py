# Full Basic Calculator App Project

# TODO -- add a loop functionality that allows the user to write another expression to calculate or type 'q' to quit.

# ---Libs---
import textwrap  # ---lib to remove whitespace before each printed line---
from decimal import Decimal  # noqa: F401
from src.cli.logic import CalcLogic
from src.cli.utils.helpers import _twe


class CalcApp:
    SUCCESS_MSG = "\n...Success"

    def __init__(self, logic: CalcLogic | None = None):
        menu = "App Starts...\n\nWelcome to the Basic Calculator Terminal App...\n\nApart from the accepted symbols; fractions and decimals are allowed and must be written in together e.g 12/4, 34.22.\n\nAccepted symbols:-\nAddition        >   +\nSubtraction     >   -\nMultiplication  >   *\nDivision        >   /\nExponentiation  >   ^\nModulus         >   %\n\nThe user's expression must follow the order of operand | operator | operand | operator...\n\nwhere '|' is the space in between.\n\nLetters are absolutely not allowed. Enjoy!!"
        print(menu, 0.0005)

        self.logic = logic if logic is not None else CalcLogic()

    def run(self):
        print("What do you want to calculate?\n")

        while True:
            expression = input("(`q` to quit)\n> ").strip()

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
            print(f"\nUser's expression:\n{expr}\nEvaluating...")

            result = eval(expr)

            print(self.SUCCESS_MSG)
            print(f"\nResult = {result}", 0.05)
        except OverflowError:
            self.fix_expr(expr)

    # method to fix overflowError
    def fix_expr(self, expr: str):
        error_msg = """
        OverflowError: Your expression ran into an overflow error.\n
        This can be due to:
            - Huge exponent.
            - Combined with true division '/'.\n
        The program will now 'fix' your expression.
        """
        print(textwrap.dedent(error_msg))

        print("Wrapping operands in 'Decimal()'...", 0.05)

        values = expr.split()

        for i, val in enumerate(values):
            if i % 2 == 0:
                # adds Decimal() wrap to operands to prevent overflow
                values[i] = values[i].replace(f"{val}", f"Decimal({val})")

        print(self.SUCCESS_MSG)

        expr = " ".join(values)

        print(f"\nUser's fixed expression:\n{expr}")
        print("\nEvaluating...")

        result = eval(expr)

        print("\n...Success")
        print(f"\nResult = {result}", 0.05)


def main():
    CalcApp().run()


if __name__ == "__main__":
    main()
    ...

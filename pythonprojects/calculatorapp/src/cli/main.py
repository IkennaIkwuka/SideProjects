# Full Basic Calculator App Project

# TODO -- add a loop functionality that allows the user to write another expression to calculate or type 'q' to quit.

# ---Libs---
import re
import textwrap  # ---lib to remove whitespace before each printed line---
from decimal import Decimal  # noqa: F401
from src.cli.logic import CalcLogic
from src.cli.utils.helpers import _twe


class CalcApp:
    SUCCESS_MSG = "\n...Success"

    def __init__(self, logic: CalcLogic | None = None):
        menu = "App Starts...\n\nWelcome to the Basic Calculator Terminal App...\n\nApart from the accepted symbols; fractions and decimals are allowed and must be written in together e.g 12/4, 34.22.\n\nAccepted symbols:-\nAddition        >   +\nSubtraction     >   -\nMultiplication  >   *\nDivision        >   /\nExponentiation  >   ^\nModulus         >   %\n\nThe user's expression must follow the order of operand | operator | operand | operator...\n\nwhere '|' is the space in between.\n\nLetters are absolutely not allowed. Enjoy!!"
        _twe(menu, 0.0005)

        self.logic = logic if logic is not None else CalcLogic()

    def run(self):
        print("What do you want to calculate?\n")

        # while True:
        # TODO do that here
        while True:
            expression = input("(`q` to quit)> ").strip()

            # if expression == "q":
            expr = ""
            #     return False

            result = self.logic.get_expr(expression)

            if not result or result == "q":
                break

            print(result)  # ---debug---

        # try:
        #     _twe(f"\nUser's expression:\n{expr}")
        #     _twe("\nEvaluating...")

        #     result = eval(expr)

        #     _twe(self.SUCCESS_MSG)
        #     _twe(f"\nResult = {result}", 0.05)
        # except OverflowError:
        #     self.fix_str(expr)

    # ---method to fix overflowError---
    def fix_str(self, expr: str):
        error_msg = """
        OverflowError: Your expression ran into an overflow error.
        
        This can be due to:
            - Huge exponent.
            - Combined with true division '/'.
        
        The program will now 'fix' your expression.
        """
        _twe(textwrap.dedent(error_msg))

        _twe("Wrapping operands in 'Decimal()'...", 0.05)

        values = expr.split()

        for i in range(0, len(values), 2):
            # ---adds Decimal() wrap to operands to prevent overflow---
            values[i] = f"Decimal({values[i]})"

        _twe(self.SUCCESS_MSG)

        expr = " ".join(values)

        _twe(f"\nUser's fixed expression:\n{expr}")
        _twe("\nEvaluating...")

        result = eval(expr)

        _twe("\n...Success")
        _twe(f"\nResult = {result}", 0.05)


def main():
    CalcApp().run()


if __name__ == "__main__":
    main()
    ...

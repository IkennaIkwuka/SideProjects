# Full Basic Calculator App Project

# TODO -- add a loop functionality that allows the user to write another expression to calculate or type 'q' to quit.

# ---Libs---
from utils.python import twe_
import textwrap  # ---lib to remove whitespace before each printed line---
from decimal import Decimal  # noqa: F401


class calc_app:
    def __init__(self) -> None:
        _ = """
        App Starts...
        
        Welcome to the Basic Calculator Terminal App...
        
        Apart from the accepted symbols; fractions and decimals are allowed and must be written in together e.g 12/4, 34.22.

        Accepted symbols:-
        Addition        >   +
        Subtraction     >   -
        Multiplication  >   *
        Division        >   /
        Exponentiation  >   ^
        Modulus         >   %
        
        The user's expression must follow the order of operand | operator | operand | operator...
        
        where '|' is the space in between.
        
        Letters are absolutely not allowed. Enjoy!!
        """
        twe_(textwrap.dedent(_), 0.0005)

        prompt = "What do you want to calculate?\n:  "

        expr = ""

        # while True:
        # TODO do that here
        user_input = input(prompt).strip().lower()

        # if user_input == "q":
        #     return False

        expr = self.validate_str(user_input)

        try:
            twe_(f"\nUser's expression:\n{expr}")
            twe_("\nEvaluating...")

            result = eval(expr)

            twe_("\n...Success")
            twe_(f"\nResult = {result}", 0.05)
        except OverflowError:
            self.fix_str(expr)

    # ---method to fix overflowError---
    def fix_str(self, expr: str):
        error_msg = """
        OverflowError: Your expression ran into an overflow error.
        
        This can be due to:
            - Huge exponent.
            - Combined with true division '/'.
        
        The program will now 'fix' your expression.
        """
        twe_(textwrap.dedent(error_msg))

        twe_("Wrapping operands in 'Decimal()'...", 0.05)

        values = expr.split()

        for i in range(0, len(values), 2):
            # ---adds Decimal() wrap to operands to prevent overflow---
            values[i] = f"Decimal({values[i]})"

        twe_("\n...Success")

        expr = " ".join(values)

        twe_(f"\nUser's fixed expression:\n{expr}")
        twe_("\nEvaluating...")

        result = eval(expr)

        twe_("\n...Success")
        twe_(f"\nResult = {result}", 0.05)

    def check_operator(self, operator: str):
        standalone = {"+", "*", "-", "/"}

        for sep in standalone:
            if operator == sep:
                return True
            continue
        return False

    def check_operand(self, operand: str):
        if operand.isdigit():
            return True

        if operand == "/":
            return False  # ---fix for duplicate last value error---

        inner_sep = {".", "%", "^", "/"}

        for sep in inner_sep:
            if sep == operand:
                return False
            if sep in operand:
                left, right = operand.split(sep, 1)
                if left.isdigit() and right.isdigit():
                    return True
                return False
            continue
        return False

    # ---validates user input---
    def validate_str(self, user_input: str):
        values = user_input.split()
        operands: list[str] = []
        operators: list[str] = []
        expr = ""

        # ---checks whether last value is not an operand or not---
        if not self.check_operand(values[-1]):
            raise ValueError(
                f"Input: {values}\n\tError: You cannot end with '{values[-1]}'"
            )

        # ---checks the order of values inputted alternating operands/operator by order of operand | operator | operand | operator | etc---
        for i, val in enumerate(values):
            if i % 2 == 0:
                if not self.check_operand(val):
                    raise ValueError(
                        f"Input: {values}\n\tError: Value number {i}. {values[i]} is invalid."
                        "Expected an operand."
                    )
                operands.append(val)
            else:
                if not self.check_operator(val):
                    raise ValueError(
                        f"Input: {values}\n\tError: Value number {i}. {values[i]} is invalid."
                        "Expected an operator."
                    )
                operators.append(val)

        for ops, opt in zip(operands, operators):
            expr += ops + " " + opt + " "

        expr += f"{operands[-1]}"

        # ---converts "^" to "**" for eval() to work with "^" in python---
        expr = expr.replace("^", "**")

        return expr


if __name__ == "__main__":
    calc_app()

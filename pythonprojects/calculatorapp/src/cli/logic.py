#


class CalcLogic:
    # ---validates user input---
    def get_expr(self, expression: str):
        if not expression:
            return "error"

        values = expression.split()

        if not self._is_sequence_valid(values):
            return "error"

        operands = []
        operators = []

        raise_error = False

        for i, val in enumerate(values):
            if not values[-1].isdigit() and not self.check_operand(values[-1]):
                print(f"Error: Expression {values[-1]} must end with an operand.")
                raise_error = True
                break

            if i % 2 == 0 and not val.isdigit() and not self.check_operand(val):
                print(f"Error: Expression {val} must be a valid operand.")
                raise_error = True
                break
            elif i % 2 == 0:
                operands.append(val)

            if i % 2 != 0 and val not in "+-*/^%." and not self.check_operator(val):
                print(f"Error: Expression {val} must be a valid operator.")
                raise_error = True
                break
            elif i % 2 != 0:
                if val == "^":
                    # ---converts "^" to "**" for eval() to work with "^" in python---
                    val = val.replace("^", "**")
                operators.append(val)

        if raise_error:
            return "error"
        return self._build_expr(operands, operators)

    def _is_sequence_valid(self, values: list[str]):
        if len(values) % 2 == 0:
            return False

        for i, val in enumerate(values):
            if i % 2 == 0:
                if not self.check_operand(val):
                    print(f"Error: {val} is not an operand")
                    return False
            else:
                if not self.check_operator(val):
                    print(f"Error: {val} is not a valid operator")
                    return False

        return True

    def _build_expr(self, operands: list[str], operators: list[str]):
        expr = ""

        for ops, opr in zip(operands, operators):
            expr += f"{ops} {opr} "

        return expr + operands[-1]

    def check_operator(self, operator: str):
        return operator in ("+", "*", "-", "/")

    def check_operand(self, operand: str):
        if not operand.isdigit():
            return False


        inner_sep = (".", "%", "^", "/")

        for sep in inner_sep:
            elif sep in operand:
                left, right = operand.split(sep, 1)
                if left.isdigit() and right.isdigit():
                    return True
                else:
                    return False
            else:
                continue

        return False

#


class CalcLogic:
    # ---validates user input---
    def get_expr(self, expression: str) -> None | str:
        if not expression:
            print("Error: Missing input")
            return

        if expression.strip().lower() == "q":
            return "q"

        values = expression.split()

        if not self._is_sequence_valid(values):
            return

        operands = [val for i, val in enumerate(values) if i % 2 == 0]

        operators = [
            val.replace("^", "**") for i, val in enumerate(values) if i % 2 != 0
        ]

        return self._build_expr(operands, operators)

    def _build_expr(self, operands: list[str], operators: list[str]) -> str:
        expression: list[str] = []

        for ops, opr in zip(operands, operators):
            expression.append(ops)
            expression.append(opr)

        expression.append(operands[-1])

        return " ".join(expression)

    def _is_sequence_valid(self, values: list[str]) -> bool:
        for i, val in enumerate(values):
            if i % 2 == 0:
                if not self._check_operand(val):
                    print(f"Error: {val} is not a valid operand")
                    return False
            else:
                if not self._check_operator(val):
                    print(f"Error: {val} is not a valid operator")
                    return False

        if len(values) % 2 == 0:
            print("Error: The last value must be an operand")
            return False

        return True

    def _check_operator(self, operator: str) -> bool:
        return operator in ("+", "*", "-", "/")

    def _check_operand(self, operand: str) -> bool:
        if operand.isdigit():
            return True

        for i in (".", "%", "^", "/"):
            if i in operand:
                parts = operand.split(i, 1)
                return len(parts) == 2 and all(p.isdigit() for p in parts)
        return False

import pytest
from src.cli.logic import CalcLogic


@pytest.fixture
def calc():
    return CalcLogic()


class TestCalcLogic:
    # --- Tests for get_expr ---

    def test_get_expr_empty_input(self, calc: CalcLogic):
        assert calc.get_expr("") is None

    def test_get_expr_quit(self, calc: CalcLogic):
        assert calc.get_expr("q") == "q"
        assert calc.get_expr("Q") == "q"

    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("1 + 2", "1 + 2"),
            ("10.5 * 2 / 5", "10.5 * 2 / 5"),
            ("1/2 + 3/4", "1/2 + 3/4"),
            ("5", "5"),
        ],
    )
    def test_get_expr_valid_sequences(
        self, calc: CalcLogic, input_str: str, expected: str
    ):
        assert calc.get_expr(input_str) == expected

    @pytest.mark.parametrize(
        "input_str",
        [
            ("1 +"),  # Ends in operator
            ("+ 1"),  # Starts with operator
            ("1 + 2 +"),  # Ends in operator
            ("1 plus 2"),  # Invalid operator
            ("abc + 2"),  # Invalid operand
            ("1 + 2.5.5"),  # Malformed float
        ],
    )
    def test_get_expr_invalid_sequences(self, calc: CalcLogic, input_str: str):
        assert calc.get_expr(input_str) is None

    # --- Tests for Internal Validation Methods ---

    @pytest.mark.parametrize(
        "operand, expected",
        [
            ("123", True),
            ("1.5", True),
            ("1/2", True),
            ("10%2", True),
            ("2^3", True),
            ("1.2.3", False),  # Too many separators
            ("abc", False),  # Not numeric
            ("1/", False),  # Incomplete
            ("/1", False),  # Incomplete
        ],
    )
    def test_check_operand(self, calc: CalcLogic, operand: str, expected: bool):
        assert calc._check_operand(operand) == expected

    @pytest.mark.parametrize(
        "operator, expected",
        [
            ("+", True),
            ("-", True),
            ("*", True),
            ("/", True),
            ("**", False),
            ("plus", False),
        ],
    )
    def test_check_operator(self, calc: CalcLogic, operator: str, expected: bool):
        assert calc._check_operator(operator) == expected

    def test_build_expr(self, calc: CalcLogic):
        operands = ["1", "2", "3"]
        operators = ["+", "*"]
        assert calc._build_expr(operands, operators) == "1 + 2 * 3"

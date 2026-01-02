import pytest
from src.cli.logic import GameLogic


@pytest.fixture
def logic(levels: dict[int, int]):
    return GameLogic(levels)


@pytest.fixture
def levels():
    return {1: 10, 2: 50, 3: 100}


# --- Tests for get_level ---


def test_get_level_no_input(logic: GameLogic):
    assert logic.get_level("") is None


def test_get_level_quit(logic: GameLogic):
    assert logic.get_level("q") == "q"
    assert logic.get_level("Q") == "q"


@pytest.mark.parametrize(
    "input_str,expected",
    [("1", 1), ("2", 2), ("3", 3)],
)
def test_get_level_valid(logic: GameLogic, input_str: str, expected: str):
    assert logic.get_level(input_str) == expected


@pytest.mark.parametrize(
    "input_str",
    [("-123"), ("123"), ("abc")],
)
def test_get_level_invalid(logic: GameLogic, input_str: str):
    assert logic.get_level(input_str) is None


# -- Tests for get_user_guess ---


@pytest.mark.parametrize(
    "input_str,expected",
    [("1", 1), ("2", 2), ("3", 3)],
)
def test_get_user_guess_valid(logic: GameLogic, input_str: str, expected: str):
    assert logic.get_user_guess(input_str, 1, 100) == expected


@pytest.mark.parametrize(
    "input_str",
    [("123"), ("-123"), ("abc")],
)
def test_get_user_guess_invalid(logic: GameLogic, input_str: str):
    assert logic.get_user_guess(input_str, 1, 100) is None


# --- Tests for internal methods ---


def test_is_number_valid(logic: GameLogic):
    assert logic._is_number("123") is True


def test_is_number_invalid(logic: GameLogic):
    assert logic._is_number("abc") is False

from src.services.logic import GameLogic
import pytest


@pytest.fixture
def levels():
    return {1: 10, 2: 50, 3: 100}


@pytest.fixture
def logic(levels: dict[int, int]):
    return GameLogic(levels)


def test_game_difficulty(logic):
    assert logic.game_difficulty("1") == 1
    assert logic.game_difficulty("2") == 2
    assert logic.game_difficulty("3") == 3
    assert logic.game_difficulty("q") == "q"
    assert logic.game_difficulty("4") == "out of Range"
    assert logic.game_difficulty("0") == "out of Range"
    assert logic.game_difficulty("abc") == "invalid Input"


def test_user_number(logic):
    assert logic.user_number("3", 10) == 3
    assert logic.user_number("8", 10) == 8
    assert logic.user_number("0", 10) == "out of range"
    assert logic.user_number("11", 10) == "out of range"
    assert logic.user_number("abc", 10) == "invalid input"

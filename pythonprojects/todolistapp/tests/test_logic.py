import pytest
from src.cli.logic import AppLogic

# ------------------
# Fixtures
# ------------------


@pytest.fixture
def logic():
    return AppLogic()


# Tests for menu


@pytest.mark.parametrize("input_str,expected", [("2", 2), ("Q", "q")])
def test_app_menu_valid_input(logic: AppLogic, input_str: str, expected: str):
    assert logic.app_menu(input_str, 4) == expected


@pytest.mark.parametrize("input_str", [("abc"), ("123"), ("-123"), ("")])
def test_app_menu_invalid(logic: AppLogic, input_str: str):
    assert logic.app_menu(input_str, 4) is None


# Tests for add_tasks


@pytest.mark.parametrize("input_str,expected", [("New Task", "New Task"), ("Q", "q")])
def test_create_tasks_valid_inputs(logic: AppLogic, input_str: str, expected: str):
    assert logic.create_tasks(input_str) == expected


@pytest.mark.parametrize("input_str", [("")])
def test_create_tasks_invalid(logic: AppLogic, input_str: str):
    assert logic.create_tasks(input_str) is None


# Test for remove_tasks


@pytest.mark.parametrize(
    "input_str,expected", [("D", "d"), ("Q", "q"), ("V", "v"), ("2", 2)]
)
def test_remove_tasks_valid(logic: AppLogic, input_str: str, expected: str):
    assert logic.remove_tasks(input_str) == expected


@pytest.mark.parametrize("input_str", [(""), ("abc")])
def test_remove_tasks_invalid(logic: AppLogic, input_str: str):
    assert logic.remove_tasks(input_str) is None


# Test for edit_tasks


@pytest.mark.parametrize("input_str,expected", [("Q", "q"), ("V", "v"), ("2", 2)])
def test_edit_tasks_valid(logic: AppLogic, input_str: str, expected: str):
    assert logic.edit_tasks(input_str) == expected


@pytest.mark.parametrize("input_str", [(""), ("abc")])
def test_edit_tasks_invalid(logic: AppLogic, input_str: str):
    assert logic.edit_tasks(input_str) is None

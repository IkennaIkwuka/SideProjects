import pytest
from src.cli.logic import AppLogic

# ------------------
# Fixtures
# ------------------


@pytest.fixture
def logic(tasks):
    return AppLogic(tasks)


@pytest.fixture
def tasks():
    return ["Task 1", "Task 2", "Task 3"]


# Tests for menu


@pytest.mark.parametrize(
    "input_str,expected",
    [("2", 2), ("Q", "q")],
)
def test_menu_valid(logic: AppLogic, input_str: str, expected: str):
    assert logic.menu(input_str) == expected


@pytest.mark.parametrize("input_str", [("abc"), ("123"), ("-123"), ("")])
def test_menu_invalid(logic: AppLogic, input_str: str):
    assert logic.menu(input_str) is None


# Tests for add_tasks


@pytest.mark.parametrize("input_str,expected", [("New Task", "New Task"), ("Q", "q")])
def test_add_tasks_valid(logic: AppLogic, input_str: str, expected: str):
    assert logic.add_tasks(input_str) == expected


@pytest.mark.parametrize("input_str", [(""), ("Task 1")])
def test_add_tasks_invalid(logic: AppLogic, input_str: str):
    assert logic.add_tasks(input_str) is None


# Test for remove_tasks


@pytest.mark.parametrize(
    "input_str,expected",
    [("D", "d"), ("Q", "q"), ("V", "v"), ("2", 2)],
)
def test_remove_tasks_valid(logic: AppLogic, input_str: str, expected: str):
    assert logic.remove_tasks(input_str) == expected


@pytest.mark.parametrize("input_str", [(""), ("abc"), ("123"), ("-123")])
def test_remove_tasks_invalid(logic: AppLogic, input_str: str):
    assert logic.remove_tasks(input_str) is None


# Test for edit_tasks


@pytest.mark.parametrize(
    "input_str,expected",
    [("Q", "q"), ("V", "v"), ("2", 2)],
)
def test_edit_tasks_valid(logic: AppLogic, input_str: str, expected: str):
    assert logic.edit_tasks(input_str) == expected


@pytest.mark.parametrize("input_str", [(""), ("abc"), ("123"), ("-123")])
def test_edit_tasks_invalid(logic: AppLogic, input_str: str):
    assert logic.edit_tasks(input_str) is None


# Test for update_tasks
@pytest.mark.parametrize("input_str,expected", [("updated task", "updated task")])
def test_update_task_valid(logic: AppLogic, input_str: str, expected: str):
    assert logic.updated_task(input_str) == expected


@pytest.mark.parametrize("input_str", [("Task 1"), ("")])
def test_update_task_invalid(logic: AppLogic, input_str: str):
    assert logic.updated_task(input_str) is None

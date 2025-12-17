import pytest
from py_todolistApp.src.cli.logic import AppLogic, TaskStatus


@pytest.fixture
def tasks():
    return ["Task 1", "Task 2", "Task 3"]


@pytest.fixture
def logic(tasks: list[str]):
    return AppLogic(tasks)


# ------------------
# HUB TESTS
# ------------------


@pytest.mark.parametrize(
    "user_input, actions, expected",
    [
        ("", {1: None}, TaskStatus.EMPTY),
        (" ", {1: None}, TaskStatus.EMPTY),
        ("q", {1: None}, TaskStatus.QUIT),
        ("abc", {1: None}, TaskStatus.INVALID),
        ("'[;,]", {1: None}, TaskStatus.INVALID),
        ("6", {1: None, 2: None}, TaskStatus.OUT_OF_RANGE),
        ("-2", {1: None, 2: None}, TaskStatus.OUT_OF_RANGE),
        ("3", {1: None, 2: None, 3: None}, 3),
    ],
)
def test_validate_hub_inputs(logic, user_input, actions, expected):
    assert logic.validate_hub(user_input, actions) == expected


def test_force_add_tasks_when_empty():
    logic = AppLogic([])
    assert logic.force_add_tasks(1) is True
    assert logic.force_add_tasks(2) is False


def test_force_add_tasks_when_exists():
    logic = AppLogic(["Task 1", "Task 2"])
    assert logic.force_add_tasks(1) is False


# ------------------
# ADD TASK TESTS
# ------------------


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("", TaskStatus.EMPTY),
        (" ", TaskStatus.EMPTY),
        ("q", TaskStatus.QUIT),
        ("Task 1", TaskStatus.EXISTS),
        ("New Task", "New Task"),
    ],
)
def test_validate_add_task(logic, user_input, expected):
    assert logic.validate_add_tasks(user_input) == expected


# ------------------
# REMOVE TASK TESTS
# ------------------


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("", TaskStatus.EMPTY),
        (" ", TaskStatus.EMPTY),
        ("q", TaskStatus.QUIT),
        ("d", TaskStatus.DELETE_ALL),
        ("v", TaskStatus.VIEW),
        ("abcde", TaskStatus.INVALID),
        ("[];',", TaskStatus.INVALID),
        ("4", TaskStatus.OUT_OF_RANGE),
        ("-3", TaskStatus.OUT_OF_RANGE),
        ("3", 3),
    ],
)
def test_validate_remove_tasks(logic, user_input, expected):
    assert logic.validate_remove_tasks(user_input) == expected


# ------------------
# EDIT TASK TESTS
# ------------------


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("", TaskStatus.EMPTY),
        (" ", TaskStatus.EMPTY),
        ("q", TaskStatus.QUIT),
        ("v", TaskStatus.VIEW),
        ("abcde", TaskStatus.INVALID),
        ("[];',", TaskStatus.INVALID),
        ("4", TaskStatus.OUT_OF_RANGE),
        ("-3", TaskStatus.OUT_OF_RANGE),
        ("3", 3),
    ],
)
def test_validate_edit_tasks(logic, user_input, expected):
    assert logic.validate_edit_tasks(user_input) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("", TaskStatus.EMPTY),
        (" ", TaskStatus.EMPTY),
        ("Task 1", TaskStatus.EXISTS),
        ("Updated Task", "Updated Task"),
    ],
)
def test_validate_updated_task(logic, user_input, expected):
    assert logic.validate_updated_task(user_input) == expected

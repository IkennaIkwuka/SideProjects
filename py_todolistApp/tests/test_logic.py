import pytest
from py_todolistApp.src.cli.logic import AppLogic, TaskStatus


# ------------------
# Fixtures
# ------------------


@pytest.fixture
def logic():
    return AppLogic(["Task 1", "Task 2", "Task 3"])


@pytest.fixture
def actions():
    return {1: None, 2: None, 3: None}


# ------------------
# Shared Input Constants
# ------------------


EMPTY_INPUTS = [""]
QUIT_INPUTS = ["q"]
INVALID_INPUTS = ["abc"]
OUT_OF_RANGE_INPUTS = ["4", "-3"]  # outside the length of actions() fixture
DELETE_ALL_INPUTS = ["d"]
VIEW_INPUTS = ["v"]


# ------------------
# HUB TESTS
# ------------------


@pytest.mark.parametrize("user_input", EMPTY_INPUTS)
def test_validate_hub_empty(logic, user_input, actions):
    assert logic.validate_hub(user_input, actions) == TaskStatus.EMPTY


@pytest.mark.parametrize("user_input", QUIT_INPUTS)
def test_validate_hub_quit(logic, user_input, actions):
    assert logic.validate_hub(user_input, actions) == TaskStatus.QUIT


@pytest.mark.parametrize("user_input", INVALID_INPUTS)
def test_validate_hub_invalid(logic, user_input, actions):
    assert logic.validate_hub(user_input, actions) == TaskStatus.INVALID


@pytest.mark.parametrize("user_input", OUT_OF_RANGE_INPUTS)
def test_validate_hub_out_of_range(logic, user_input, actions):
    assert logic.validate_hub(user_input, actions) == TaskStatus.OUT_OF_RANGE


def test_validate_hub_valid(logic):
    actions = {1: None, 2: None}
    assert logic.validate_hub("2", actions) == 2


# ------------------
# ADD, REMOVE, EDIT, UPDATED TASKS TESTS
# ------------------


@pytest.mark.parametrize("user_input", EMPTY_INPUTS)
def test_add_remove_edit_updated_tasks_empty(logic, user_input):
    assert logic.validate_add_tasks(user_input) == TaskStatus.EMPTY
    assert logic.validate_remove_tasks(user_input) == TaskStatus.EMPTY
    assert logic.validate_edit_tasks(user_input) == TaskStatus.EMPTY
    assert logic.validate_updated_task(user_input) == TaskStatus.EMPTY


@pytest.mark.parametrize("user_input", QUIT_INPUTS)
def test_add_remove_edit_tasks_quit(logic, user_input):
    assert logic.validate_add_tasks(user_input) == TaskStatus.QUIT
    assert logic.validate_remove_tasks(user_input) == TaskStatus.QUIT
    assert logic.validate_edit_tasks(user_input) == TaskStatus.QUIT


@pytest.mark.parametrize("user_input", DELETE_ALL_INPUTS)
def test_remove_tasks_delete_all(logic, user_input):
    assert logic.validate_remove_tasks(user_input) == TaskStatus.DELETE_ALL


@pytest.mark.parametrize("user_input", VIEW_INPUTS)
def test_remove_edit_tasks_view(logic, user_input):
    assert logic.validate_remove_tasks(user_input) == TaskStatus.VIEW
    assert logic.validate_edit_tasks(user_input) == TaskStatus.VIEW


@pytest.mark.parametrize("user_input", INVALID_INPUTS)
def test_remove_edit_tasks_invalid(logic, user_input):
    assert logic.validate_remove_tasks(user_input) == TaskStatus.INVALID
    assert logic.validate_edit_tasks(user_input) == TaskStatus.INVALID


@pytest.mark.parametrize("user_input", OUT_OF_RANGE_INPUTS)
def test_remove_edit_tasks_out_of_range(logic, user_input):
    assert logic.validate_remove_tasks(user_input) == TaskStatus.OUT_OF_RANGE
    assert logic.validate_edit_tasks(user_input) == TaskStatus.OUT_OF_RANGE


def test_add_remove_edit_updated_tasks_valid(logic):
    assert logic.validate_add_tasks("New Task") == "New Task"
    assert logic.validate_remove_tasks("3") == 3
    assert logic.validate_edit_tasks("3") == 3
    assert logic.validate_updated_task("Updated Task") == "Updated Task"


def test_add_updated_tasks_exists(logic):
    assert logic.validate_add_tasks("Task 1") == TaskStatus.EXISTS
    assert logic.validate_updated_task("Task 1") == TaskStatus.EXISTS

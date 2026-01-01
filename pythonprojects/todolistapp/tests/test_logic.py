import pytest
from src.cli.services.logic import AppLogic
from src.cli.models.status import TaskStatus

# ------------------
# Fixtures
# ------------------


@pytest.fixture
def test_logic(fake_tasks):
    return AppLogic(fake_tasks)


@pytest.fixture
def fake_tasks():
    return ["Task 1", "Task 2", "Task 3"]


@pytest.fixture
def fake_menu_options():
    return ("save", "view", "add", "remove")


# -------------------
# Tests
# -------------------


def test_menu(test_logic, fake_menu_options):
    assert test_logic.menu("q", fake_menu_options) == TaskStatus.QUIT
    assert test_logic.menu("abc", fake_menu_options) == TaskStatus.INVALID
    assert test_logic.menu("", fake_menu_options) == TaskStatus.INVALID
    assert (
        test_logic.menu(str(len(fake_menu_options) + 1), fake_menu_options)
        == TaskStatus.OUT_OF_RANGE
    )
    assert test_logic.menu(str(len(fake_menu_options)), fake_menu_options) == len(
        fake_menu_options
    )


def test_add_tasks(test_logic):
    assert test_logic.add_tasks("q") == TaskStatus.QUIT
    assert test_logic.add_tasks("Task 1") == TaskStatus.EXISTS
    assert test_logic.add_tasks("") == TaskStatus.INVALID
    assert test_logic.add_tasks("New Task") == "New Task"


def test_remove_tasks(test_logic, fake_tasks):
    assert test_logic.remove_tasks("q") == TaskStatus.QUIT
    assert test_logic.remove_tasks("d") == TaskStatus.DELETE_ALL
    assert test_logic.remove_tasks("v") == TaskStatus.VIEW
    assert test_logic.remove_tasks("abc") == TaskStatus.INVALID
    assert test_logic.remove_tasks(str(len(fake_tasks) + 1)) == TaskStatus.OUT_OF_RANGE
    assert test_logic.remove_tasks(str(len(fake_tasks))) == len(fake_tasks)


def test_edit_tasks(test_logic, fake_tasks):
    assert test_logic.edit_tasks("q") == TaskStatus.QUIT
    assert test_logic.edit_tasks("v") == TaskStatus.VIEW
    assert test_logic.edit_tasks("abc") == TaskStatus.INVALID
    assert test_logic.remove_tasks(str(len(fake_tasks) + 1)) == TaskStatus.OUT_OF_RANGE
    assert test_logic.remove_tasks(str(len(fake_tasks))) == len(fake_tasks)


def test_update_task(test_logic):
    assert test_logic.updated_task("Task 1") == TaskStatus.EXISTS
    assert test_logic.updated_task("") == TaskStatus.INVALID
    assert test_logic.updated_task("Updated Task") == "Updated Task"


def test_delete_all_confirmation(test_logic):
    assert test_logic.delete_all_confirmation("other") == TaskStatus.INVALID
    assert test_logic.delete_all_confirmation("3") == TaskStatus.INVALID
    assert test_logic.delete_all_confirmation("y") is True
    assert test_logic.delete_all_confirmation("n") is False


def test_get_messages(test_logic):
    assert test_logic.get_message(TaskStatus.OUT_OF_RANGE) == "Out of range."
    assert test_logic.get_message(TaskStatus.INVALID) == "Invalid input."
    assert test_logic.get_message(TaskStatus.EXISTS) == "Task exists."
    assert test_logic.get_message(None) == ""
    assert test_logic.get_message("abc") == ""
    assert test_logic.get_message(3) == ""

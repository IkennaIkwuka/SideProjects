import pytest
from cli.logic import AppLogic

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
    assert test_logic.menu("q", fake_menu_options) == "q"
    assert test_logic.menu("abc", fake_menu_options) is None
    assert test_logic.menu("", fake_menu_options) is None
    assert test_logic.menu(str(len(fake_menu_options) + 1), fake_menu_options) is None
    assert test_logic.menu(str(len(fake_menu_options)), fake_menu_options) == len(
        fake_menu_options
    )


def test_add_tasks(test_logic):
    assert test_logic.add_tasks("q") == "q"
    assert test_logic.add_tasks("Task 1") is None
    assert test_logic.add_tasks("") is None
    assert test_logic.add_tasks("New Task") == "New Task"


def test_remove_tasks(test_logic, fake_tasks):
    assert test_logic.remove_tasks("q") == "q"
    assert test_logic.remove_tasks("d") == "d"
    assert test_logic.remove_tasks("v") == "v"
    assert test_logic.remove_tasks("abc") is None
    assert test_logic.remove_tasks(str(len(fake_tasks) + 1)) is None
    assert test_logic.remove_tasks(str(len(fake_tasks))) == len(fake_tasks)


def test_edit_tasks(test_logic, fake_tasks):
    assert test_logic.edit_tasks("q") == "q"
    assert test_logic.edit_tasks("v") == "v"
    assert test_logic.edit_tasks("abc") is None
    assert test_logic.remove_tasks(str(len(fake_tasks) + 1)) is None
    assert test_logic.remove_tasks(str(len(fake_tasks))) == len(fake_tasks)


def test_update_task(test_logic):
    assert test_logic.updated_task("Task 1") is None
    assert test_logic.updated_task("") is None
    assert test_logic.updated_task("Updated Task") == "Updated Task"

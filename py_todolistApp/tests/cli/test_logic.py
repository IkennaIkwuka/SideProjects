import pytest
from py_todolistApp.src.cli.logic import AppLogic, TaskStatus

# ------------------
# Fixtures
# ------------------


@pytest.fixture
def test_logic(tasks):
    return AppLogic(tasks)


@pytest.fixture
def tasks():
    return ["Task 1", "Task 2", "Task 3"]


@pytest.fixture
def app_menu():
    return ("save", "view", "add", "remove")


# -------------------
# Tests
# -------------------


def test_run(test_logic, app_menu):
    assert test_logic.run("q", app_menu) == TaskStatus.QUIT
    assert test_logic.run(str(len(app_menu) + 1), app_menu) == TaskStatus.OUT_OF_RANGE
    assert test_logic.run(str(len(app_menu)), app_menu) == len(app_menu)


def test_run_invalid(test_logic, app_menu):
    assert test_logic.run("abc", app_menu) == TaskStatus.INVALID
    assert test_logic.run("", app_menu) == TaskStatus.INVALID


def test_add_tasks(test_logic):
    assert test_logic.add_tasks("q") == TaskStatus.QUIT
    assert test_logic.add_tasks("Task 1") == TaskStatus.EXISTS
    assert test_logic.add_tasks("New Task") == "New Task"


def test_add_tasks_invalid(test_logic):
    assert test_logic.add_tasks("") == TaskStatus.INVALID


def test_remove_tasks(test_logic, tasks):
    assert test_logic.remove_tasks("q") == TaskStatus.QUIT
    assert test_logic.remove_tasks("d") == TaskStatus.DELETE_ALL
    assert test_logic.remove_tasks("v") == TaskStatus.VIEW
    assert test_logic.remove_tasks(str(len(tasks) + 1)) == TaskStatus.OUT_OF_RANGE
    assert test_logic.remove_tasks(str(len(tasks))) == len(tasks)


def test_remove_tasks_invalid(test_logic):
    assert test_logic.remove_tasks("abc") == TaskStatus.INVALID


def test_delete_all_confirmation(test_logic):
    assert test_logic.delete_all_confirmation("y") is True
    assert test_logic.delete_all_confirmation("n") is False


def test_delete_all_confirmation_invalid(test_logic):
    assert test_logic.delete_all_confirmation("other") == TaskStatus.INVALID
    assert test_logic.delete_all_confirmation("3") == TaskStatus.INVALID


def test_edit_tasks(test_logic, tasks):
    assert test_logic.edit_tasks("q") == TaskStatus.QUIT
    assert test_logic.edit_tasks("v") == TaskStatus.VIEW
    assert test_logic.remove_tasks(str(len(tasks) + 1)) == TaskStatus.OUT_OF_RANGE
    assert test_logic.remove_tasks(str(len(tasks))) == len(tasks)


def test_edit_tasks_invalid(test_logic):
    assert test_logic.edit_tasks("abc") == TaskStatus.INVALID


def test_update_task(test_logic):
    assert test_logic.updated_task("Task 1") == TaskStatus.EXISTS
    assert test_logic.updated_task("Updated Task") == "Updated Task"


def test_update_task_invalid(test_logic):
    assert test_logic.updated_task("") == TaskStatus.INVALID


def test_get_messages(test_logic):
    assert test_logic.get_message(TaskStatus.OUT_OF_RANGE) == "Out of range."
    assert test_logic.get_message(TaskStatus.INVALID) == "Invalid input."
    assert test_logic.get_message(TaskStatus.EXISTS) == "Task exists."


def test_get_messages_invalid(test_logic):
    assert test_logic.get_message(None) == ""
    assert test_logic.get_message("abc") == ""
    assert test_logic.get_message(3) == ""

import pytest
from src.cli.io import TodoIO


@pytest.fixture
def io(tmp_path):
    f = tmp_path / "io_test.txt"
    return TodoIO(f)


@pytest.mark.parametrize("task_name", ["Task A", "Task B", "12345"])
def test_store_task_parametrized(io, task_name):
    io.store_task(task_name)
    assert task_name in io.get_tasks()


@pytest.mark.parametrize(
    "index, expected_count",
    [
        (1, 0),  # Valid index for a list of 1
        (0, 1),  # Invalid (too low)
        (2, 1),  # Invalid (too high)
        (-1, 1),  # Invalid
    ],
)
def test_delete_task_boundaries(io, index, expected_count):
    io.store_task("Sample")
    io.delete_task(index)
    assert len(io.get_tasks()) == expected_count


def test_edit_task_content_duplicate_prevention(io, capsys):
    io.store_task("Apple")
    io.store_task("Banana")

    # Try to edit "Banana" (index 2) to "Apple"
    io.edit_task_content(2, "Apple")

    captured = capsys.readouterr()
    assert "Error: Task already exist." in captured.out
    assert io.get_tasks()[1] == "Banana"  # Should not have changed

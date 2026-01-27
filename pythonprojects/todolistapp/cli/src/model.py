import sqlite3
from pathlib import Path


class TodoModel:
    def __init__(self, db_file: str | Path):
        self.db_file = Path(db_file)
        self.db_file.parent.mkdir(parents=True, exist_ok=True)

        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT UNIQUE NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self.conn.commit()

    def get_tasks(self, include_completed=True):
        if include_completed:
            cursor = self.conn.execute(
                "SELECT content, completed FROM tasks ORDER BY id"
            )
        else:
            cursor = self.conn.execute(
                "SELECT content, completed FROM tasks WHERE completed = 0 ORDER BY id"
            )

        return [(row["content"], bool(row["completed"])) for row in cursor.fetchall()]

    def store_task(self, task: str):
        try:
            self.conn.execute(
                "INSERT INTO tasks (content) VALUES (?)",
                (task,),
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError("Task already exists.")

    def toggle_complete(self, index: int):
        task_id = self._index_to_id(index)
        self.conn.execute(
            """
            UPDATE tasks
            SET completed = NOT completed
            WHERE id = ?
            """,
            (task_id,),
        )
        self.conn.commit()

    def delete_task(self, index: int):
        task_id = self._index_to_id(index)
        self.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def edit_task_content(self, index: int, new_task: str):
        task_id = self._index_to_id(index)
        self.conn.execute(
            "UPDATE tasks SET content = ? WHERE id = ?",
            (new_task, task_id),
        )
        self.conn.commit()

    def clear_all(self):
        self.conn.execute("DELETE FROM tasks")
        self.conn.commit()

    def _index_to_id(self, index: int) -> int:
        cursor = self.conn.execute("SELECT id FROM tasks ORDER BY id")
        rows = cursor.fetchall()
        return rows[index - 1]["id"]


if __name__ == "__main__":
    ...

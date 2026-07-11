import sqlite3
from pathlib import Path
from datetime import date


class TodoModel:
    PRIORITIES = ("LOW", "MEDIUM", "HIGH")

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
                completed INTEGER NOT NULL DEFAULT 0,
                priority TEXT NOT NULL DEFAULT 'MEDIUM',
                due_date TEXT
            )
            """
        )
        self.conn.commit()

    # ---------- CRUD ---------- #

    def get_tasks(self):
        cursor = self.conn.execute(
            """
            SELECT content, completed, priority, due_date
            FROM tasks
            ORDER BY
                completed ASC,
                CASE priority
                    WHEN 'HIGH' THEN 1
                    WHEN 'MEDIUM' THEN 2
                    WHEN 'LOW' THEN 3
                END,
                due_date IS NULL,
                due_date
            """
        )
        return [
            (
                row["content"],
                bool(row["completed"]),
                row["priority"],
                row["due_date"],
            )
            for row in cursor.fetchall()
        ]

    def store_task(self, task: str, priority="MEDIUM", due_date=None):
        self.conn.execute(
            """
            INSERT INTO tasks (content, priority, due_date)
            VALUES (?, ?, ?)
            """,
            (task, priority, due_date),
        )
        self.conn.commit()

    def toggle_complete(self, index: int):
        task_id = self._index_to_id(index)
        self.conn.execute(
            "UPDATE tasks SET completed = NOT completed WHERE id = ?",
            (task_id,),
        )
        self.conn.commit()

    def update_task(self, index: int, content=None, priority=None, due_date=None):
        task_id = self._index_to_id(index)

        if content is not None:
            self.conn.execute(
                "UPDATE tasks SET content = ? WHERE id = ?",
                (content, task_id),
            )
        if priority is not None:
            self.conn.execute(
                "UPDATE tasks SET priority = ? WHERE id = ?",
                (priority, task_id),
            )
        if due_date is not None:
            self.conn.execute(
                "UPDATE tasks SET due_date = ? WHERE id = ?",
                (due_date, task_id),
            )

        self.conn.commit()

    def delete_task(self, index: int):
        task_id = self._index_to_id(index)
        self.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def clear_all(self):
        self.conn.execute("DELETE FROM tasks")
        self.conn.commit()

    # ---------- helpers ---------- #

    def _index_to_id(self, index: int) -> int:
        cursor = self.conn.execute("SELECT id FROM tasks ORDER BY id")
        rows = cursor.fetchall()
        return rows[index - 1]["id"]

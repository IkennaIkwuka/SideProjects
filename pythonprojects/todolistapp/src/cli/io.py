from pathlib import Path


class TodoIO:
    def __init__(self, file: Path | str):
        self.file = Path(file)
        self.tasks = self.read()

    def read(self):
        if self.file.exists():
            return [line.strip() for line in self.file.read_text().splitlines()]
        return []

    def save(self):
        self.file.write_text("\n".join(self.tasks))

    def is_tasks(self):
        return True if self.tasks else False

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def store_task(self, task: str):
        if task and task not in self.tasks:
            self.tasks.append(task)
            print("\nTask created.")
        else:
            print("\nError: task exists.\n")

    def clear_all(self):
        try:
            self.tasks.clear()
            return True
        except Exception as e:
            print(f"Error at {e}")
            return False

    def delete_task(self, index: int):
        if index > 0 and index <= len(self.tasks):
            self.tasks.pop(index - 1)
            print("\nTask deleted.")
        else:
            print("Error: not a task.")

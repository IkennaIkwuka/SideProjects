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

    def display_tasks(self):
        if not self.tasks:
            return False
        else:
            print("\nViewing tasks list...\n")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        return True

    def task_stored(self, task: str):
        if task and task not in self.tasks:
            self.tasks.append(task)
            print("\nTask created.")
        else:
            print("\nError: task exists.\n")

from pathlib import Path


class TodoIO:
    def __init__(self, file: str | Path):
        self.file = Path(file)
        self.tasks = self.read()

    def read(self):
        return [line.strip() for line in self.file.read_text().splitlines()]

    def save(self):
        self.file.write_text("\n".join(self.tasks))

    def get_tasks(self):
        return self.tasks

    def display_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def store_task(self, task: str):
        self.tasks.append(task)
        print("\nTask created.")
        self.save()

    def clear_all(self):
        self.tasks.clear()
        print("\nAll tasks have been deleted.")
        self.save()

    def delete_task(self, index: int):
        self.tasks.pop(index - 1)
        print("\nTask deleted.")
        self.save()

    def edit_task_content(self, index: int, new_task: str):
        self.tasks[index - 1] = new_task
        print("\nTask updated.")
        self.save()

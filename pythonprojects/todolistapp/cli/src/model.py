from pathlib import Path


class TodoModel:
    def __init__(self, file: str | Path):
        self.file = Path(file)
        self.tasks = self.read()

    def read(self):
        return [line.strip() for line in self.file.read_text().splitlines()]

    def save(self):
        self.file.write_text("\n".join(self.tasks))

    def get_tasks(self):
        return self.tasks   

    def store_task(self, task: str):
        self.tasks.append(task)
        self.save()

    def clear_all(self):
        self.tasks.clear()
        self.save()

    def delete_task(self, index: int):
        self.tasks.pop(index - 1)
        self.save()

    def edit_task_content(self, index: int, new_task: str):
        self.tasks[index - 1] = new_task
        self.save()

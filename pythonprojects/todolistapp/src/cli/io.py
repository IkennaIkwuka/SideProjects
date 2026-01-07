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

    def get_tasks(self):
        return self.tasks

    def display_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def __does_task_exist(self, task: str):
        if task in self.tasks:
            print("Error: Task already exist.")
            return True
        else:
            return False

    def store_task(self, task: str):
        if task and not self.__does_task_exist(task):
            self.tasks.append(task)
            print("\nTask created.")

    def clear_all(self):
        try:
            self.tasks.clear()
            return True
        except Exception as e:
            print(f"Error at {e}")
            return False

    def __is_task_index_valid(self, index: int):
        if index > 0 and index <= len(self.tasks):
            return True
        else:
            print("Error: Invalid task index.")
            return False

    def delete_task(self, index: int):
        if self.__is_task_index_valid(index):
            self.tasks.pop(index - 1)
            print("\nTask deleted.")

    def edit_task_content(self, index: int, new_task: str):
        if self.__is_task_index_valid(index) and not self.__does_task_exist(new_task):
            self.tasks[index - 1] = new_task
            print("\nTask updated.")

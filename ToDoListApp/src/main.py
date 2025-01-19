import os 
os.makedirs("/docs/Tasks.txt",exist_ok=True)
# Steps

# class of todolistapp
class Todolistapp:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    # method to read file for tasks
    # append to list or set?
    def load_tasks(self) -> list[str]:
        file_list = []
        duplicates = set()
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                _ = file.readlines()
                for task in _:
                    task = task.strip()
                    if task in duplicates:
                        print(f"Duplicate: {task}")
                    if not isinstance(task, str):
                        print("Not string")
                        task = str(task)
                    duplicates.add(task)
                    file_list.append(task)
        except FileNotFoundError:
            file_list.extend([])

        return file_list

    # method to add tasks to tasks list
    # add till a certain limit
    # validate for no duplicates (use sets)
    def add_tasks(self, tasks_list: list, task: str):
        if len(tasks_list) > 10:
            print("Task list is full.")
            return
        if task in tasks_list:
            print(f"Task: {task} already exists.")
        tasks_list.append(task)

    # method to remove tasks from list/file
    # employ use of indexes
    def remove_task(self, tasks_list: list, index: int):
        if not tasks_list:
            print(f"Cannot remove task at index {index} as there are no tasks.")
            return
        try:
            tasks_list.pop(index)
            print(f"'{tasks_list[index]}' has been removed at index {index}.")
        except IndexError:
            print("No such task exist at that index.")
            raise

    # method to update tasks in file
    # employ use of indexes
    def update_tasks(self, tasks_list: list, index: int, task: str):
        if not tasks_list:
            print("Cannot update task as there are no tasks.")
            return
        try:
            tasks_list.pop(index)
            tasks_list.insert(index, task)
            print(
                f"'{tasks_list[index]}' has been updated successfully at index {index}."
            )
        except IndexError:
            print("No such task exist at that index.")
            raise

    # method to save tasks
    def save_tasks(self, tasks_list: list):
        if not tasks_list:
            print("Cannot save tasks as there are no tasks.")
            return
        try:
            with open(f"{self.file_name}.txt", "a") as file:
                file.writelines(tasks_list)
        except FileNotFoundError:
            print(f"{self.file_name}.txt does not exist")
            with open(f"{self.file_name}.txt", "x") as file:
                file.writelines([])


# main method to run program
# display index, tasks .. in tasks list
def main():
    app = Todolistapp("docs/Tasks")

    tasks = app.load_tasks()

    print("\nToDoList App\n")
    while True:
        for idx, tsk in enumerate(tasks):
            if not tasks:
                print("No tasks")
                break
            print(f"id: {idx} Task: {tsk}")
        user_input = input("What do you want to do? (add, remove, update, quit): ")
        if user_input not in ["add", "remove", "update", "quit"]:
            print(f"'{user_input}' is an invalid input")
            continue
        break
    while True:
        match user_input:
            case "add":
                add = input("Provide a task you would like to add (q to quit): ")
                if add == "q":
                    break
                app.add_tasks(tasks, add)
                app.save_tasks(tasks)
            case "remove":
                while True:
                    remove = input(
                        "Give the 'id' of the task you would like to remove(q to quit)"
                    )
                    if remove == "q":
                        break

                    if not isinstance(remove, int):
                        print("Invalid. Please provide a valid 'id' (a number).")
                        continue
                    remove = int(remove)
                    app.remove_task(tasks, remove)
            case "update":
                while True:
                    update_id = input(
                        "Give the 'id' of the task you would like to update(q to quit)"
                    )
                    if update_id == "q":
                        break

                    if not isinstance(update_id, int):
                        print("Invalid. Please provide a valid 'id' (a number).")
                        continue
                    update_id = int(update_id)
                    update_task = input("Provide the updated task.(q to quit)")
                    if update_task == "q":
                        break

                    app.update_tasks(tasks, update_id, update_task)
            case "quit":
                print("Quitting program")
                app.save_tasks(tasks)
                break


if __name__ == "__main__":
    main()

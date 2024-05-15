class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def show_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

todo_list = TodoList()

while True:
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.add_task(task)
    elif choice == '2':
        index = int(input("Enter index of task to delete: ")) - 1
        todo_list.delete_task(index)
    elif choice == '3':
        print("\nTasks:")
        todo_list.show_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

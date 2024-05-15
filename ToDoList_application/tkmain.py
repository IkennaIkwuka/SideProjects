import tkinter as tk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.task_listbox.delete(index)
            del self.tasks[index]

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoListApp(root)
    root.mainloop()

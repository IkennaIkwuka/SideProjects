from main import ToDoListApp

class Circle(ToDoListApp):
    def __init__(self, task_file):
        super().__init__(task_file)
        
    def run(self):
        print("hi")
        
app = Circle("book")
app.run()
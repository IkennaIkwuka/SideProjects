from rich import box
from rich.console import Console
from rich.table import Table


class TodoView:
    def __init__(self):
        self.console = Console()

    def menu(self):
        self.console.print(
            "\nToDo App ([bold magenta]'q'[/bold magenta] Quit)\n",
            style="bold cyan",
        )
        self.console.print(
            "1. Create task\n2. View tasks\n3. Remove task\n4. Edit task\n",
            style="white",
        )

    def warning(self, msg: str):
        self.console.print(f"\n{msg}\n", style="bold blue")

    def error(self, msg: str):
        self.console.print(f"\n{msg}\n", style="red")

    def success(self, msg: str):
        self.console.print(f"\n{msg}\n", style="green")

    def show_tasks(self, tasks: list[tuple[str, bool]]):
        if not tasks:
            self.warning("No tasks available.")
            return

        table = Table(title="Current Tasks", box=box.SIMPLE)
        table.add_column("#", justify="right", style="yellow")
        table.add_column("Status", justify="center")
        table.add_column("Task Description", style="cyan")

        for i, (task, completed) in enumerate(tasks, start=1):
            status = "[green]✓[/green]" if completed else "[red]•[/red]"
            table.add_row(str(i), status, task)

        self.console.print(table)

    def action(self, msg: str):
        self.console.print(f"\n{msg}\n", style="magenta")

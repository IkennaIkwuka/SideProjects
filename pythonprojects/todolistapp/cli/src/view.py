from rich.console import Console
from rich.table import Table


class TodoView:
    def __init__(self):
        self.console = Console()

    def menu(self):
        self.console.print(
            "\n[bold cyan]ToDo App ([bold magenta]'q'[/bold magenta] Quit) [/bold cyan]\n"
            "1. Create task\n2. View tasks\n3. Remove task\n4. Edit task\n"
        )

    def warning(self, msg: str):
        self.console.print(f"[bold blue]{msg}[/bold blue]")

    def error(self, msg: str):
        self.console.print(f"[red]{msg}[/red]")

    def success(self, msg: str):
        self.console.print(f"[green]{msg}[/green]")

    def show_tasks(self, tasks: list[str]):
        table = Table(title="Tasks")
        table.add_column("#", justify="right")
        table.add_column("Task", justify="left")

        for i, task in enumerate(tasks, start=1):
            table.add_row(str(i), task)

        self.console.print(table)

from rich.console import Console
from rich.table import Table

console = Console()

def print_projects(projects):
    if not projects:
        console.print("[yellow]No projects found.[/yellow]")
        return
    table = Table(title="Projects")
    table.add_column("Title", style="cyan")
    table.add_column("Description")
    table.add_column("Due Date")
    for p in projects:
        table.add_row(p.title, p.description, p.due_date)
    console.print(table)

def print_tasks(tasks):
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return
    table = Table(title="Tasks")
    table.add_column("Title", style="cyan")
    table.add_column("Status")
    table.add_column("Assigned To")
    for t in tasks:
        table.add_row(t.title, t.status, t.assigned_to)
    console.print(table)

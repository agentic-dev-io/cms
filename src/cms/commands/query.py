import typer
from rich import print as rprint
from rich.table import Table
from rich.console import Console

from cms.db import get_connection
from cms.main import app

console = Console()


@app.command()
def query(sql: str = typer.Argument(..., help="SQL query to execute")):
    """Execute a SQL query against the content database."""
    con = get_connection()
    try:
        result = con.execute(sql)
        columns = [desc[0] for desc in result.description]
        rows = result.fetchall()

        if not rows:
            rprint("[yellow]No results.[/yellow]")
            return

        table = Table(show_header=True)
        for col in columns:
            table.add_column(col)
        for row in rows:
            table.add_row(*[str(v) for v in row])

        console.print(table)
        rprint(f"[dim]{len(rows)} row(s)[/dim]")
    except Exception as e:
        rprint(f"[red]Error: {e}[/red]")
    finally:
        con.close()

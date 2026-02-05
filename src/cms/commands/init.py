import typer
from rich import print as rprint

from cms.db import SCHEMA_PATH, get_connection
from cms.main import app


@app.command()
def init():
    """Initialize the DuckDB database with the CMS schema."""
    con = get_connection()
    sql = SCHEMA_PATH.read_text(encoding="utf-8")
    con.execute(sql)
    con.close()
    rprint("[green]Database initialized with schema.[/green]")

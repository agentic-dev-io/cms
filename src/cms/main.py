import typer

app = typer.Typer(name="cms", help="DuckDB-based CMS for synapticore web properties")


@app.callback()
def callback():
    pass


from cms.commands import init, seed, export, query  # noqa: E402, F401

if __name__ == "__main__":
    app()

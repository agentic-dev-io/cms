import json
from pathlib import Path

import typer
from rich import print as rprint

from cms.db import DATA_DIR, get_connection
from cms.main import app


def _write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _rows_to_dicts(con, sql, params=None):
    result = con.execute(sql, params or [])
    columns = [desc[0] for desc in result.description]
    return [dict(zip(columns, row)) for row in result.fetchall()]


def _parse_json_fields(row: dict, fields: list[str]) -> dict:
    for field in fields:
        if field in row and isinstance(row[field], str):
            try:
                row[field] = json.loads(row[field])
            except (json.JSONDecodeError, TypeError):
                pass
    return row


def _export_ecosystem(con):
    rows = _rows_to_dicts(con, "SELECT * FROM ecosystem_orgs ORDER BY sort_order")
    _write_json(DATA_DIR / "shared" / "ecosystem.json", rows)
    rprint("[green]  shared/ecosystem.json[/green]")


def _export_agentic_dev(con):
    site_id = "agentic-dev"
    out = DATA_DIR / site_id

    # hero
    heroes = _rows_to_dicts(con, "SELECT * FROM hero_sections WHERE site_id = ?", [site_id])
    if heroes:
        hero = _parse_json_fields(heroes[0], ["features"])
        _write_json(out / "hero.json", hero)
        rprint("[green]  agentic-dev/hero.json[/green]")

    # problems
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, description, icon FROM content_blocks WHERE site_id = ? AND block_type = 'problem' ORDER BY sort_order",
        [site_id],
    )
    _write_json(out / "problems.json", rows)
    rprint("[green]  agentic-dev/problems.json[/green]")

    # solutions
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, description, icon FROM content_blocks WHERE site_id = ? AND block_type = 'solution' ORDER BY sort_order",
        [site_id],
    )
    _write_json(out / "solutions.json", rows)
    rprint("[green]  agentic-dev/solutions.json[/green]")

    # stack
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, description FROM content_blocks WHERE site_id = ? AND block_type = 'stack' ORDER BY sort_order",
        [site_id],
    )
    _write_json(out / "stack.json", rows)
    rprint("[green]  agentic-dev/stack.json[/green]")

    # services
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, description, icon, features, metadata FROM content_blocks WHERE site_id = ? AND block_type = 'service' ORDER BY sort_order",
        [site_id],
    )
    for r in rows:
        _parse_json_fields(r, ["features", "metadata"])
    _write_json(out / "services.json", rows)
    rprint("[green]  agentic-dev/services.json[/green]")

    # comparison
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, features, metadata FROM content_blocks WHERE site_id = ? AND block_type = 'comparison' ORDER BY sort_order",
        [site_id],
    )
    for r in rows:
        _parse_json_fields(r, ["features", "metadata"])
    _write_json(out / "comparison.json", rows)
    rprint("[green]  agentic-dev/comparison.json[/green]")

    # about
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, metadata FROM content_blocks WHERE site_id = ? AND block_type = 'about' ORDER BY sort_order",
        [site_id],
    )
    if rows:
        about = _parse_json_fields(rows[0], ["metadata"])
        _write_json(out / "about.json", about)
        rprint("[green]  agentic-dev/about.json[/green]")


def _export_synapticore_io(con):
    site_id = "synapticore-io"
    out = DATA_DIR / site_id

    # hero
    heroes = _rows_to_dicts(con, "SELECT * FROM hero_sections WHERE site_id = ?", [site_id])
    if heroes:
        hero = _parse_json_fields(heroes[0], ["features"])
        _write_json(out / "hero.json", hero)
        rprint("[green]  synapticore-io/hero.json[/green]")

    # modes
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, description, icon FROM content_blocks WHERE site_id = ? AND block_type = 'mode' ORDER BY sort_order",
        [site_id],
    )
    _write_json(out / "modes.json", rows)
    rprint("[green]  synapticore-io/modes.json[/green]")

    # stats
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, description, metadata FROM content_blocks WHERE site_id = ? AND block_type = 'stats' ORDER BY sort_order",
        [site_id],
    )
    if rows:
        stats = _parse_json_fields(rows[0], ["metadata"])
        _write_json(out / "stats.json", stats)
        rprint("[green]  synapticore-io/stats.json[/green]")


def _export_synapticore_studio(con):
    site_id = "synapticore-studio"
    out = DATA_DIR / site_id

    # hero
    heroes = _rows_to_dicts(con, "SELECT * FROM hero_sections WHERE site_id = ?", [site_id])
    if heroes:
        hero = _parse_json_fields(heroes[0], ["features"])
        _write_json(out / "hero.json", hero)
        rprint("[green]  synapticore-studio/hero.json[/green]")

    # capabilities
    rows = _rows_to_dicts(
        con,
        "SELECT block_id, title, description, icon FROM content_blocks WHERE site_id = ? AND block_type = 'capability' ORDER BY sort_order",
        [site_id],
    )
    _write_json(out / "capabilities.json", rows)
    rprint("[green]  synapticore-studio/capabilities.json[/green]")

    # case studies
    rows = _rows_to_dicts(
        con,
        "SELECT * FROM case_studies WHERE site_id = ? ORDER BY sort_order",
        [site_id],
    )
    for r in rows:
        _parse_json_fields(r, ["tags", "stats"])
    _write_json(out / "case-studies.json", rows)
    rprint("[green]  synapticore-studio/case-studies.json[/green]")

    # timeline
    rows = _rows_to_dicts(
        con,
        "SELECT * FROM timeline_events WHERE site_id = ? ORDER BY sort_order",
        [site_id],
    )
    _write_json(out / "timeline.json", rows)
    rprint("[green]  synapticore-studio/timeline.json[/green]")


@app.command(name="export")
def export_cmd(
    site: str = typer.Option(None, help="Export only this site (agentic-dev, synapticore-io, synapticore-studio)"),
    all_sites: bool = typer.Option(False, "--all", help="Export all sites"),
):
    """Export content from DuckDB to JSON files."""
    if not site and not all_sites:
        rprint("[red]Specify --all or --site <name>[/red]")
        raise typer.Exit(1)

    con = get_connection()

    if all_sites or site == "shared":
        _export_ecosystem(con)

    if all_sites or site == "agentic-dev":
        _export_agentic_dev(con)

    if all_sites or site == "synapticore-io":
        _export_synapticore_io(con)

    if all_sites or site == "synapticore-studio":
        _export_synapticore_studio(con)

    con.close()
    rprint("[bold green]Export complete.[/bold green]")

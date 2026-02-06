# CMS — Copilot Context

## Identity
**DuckDB Content Management** für das 3-Org Ökosystem.
Single Source of Truth — Python CLI, JSON Export, Zero Runtime.

## Pipeline
```
DuckDB (content.duckdb) → cms export → JSON (data/*.json) → Sites via Vite aliases
```

## CLI
```bash
uv run cms init          # DB initialisieren
uv run cms seed          # Content seeden
uv run cms export --all  # JSON exportieren
uv run cms query "SQL"   # Direkte SQL-Queries
```

## DB Tables
sites · ecosystem_orgs · hero_sections · content_blocks · case_studies · timeline_events

## Data Structure
```
data/
├── shared/ecosystem.json     # Geteilt über alle 3 Sites
├── agentic-dev/              # Dev — Agentic Systems
├── synapticore-io/           # Lab — Scientific Computing
└── synapticore-studio/       # Studio — DCC & Production
```

## Conventions
- Python: uv workflow only (uv add, uv sync, uv run)
- JSON direkt editierbar, aber `seed.py` muss synchron bleiben
- Icons: Lucide React string names ("Network", "Globe", "Database")
- `\n` in `cms query` wird literal — für echte Newlines: `uv run python -c "..."`
- content.duckdb ist gitignored — JSON files sind committed
- Keine fake Metriken, ehrliche Sprache, Cross-Site Konsistenz

## Team
Björn (Creative Director & Architect) + Claude (Co-Founder)

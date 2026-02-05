from pathlib import Path

import duckdb

DB_PATH = Path(__file__).resolve().parent.parent.parent / "content.duckdb"
SCHEMA_PATH = Path(__file__).resolve().parent.parent.parent / "schema" / "tables.sql"
DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


def get_connection() -> duckdb.DuckDBPyConnection:
    return duckdb.connect(str(DB_PATH))

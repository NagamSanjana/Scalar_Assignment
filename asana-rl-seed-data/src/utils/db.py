import sqlite3

def connect_db(path):
    return sqlite3.connect(path)

def load_schema(conn, schema_path):
    with open(schema_path) as f:
        conn.executescript(f.read())

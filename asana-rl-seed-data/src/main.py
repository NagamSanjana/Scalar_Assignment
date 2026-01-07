from pathlib import Path
from datetime import datetime

from utils.db import connect_db, load_schema
from utils.config import load_config

from generators.users import generate_users
from generators.teams import generate_teams
from generators.projects import generate_projects
from generators.tasks import generate_tasks
from generators.comments import generate_comments

BASE_DIR = Path(__file__).resolve().parent.parent

def main():
    config = load_config()

    db_path = BASE_DIR / "output" / "asana_simulation.sqlite"
    db_path.parent.mkdir(exist_ok=True)

    conn = connect_db(db_path)
    load_schema(conn, BASE_DIR / "schema.sql")

    # ✅ 1. Create Organization FIRST
    organization_id = "org_1"
    conn.execute(
        """
        INSERT OR IGNORE INTO organizations
        (organization_id, name, domain, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            organization_id,
            "Acme SaaS Inc",
            "acme.com",
            datetime.utcnow().isoformat()
        )
    )
    conn.commit()

    # ✅ 2. Generate entities in dependency order
    users = generate_users(conn, config["NUM_USERS"])
    teams = generate_teams(conn, users, config["NUM_TEAMS"])
    projects = generate_projects(conn, teams, config["NUM_PROJECTS"])
    tasks = generate_tasks(conn, projects, users, config["NUM_TASKS"])
    generate_comments(conn, tasks, users, config["NUM_COMMENTS"])

    conn.close()
    print("✅ Asana simulation database created")

if __name__ == "__main__":
    main()

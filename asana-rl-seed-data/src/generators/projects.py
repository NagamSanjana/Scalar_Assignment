import uuid
import random
from datetime import datetime, timezone
from faker import Faker

fake = Faker()

PROJECT_TYPES = [
    "Product Development",
    "Sprint",
    "Bug Tracking",
    "Marketing Campaign",
    "Customer Onboarding",
    "Internal Operations"
]

def generate_projects(conn, teams, n):
    projects = []

    for i in range(n):
        project_id = str(uuid.uuid4())
        team_id = random.choice(teams)
        name = fake.bs().capitalize()
        project_type = random.choice(PROJECT_TYPES)
        created_at = datetime.now(timezone.utc).isoformat()

        conn.execute(
            """
            INSERT INTO projects (
                project_id,
                team_id,
                name,
                project_type,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                project_id,
                team_id,
                name,
                project_type,
                created_at
            )
        )

        projects.append(project_id)

    conn.commit()
    return projects

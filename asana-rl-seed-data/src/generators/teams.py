import uuid
import random
from datetime import datetime, timezone
from faker import Faker

fake = Faker()

TEAM_FUNCTIONS = [
    "Engineering",
    "Product",
    "Marketing",
    "Sales",
    "Customer Success",
    "Operations",
    "Data"
]

def generate_teams(conn, users, n):
    teams = []
    organization_id = "org_1"

    for i in range(n):
        team_id = str(uuid.uuid4())
        name = f"{fake.word().capitalize()} Team"
        function = random.choice(TEAM_FUNCTIONS)
        created_at = datetime.now(timezone.utc).isoformat()

        # ✅ Insert team (matches schema exactly)
        conn.execute(
            """
            INSERT INTO teams (
                team_id,
                organization_id,
                name,
                function,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                team_id,
                organization_id,
                name,
                function,
                created_at
            )
        )

        teams.append(team_id)

        # ✅ Team memberships (many-to-many)
        members = random.sample(users, k=min(10, len(users)))
        for user_id in members:
            conn.execute(
                """
                INSERT OR IGNORE INTO team_memberships
                (team_id, user_id)
                VALUES (?, ?)
                """,
                (team_id, user_id)
            )

    conn.commit()
    return teams

import uuid
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_users(conn, n):
    users = []
    organization_id = "org_1"  # must exist in organizations table

    for _ in range(n):
        user_id = str(uuid.uuid4())
        full_name = fake.name()
        email = full_name.lower().replace(" ", ".") + "@example.com"
        role = fake.job()
        is_active = True
        created_at = datetime.utcnow().isoformat()

        conn.execute(
            """
            INSERT INTO users (
                user_id,
                organization_id,
                full_name,
                email,
                role,
                is_active,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                organization_id,
                full_name,
                email,
                role,
                is_active,
                created_at
            )
        )

        users.append(user_id)

    conn.commit()
    return users

import uuid
import random
from datetime import datetime, timezone
from faker import Faker

fake = Faker()

def generate_comments(conn, tasks, users, n):
    for _ in range(n):
        comment_id = str(uuid.uuid4())
        task_id = random.choice(tasks)
        user_id = random.choice(users)
        content = fake.sentence(nb_words=12)
        created_at = datetime.now(timezone.utc).isoformat()

        conn.execute(
            """
            INSERT INTO comments (
                comment_id,
                task_id,
                user_id,
                content,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                comment_id,
                task_id,
                user_id,
                content,
                created_at
            )
        )

    conn.commit()

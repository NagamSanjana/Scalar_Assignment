import uuid
import random
from datetime import datetime, timedelta, timezone

def generate_tasks(conn, projects, users, n):
    task_ids = []

    for i in range(n):
        task_id = str(uuid.uuid4())
        project_id = random.choice(projects)

        section_id = None            # sections not modeled yet
        parent_task_id = None        # no subtasks for now

        name = f"Task {i + 1}"
        completed = random.choice([0, 1])

        created_at = (
            datetime.now(timezone.utc)
            - timedelta(days=random.randint(1, 90))
        ).isoformat()

        completed_at = None
        if completed:
            completed_at = (
                datetime.fromisoformat(created_at)
                + timedelta(days=random.randint(1, 14))
            ).isoformat()

        conn.execute(
            """
            INSERT INTO tasks (
                task_id,
                project_id,
                section_id,
                parent_task_id,
                name,
                completed,
                created_at,
                completed_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                task_id,
                project_id,
                section_id,
                parent_task_id,
                name,
                completed,
                created_at,
                completed_at
            )
        )

        task_ids.append(task_id)

    conn.commit()
    return task_ids

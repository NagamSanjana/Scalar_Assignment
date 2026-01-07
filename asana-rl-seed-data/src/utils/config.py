import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    return {
        "NUM_USERS": int(os.getenv("NUM_USERS", 100)),
        "NUM_TEAMS": int(os.getenv("NUM_TEAMS", 5)),
        "NUM_PROJECTS": int(os.getenv("NUM_PROJECTS", 10)),
        "NUM_TASKS": int(os.getenv("NUM_TASKS", 200)),
        "NUM_COMMENTS": int(os.getenv("NUM_COMMENTS", 300)),
    }

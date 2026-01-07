# Scalar_Assignment
# 📌 Asana RL Seed Data Simulation

This project generates a **realistic SQLite database** that simulates core functionality of **Asana-style project management systems**, intended for **reinforcement learning, analytics, and system design experiments**.

The database includes **organizations, teams, users, projects, sections, tasks, and comments** with realistic relationships and timestamps.

---

## 📂 Project Structure

asana-rl-seed-data/
├── README.md
|
├── requirements.txt
|
├── schema.sql
|
├── .env.example
|
├── src/
|
│   ├── main.py
|
│   ├── generators/
|   |   |
│   │   ├── users.py
|   |   |
│   │   ├── teams.py
|   |   |
│   │   ├── projects.py
|   |   |
│   │   ├── tasks.py
|   |   |
│   │   └── comments.py
|   |    
│   ├── utils/
|   |   |
│   │   ├── db.py
|   |   |
│   │   └── config.py
|   |  
│   └── models/
| 
├── prompts/
|   |
│   └── task_prompts.txt
|  
└── output/
    |
    └── asana_simulation.sqlite




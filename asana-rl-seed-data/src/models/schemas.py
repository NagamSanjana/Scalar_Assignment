"""
schemas.py

Logical data models for the Asana workspace simulation.

These classes are NOT full ORM models.
They serve as:
- Documentation of core entities
- A reference layer between database schema and generators
- An extension point for future ORM integration if needed
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    user_id: str
    name: str
    email: str


@dataclass
class Team:
    team_id: str
    name: str


@dataclass
class Project:
    project_id: str
    name: str
    team_id: str


@dataclass
class Task:
    task_id: str
    name: str
    project_id: str
    assignee_id: Optional[str]
    created_at: str
    completed: bool
    parent_task_id: Optional[str] = None


@dataclass
class Comment:
    comment_id: str
    task_id: str
    author_id: str
    body: str
    created_at: str

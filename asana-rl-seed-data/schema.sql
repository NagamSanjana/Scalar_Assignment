PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS organizations (
  organization_id TEXT PRIMARY KEY,
  name TEXT,
  domain TEXT,
  created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS teams (
  team_id TEXT PRIMARY KEY,
  organization_id TEXT,
  name TEXT,
  function TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

CREATE TABLE IF NOT EXISTS users (
  user_id TEXT PRIMARY KEY,
  organization_id TEXT,
  full_name TEXT,
  email TEXT,
  role TEXT,
  is_active BOOLEAN,
  created_at TIMESTAMP,
  FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

CREATE TABLE IF NOT EXISTS projects (
  project_id TEXT PRIMARY KEY,
  team_id TEXT,
  name TEXT,
  project_type TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE IF NOT EXISTS sections (
  section_id TEXT PRIMARY KEY,
  project_id TEXT,
  name TEXT,
  position INTEGER,
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS team_memberships (
  team_id TEXT,
  user_id TEXT,
  PRIMARY KEY (team_id, user_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS comments (
  comment_id TEXT PRIMARY KEY,
  task_id TEXT,
  user_id TEXT,
  content TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (task_id) REFERENCES tasks(task_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS tasks (
  task_id TEXT PRIMARY KEY,
  project_id TEXT,
  section_id TEXT,
  parent_task_id TEXT,
  name TEXT,
  completed BOOLEAN,
  created_at TIMESTAMP,
  completed_at TIMESTAMP,
  FOREIGN KEY (project_id) REFERENCES projects(project_id),
  FOREIGN KEY (section_id) REFERENCES sections(section_id),
  FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id)
);

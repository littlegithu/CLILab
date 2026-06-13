import json
import os

DATA_FILE = "data/project_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "projects": [], "tasks": []}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: Data file corrupt. Starting fresh.")
        return {"users": [], "projects": [], "tasks": []}

def save_data(users, projects, tasks):
    data = {
        "users": [{"name": u.name, "email": u.email} for u in users],
        "projects": [{"title": p.title, "description": p.description, "due_date": p.due_date, "tasks": [t.title for t in p.tasks]} for p in projects],
        "tasks": [{"title": t.title, "status": t.status, "assigned_to": t.assigned_to} for t in tasks]
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

#!/usr/bin/env python3
import argparse
import sys
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_handler import load_data, save_data
from utils.helpers import print_projects, print_tasks

users = []
projects = []
tasks = []

def rebuild_from_json():
    global users, projects, tasks
    data = load_data()
    users.clear()
    for u_data in data.get("users", []):
        u = User(u_data["name"], u_data["email"])
        users.append(u)
    projects.clear()
    for p_data in data.get("projects", []):
        p = Project(p_data["title"], p_data["description"], p_data["due_date"])
        projects.append(p)
    tasks.clear()
    for t_data in data.get("tasks", []):
        t = Task(t_data["title"], t_data["assigned_to"])
        t.status = t_data["status"]
        tasks.append(t)

def save_all():
    save_data(users, projects, tasks)

def find_user(name):
    for u in users:
        if u.name == name:
            return u
    return None

def find_project(title):
    for p in projects:
        if p.title == title:
            return p
    return None

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_add_user = subparsers.add_parser("add-user", help="Add a new user")
    p_add_user.add_argument("--name", required=True)
    p_add_user.add_argument("--email", required=True)

    p_add_proj = subparsers.add_parser("add-project", help="Add a project to a user")
    p_add_proj.add_argument("--user", required=True)
    p_add_proj.add_argument("--title", required=True)
    p_add_proj.add_argument("--desc", default="")
    p_add_proj.add_argument("--due", required=True)

    p_add_task = subparsers.add_parser("add-task", help="Add a task to a project")
    p_add_task.add_argument("--project", required=True)
    p_add_task.add_argument("--title", required=True)
    p_add_task.add_argument("--assignee", required=True)

    p_list_proj = subparsers.add_parser("list-projects", help="List all projects for a user")
    p_list_proj.add_argument("--user", required=True)

    p_list_tasks = subparsers.add_parser("list-tasks", help="List tasks for a project")
    p_list_tasks.add_argument("--project", required=True)

    p_complete = subparsers.add_parser("complete-task", help="Mark a task complete")
    p_complete.add_argument("--project", required=True)
    p_complete.add_argument("--title", required=True)

    args = parser.parse_args()
    rebuild_from_json()

    if args.command == "add-user":
        try:
            u = User(args.name, args.email)
            users.append(u)
            save_all()
            print(f"User '{args.name}' added.")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif args.command == "add-project":
        user = find_user(args.user)
        if not user:
            print(f"Error: User '{args.user}' not found.")
            sys.exit(1)
        p = Project(args.title, args.desc, args.due)
        projects.append(p)
        user.projects.append(p)
        save_all()
        print(f"Project '{args.title}' added to user '{args.user}'.")

    elif args.command == "add-task":
        project = find_project(args.project)
        if not project:
            print(f"Error: Project '{args.project}' not found.")
            sys.exit(1)
        task = Task(args.title, args.assignee)
        tasks.append(task)
        project.add_task(task)
        save_all()
        print(f"Task '{args.title}' added to project '{args.project}'.")

    elif args.command == "list-projects":
        user = find_user(args.user)
        if not user:
            print(f"Error: User '{args.user}' not found.")
            sys.exit(1)
        print_projects(user.projects)

    elif args.command == "list-tasks":
        project = find_project(args.project)
        if not project:
            print(f"Error: Project '{args.project}' not found.")
            sys.exit(1)
        print_tasks(project.tasks)

    elif args.command == "complete-task":
        project = find_project(args.project)
        if not project:
            print(f"Error: Project '{args.project}' not found.")
            sys.exit(1)
        for task in project.tasks:
            if task.title == args.title:
                task.mark_complete()
                save_all()
                print(f"Task '{args.title}' marked complete.")
                break
        else:
            print(f"Error: Task '{args.title}' not found in project '{args.project}'.")

if __name__ == "__main__":
    main()

# 📋 Project Management CLI Tool

A command-line application to manage users, projects, and tasks with persistent JSON storage. Built for the Python Summative Lab assignment.

## Features

- **User management** – add and store users  
- **Project tracking** – assign projects to users with descriptions and due dates  
- **Task management** – add tasks to projects, assign owners, mark as complete  
- **Persistent storage** – all data saved to `data/project_data.json` automatically  
- **Beautiful CLI tables** – uses `rich` library for readable output  
- **Error handling** – friendly messages for missing users, projects, or tasks  
- **Unit tests** – included and passing  

## Quick Start

### Prerequisites
- Python 3.10 or higher  
- `pip` package manager  

### Installation

```bash
pip install -r requirements.txt

class Task:
    def __init__(self, title, assigned_to):
        self.title = title
        self.assigned_to = assigned_to
        self.status = "pending"

    def mark_complete(self):
        self.status = "complete"

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status}, assigned_to={self.assigned_to})"

import unittest
from models.project import Project
from models.task import Task

class TestProject(unittest.TestCase):
    def test_create_project(self):
        p = Project("MyApp", "A great app", "2025-12-31")
        self.assertEqual(p.title, "MyApp")
        self.assertEqual(p.description, "A great app")
        self.assertEqual(p.due_date, "2025-12-31")
        self.assertEqual(len(p.tasks), 0)

    def test_add_task(self):
        p = Project("MyApp", "Desc", "2025-12-31")
        t = Task("Fix bug", "Alice")
        p.add_task(t)
        self.assertIn(t, p.tasks)

if __name__ == "__main__":
    unittest.main()

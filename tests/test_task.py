import unittest
from models.task import Task

class TestTask(unittest.TestCase):
    def test_create_task(self):
        t = Task("Write code", "Alice")
        self.assertEqual(t.title, "Write code")
        self.assertEqual(t.assigned_to, "Alice")
        self.assertEqual(t.status, "pending")

    def test_mark_complete(self):
        t = Task("Test", "Bob")
        t.mark_complete()
        self.assertEqual(t.status, "complete")

if __name__ == "__main__":
    unittest.main()

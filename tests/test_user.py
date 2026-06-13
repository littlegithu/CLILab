import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        u = User("Alice", "alice@example.com")
        self.assertEqual(u.name, "Alice")
        self.assertEqual(u.email, "alice@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User("Bob", "bademail")
        with self.assertRaises(ValueError):
            User("Bob", "bob@domain")

    def test_repr(self):
        u = User("Charlie", "charlie@test.com")
        self.assertIn("Charlie", repr(u))
        self.assertIn("charlie@test.com", repr(u))

if __name__ == "__main__":
    unittest.main()

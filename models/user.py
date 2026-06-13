class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class User(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.projects = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Invalid email address")
        self._email = value

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"

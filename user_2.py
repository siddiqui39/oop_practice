
from datetime import datetime
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self._password = password

    @property
    def email(self):
        return self._email

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email

    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email

    def get_password(self):
        print(f"Password accessed at {datetime.now()}")
        return self._password

    def set_password(self, new_password):
        self._password = new_password



user1 = User("Dan", " dan@gmail.com", "122")

user1.set_email("danny@outlook.com")
print(user1.get_email())
print(user1.get_password())


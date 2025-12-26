#Accessing and modifying data:
#1. The traditional way: make the data private and use getters and setters:

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()


user1 = User("Dan", " dAn@gmail.com", "122")
user2 = User("batman", "batman@gmail.com", "abc")

print(user1.clean_email())







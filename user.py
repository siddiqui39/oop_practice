#Accessing and modifying data:
#1. The traditional way: make the data private and use getters and setters:
# name mangled (__email)
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email     #__email will be private. _email will be protected
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()


user1 = User("Dan", " dAn@gmail.com", "122")
user2 = User("batman", "batman@gmail.com", "abc")

print(user1.clean_email())

# the consenting adults philosophy







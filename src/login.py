
class LoginSystem:

    def __init__(self):
        self.users = {
            "admin": "Password123",
            "tester": "Test123"
        }

        self.failed_attempts = {}
        self.locked_users = set()

    def login(self, username, password):

        if not username or not password:
            return "Username and password required"

        if username in self.locked_users:
            return "Account locked"

        if username not in self.users:
            return "Invalid username or password"

        if self.users[username] != password:
            attempts = self.failed_attempts.get(username, 0) + 1
            self.failed_attempts[username] = attempts

            if attempts >= 2:
                self.locked_users.add(username)
                return "Account locked"

            return "Invalid username or password"

        self.failed_attempts[username] = 0
        return "Login successful"

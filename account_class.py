import json
import bcrypt

class Account():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.failed_attempts = 0

    def create_account(self, username, password, account_manager=None):
        try:
            with open('password.txt', 'r') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

        data[username] = {"Password": hashed}

        with open('password.txt', 'w') as f:
            json.dump(data, f, indent=4)

        if account_manager is not None:
            account_manager.add_account(self)

    def login(self, username):
        try:
            with open('password.txt', 'r') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("No account data found.")
            return

        if username not in data:
            print("Invalid Username.")
            return

        stored_hash = data[username]["Password"]

        while self.failed_attempts < 5:
            password_entry = input("Enter the password: ")

            if bcrypt.checkpw(password_entry.encode('utf-8'), stored_hash.encode('utf-8')):
                print("Access Granted!")
                self.failed_attempts = 0
                return
            else:
                self.failed_attempts += 1
                remaining = 5 - self.failed_attempts
                if remaining == 0:
                    print("Too many failed attempts. Account locked.")
                else:
                    print(f"Invalid Password. Attempts left: {remaining}")
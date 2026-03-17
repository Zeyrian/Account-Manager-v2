from account_class import Account

class Account_Manager():
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account):
        username = account.username
        if username not in self.accounts:
            self.accounts[username] = account
            print(f"Account '{username}' successfully registered.")

    def fetch_account(self, username):
        if username not in self.accounts:
            print("Invalid username.")
            return None
        return self.accounts[username]
from account_manager import Account_Manager
from account_class import Account
import json

account_manager = Account_Manager()

def check_password_strength(password: str) -> int:
    score = 100

    with open('common_passwords.txt', 'r') as f:
        next(f)
        common = {line.split('\t')[1].strip() for line in f if '\t' in line}

    if password in common:
        score -= 50
    if password.isalpha() or password.isnumeric():
        score -= 40
    elif password.isalnum():
        score -= 20

    return score

def init_account_setup():
    try:
        with open('password.txt', 'r') as f:
            existing = json.load(f)
        taken_usernames = set(existing.keys())
    except (json.JSONDecodeError, FileNotFoundError):
        taken_usernames = set(existing.keys())

    while True:
        username_input = input("Enter a username (at least 5 characters): ")
        if len(username_input) < 5:
            print("Invalid username: too short.")
            continue
        if username_input in taken_usernames:
            print("Username is already taken.")
            continue

        password_input = input("Enter a strong password (at least 12 characters): ")
        if password_input == "":
            return
        if len(password_input) < 12:
            print("Password is too short.")
            continue
        if check_password_strength(password_input) <= 50:
            print("Password is too weak. Please choose a stronger one.")
            continue

        account = Account(username_input, password_input)
        account.create_account(username_input, password_input, account_manager)
        return

def init_login():
    username_input = input("Enter your username: ")
    account = Account(username_input, "")
    account.login(username_input)

while True:
    print("\n=== XYZ Login Page ===")
    print("1. Log In")
    print("2. Create Account")
    print("Q. Exit")
    init_input = input("Enter your input: ")

    if init_input.lower() == "q":
        break
    elif init_input == "1":
        init_login()
    elif init_input == "2":
        init_account_setup()
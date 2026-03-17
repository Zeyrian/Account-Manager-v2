# 🔐 Account Manager v2

An upgraded version of [Simple Account Manager](#) — adding bcrypt password hashing, persistent JSON storage, and a password strength enforcement system.

---

## 🖥️ Features

- User creation and login with bcrypt-hashed passwords
- Accounts persist across sessions via JSON storage
- Password strength checker — enforces length, character variety, and screens against a common password list
- Account lockout after 5 consecutive failed login attempts
- Class-based structure: `Account` and `Account_Manager` classes

## ⚙️ Technologies

- Python 3
- [`bcrypt`](https://pypi.org/project/bcrypt/) — password hashing
- `json` (standard library) — persistent credential storage
- OOP — modular class design

---

## 💾 How the Security Works

### bcrypt Hashing
Passwords are run through `bcrypt.hashpw()` with a unique salt before anything is written to disk. On login, `bcrypt.checkpw()` handles comparison — the original password is never reconstructed or stored.

### 💎 Password Strength Scoring
Passwords are scored out of 100 at registration. Points are deducted based on:

| Condition | Penalty |
|---|---|
| Found in common password list | −50 |
| All letters or all numbers | −40 |
| Letters and numbers only (no symbols) | −20 |

Passwords scoring **50 or below** are rejected. Minimum length is **12 characters**.

### ⛔ Account Lockout
Failed attempts are tracked on the `Account` object. After **5 failed attempts**, the session locks — no further attempts are accepted.

---

## 📁 Project Structure

```
account-manager-v2/
├── main.py               # Entry point, menu loop and input handling
├── account_class.py      # Account class, creation, login and hashing
├── account_manager.py    # Account_Manager class, account registry
├── common_passwords.txt  # Reference list for common password detection
└── password.txt          # Auto-generated, stores hashed credentials
```

## 📝 Setup

```bash
pip install bcrypt
python main.py
```

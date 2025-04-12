import json

class UserManager:
    def __init__(self, storage_file="users.json"):
        self.storage_file = storage_file
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.storage_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or is empty, return an empty dictionary
            return {}

    def save_users(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.users, file, indent=4)

    def register_user(self, username, password, name, email):
        if username in self.users:
            return "Username already exists."
        self.users[username] = {
            "password": password,
            "name": name,
            "email": email,
        }
        self.save_users()
        return "User registered successfully!"

    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            return f"Welcome, {user['name']}!"
        return "Invalid username or password."
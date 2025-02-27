import os

# Hardcoded secret key
SECRET_KEY = "my_super_secret_key"

def connect_to_database():
    # Using hardcoded credentials
    db_user = "admin"
    db_password = "password123"
    # Connect to the database...
    pass

# Example usage (vulnerable to hardcoded secrets)
print(SECRET_KEY)

import hashlib
import os

# Function to create a salt for a user
def generate_salt():
    return os.urandom(16)  # 16 bytes is a common length for salt

# Function to hash a password with a given salt
def hash_password(password, salt):
    # Combine the password and salt, then hash them using SHA-256
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return hashed_password

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import getpass
import os

def create_password():
    password = getpass.getpass("Enter your password: ")
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    with open("password.bin", "wb") as f:
        f.write(salt + key)
    print("Password created")

def login():
    try:
        password = getpass.getpass("Enter your password: ")
        with open("password.bin", "rb") as f:
            data = f.read()
            salt = data[:16]
            key = data[16:]
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,
            backend=default_backend()
        )
        kdf.verify(password.encode(), key)
        print("Login successful")
    except Exception as e:
        print(f"Login failed: {e}")

def reset_password():
    try:
        old_password = getpass.getpass("Enter your old password: ")
        with open("password.bin", "rb") as f:
            data = f.read()
            salt = data[:16]
            key = data[16:]
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,
            backend=default_backend()
        )
        kdf.verify(old_password.encode(), key)
        new_password = getpass.getpass("Enter your new password: ")
        new_salt = os.urandom(16)
        new_kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=new_salt,
            length=32,
            backend=default_backend()
        )
        new_key = new_kdf.derive(new_password.encode())
        with open("password.bin", "wb") as f:
            f.write(new_salt + new_key)
        print("Password reset")
    except Exception as e:
        print(f"Wrong password: {e}")

login()
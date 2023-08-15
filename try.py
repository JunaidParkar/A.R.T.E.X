import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass

PASSWORD_FILE = "passwords.txt"
KEY_FILE = "key.key"
SALT = b'\x17\xd2U9\x08\xc3,\x9b\xf7\xef\x1c\xd7g\xd4\xdeS'

def save_key(key):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
        print("Key saved to key file.")


def generate_key(password, salt):
    password = password.encode()  # Convert password to bytes

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def check_username(username):
    if not os.path.exists(PASSWORD_FILE):
        return False

    with open(PASSWORD_FILE, 'rb') as file:
        for line in file:
            stored_username, _ = line.decode().strip().split(":")
            if stored_username == username:
                return True
    return False

def list_passwords():
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords found.")
        return

    with open(PASSWORD_FILE, 'rb') as file:
        for line in file:
            stored_username, encrypted_password = line.decode().strip().split(":")
            print(f"Username: {stored_username}")
            print(f"Encrypted Password: {encrypted_password}")

def login():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords found.")
        return

    with open(PASSWORD_FILE, 'rb') as file:
        for line in file:
            stored_username, encrypted_password = line.decode().strip().split(":")
            if stored_username == username:
                cipher_suite = Fernet(key)
                decrypted_password = cipher_suite.decrypt(encrypted_password)
                if decrypted_password == password:
                    print("Login successful!")
                    return
            print("Login failed.")

def reset_password():
    username = input("Enter your username: ")
    old_password = getpass("Enter your old password: ")
    new_password = getpass("Enter your new password: ")
    
    if not check_username(username):
        print("Username does not exist.")
        return
    
    if old_password == new_password:
        print("New password cannot be the same as the old password.")
        return
    
    with open(PASSWORD_FILE, 'rb') as file:
        for line in file:
            stored_username, encrypted_password = line.decode().strip().split(":")
            if stored_username == username:
                key = generate_key(old_password, SALT)
                cipher_suite = Fernet(key)
                
                new_encrypted_password = cipher_suite.encrypt(new_password.encode())
                
                file.seek(0, 0)
                file.truncate()
                
                for line in file:
                    stored_username, encrypted_password = line.decode().strip().split(":")
                    if stored_username == username:
                        file.write(f"{username}:{new_encrypted_password}\n")
                        break
    
    print("Password reset successfully!")

def create_password():
    try:
        username = input("Enter your username: ")
        password = getpass("Enter your new password: ")
        
        if check_username(username):
            print("Username already exists.")
            return
        
        key = generate_key(password.encode(), SALT)
        cipher_suite = Fernet(key)
        
        encrypted_password = cipher_suite.encrypt(password.encode())
        
        if not os.path.exists(PASSWORD_FILE):
            with open(PASSWORD_FILE, "w") as file:
                pass
        
        with open(PASSWORD_FILE, "ab") as file:
            file.write(f"{username}:{encrypted_password}")
        print("Password created successfully!")
        
        # Save the key to the key file
        save_key(key)
        print("Key saved to key file.")
        
    except Exception as e:
        print(f"Error creating password: {e}")


def main():
    choice = input("Choose an option:\n1. Create Password\n2. Login\n3. List Passwords\n4. Reset Password\n5. Exit\n")

    while choice != "5":
        if choice == "1":
            create_password()
        elif choice == "2":
            login()
        elif choice == "3":
            list_passwords()
        elif choice == "4":
            reset_password()
        else:
            print("Invalid choice.")

        choice = input("Choose an option:\n1. Create Password\n2. Login\n3. List Passwords\n4. Reset Password\n5. Exit\n")

    print("Exiting...")

if __name__ == "__main__":
    main()

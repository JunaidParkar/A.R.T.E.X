from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import getpass
import os
import sys
sys.path.append(os.environ.get('Zubia'))
from Zubia.Brain.Paths import PRIVATE_1, TEMP_FOLDER
from Zubia.Body.Hand import takeInput, printData

pvt = os.path.join(os.path.split(TEMP_FOLDER)[0], "Brain", "Datasets", ".private")

def validateFolder():
    if not os.path.exists(pvt):  # Check if the folder exists and create if not
        os.makedirs(pvt)

def create_password():
    validateFolder()
    password = getpass.getpass("Enter your password: ")
    security_question = takeInput("Enter a security question:")
    security_answer = takeInput("Enter the answer to the security question:")
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    with open(os.path.join(pvt, PRIVATE_1), "wb") as f:
        f.write(salt + key + security_question.encode() + b'\n' + security_answer.encode())
    print("Password created")

def login():
    try:
        validateFolder()
        password = getpass.getpass("Enter your password: ")
        with open(os.path.join(pvt, PRIVATE_1), "rb") as f:
            data = f.read()
            salt = data[:16]
            key = data[16:48]  # Change index to accommodate new data
            security_question = data[48:data.index(b'\n')]
            security_answer = data[data.index(b'\n')+1:]
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
        validateFolder()
        old_password = getpass.getpass("Enter your old password: ")
        with open(os.path.join(pvt, PRIVATE_1), "rb") as f:
            data = f.read()
            salt = data[:16]
            key = data[16:48]  # Change index to accommodate new data
            security_question = data[48:data.index(b'\n')]
            security_answer = data[data.index(b'\n')+1:]
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
        with open(os.path.join(pvt, PRIVATE_1), "wb") as f:
            f.write(new_salt + new_key + security_question + b'\n' + security_answer)
        print("Password reset")
    except Exception as e:
        print(f"Wrong password: {e}")

def forgot_password():
    try:
        validateFolder()
        security_question = input("Enter your security question: ")
        with open(os.path.join(pvt, PRIVATE_1), "rb") as f:
            data = f.read()
            saved_security_question = data[48:data.index(b'\n')]
            saved_security_answer = data[data.index(b'\n')+1:]
        if security_question.encode() == saved_security_question:
            security_answer = input("Enter the answer to your security question: ")
            if security_answer.encode() == saved_security_answer:
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
                with open(os.path.join(pvt, PRIVATE_1), "wb") as f:
                    f.write(new_salt + new_key + saved_security_question + b'\n' + saved_security_answer)
                print("Password reset successful")
            else:
                print("Incorrect security answer")
        else:
            print("Incorrect security question")
    except Exception as e:
        print(f"Password reset failed: {e}")

def printOptions():
    print("Authentication")
    print("1. Create password")
    print("2. Log In")
    print("3. Reset password")
    print("4. Forgot password")
    print("5. Exit")

def Authenticate():
    printOptions()
    while True:
        try:
            choice = int(takeInput("Enter corresponding number...").strip())
            if choice == 1:
                create_password()
            elif choice == 2:
                login()
            elif choice == 3:
                reset_password()
            elif choice == 4:
                forgot_password()
            elif choice == 5:
                break
            else:
                printData("Invalid choice. Please enter a valid number.\n")
                printOptions()
        except ValueError:
            printData("Please enter only a number\n")
            printOptions()

Authenticate()

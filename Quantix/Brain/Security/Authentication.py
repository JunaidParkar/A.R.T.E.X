from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import getpass
import os
import sys
import subprocess
sys.path.append(os.environ.get('Quantix'))
from Quantix.Brain.Paths import TEMP_FOLDER, PRIVATE_1, PRIVATE_2, PRIVATE_3
from Quantix.Body.Hand import takeInput, printSimple
from Quantix.Body.Mouth import speak

pvt = os.path.join(os.path.split(TEMP_FOLDER)[0], "Brain", "Datasets", ".private")

def validateFolder():
    if not os.path.exists(pvt):
        os.makedirs(pvt)
        subprocess.run(f"attrib +h {pvt}", shell=True, check=True)

def deriveKey(salt, data):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
        )
    return kdf.derive(data.encode())

def verifyKey(salt, data, input):
    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,
            backend=default_backend()
            )
        kdf.verify(input.encode(), data)
        return True
    except Exception as e:
        return f"{e}"

def create_password():
    try:
        speak("Create Password here...")
        password = getpass.getpass("Create your password: ")
        password2 = getpass.getpass("Conform your password: ")
        if password == password2:
            security_question = takeInput("Enter a security question:")
            security_answer = takeInput("Enter the answer to the security question:")
            salt = os.urandom(16)
            passwordKey = deriveKey(salt, password)
            quesKey = deriveKey(salt, security_question)
            ansKey = deriveKey(salt, security_answer)
            files = [PRIVATE_1, PRIVATE_2, PRIVATE_3]
            data = [passwordKey, quesKey, ansKey]
            for index, file in enumerate(files):
                with open(os.path.join(pvt, file), "wb") as f:
                    f.write(salt + data[index])
                    f.close()
            return True
        else:
            return "Password does not match..."
    except Exception as e:
        return e

def login(pd: str=None):
    try:
        validateFolder()
        speak("Please login here...")
        if pd is None:
            password = getpass.getpass("Enter your password: ")
        else:
            password = pd
        with open(os.path.join(pvt, PRIVATE_1), "rb") as f:
            data = f.read()
            salt = data[:16]
            key = data[16:48]
        verifiedLogin = verifyKey(salt, key, password)
        if verifiedLogin is True:
            return True
        else:
            return verifiedLogin
    except Exception as e:
        return e

def reset_password():
    try:
        validateFolder()
        speak("Reset you password here...")
        old_password = getpass.getpass("Enter your old password: ")
        with open(os.path.join(pvt, PRIVATE_1), "rb") as f:
            data = f.read()
            salt = data[:16]
            key = data[16:48]
        oldPasswordVerified = verifyKey(salt, key, old_password)
        if oldPasswordVerified is True:
            new_password = getpass.getpass("Enter your new password: ")
            new_salt = os.urandom(16)
            new_key = deriveKey(new_salt, new_password)
            with open(os.path.join(pvt, PRIVATE_1), "wb") as f:
                f.write(new_salt + new_key)
            return True
        else:
            return oldPasswordVerified
    except Exception as e:
        return e

def forgot_password():
    try:
        validateFolder()
        speak("Recover your password here...")
        security_question = takeInput("Enter your security question: ")
        security_answer = takeInput("Enter the answer to your security question: ")
        with open(os.path.join(pvt, PRIVATE_2), "rb") as f:
            data = f.read()
            salt = data[:16]
            saved_security_question = data[16:48]
            questVerified = verifyKey(salt, saved_security_question, security_question)
            if not questVerified is True:
                return questVerified
        with open(os.path.join(pvt, PRIVATE_3), "rb") as f:
            data = f.read()
            salt = data[:16]
            saved_security_answer = data[16:48]
            answerVerified = verifyKey(salt, saved_security_answer, security_answer)
            if not answerVerified is True:
                return answerVerified
        speak("You need to reset your security answer and question during the process ahead. You have been proceed to set password...")
        crt = create_password()
        if crt is True:
            return True
        else:
            return crt
    except Exception as e:
        return e

def isPasswordSet():
    fp = os.path.join(pvt, PRIVATE_1)
    fq = os.path.join(pvt, PRIVATE_2)
    fa = os.path.join(pvt, PRIVATE_3)
    if not os.path.isfile(fp):
        return "Password not set"
    elif not os.path.isfile(fq) or not os.path.isfile(fa):
        return "Something wrong with security system. Kindly Reset your password."
    return True

def getOptions():
    return ["Create password", "Log in", "Reset password", "Forgot password", "Exit"]

def printOptions():
    options = getOptions()
    pws = isPasswordSet()
    if pws is True:
        opt = [options[1], options[2], options[3], options[4]]
    else:
        opt = [options[0]]
    
    if len(opt) == 1 and opt[0] == options[0]:
        return "crt"
    else:
        printSimple("Authentication")
        for index, option in enumerate(opt):
            print(f"   {index + 1}: {option}")
    return opt

def Authenticate():
    validateFolder()
    options = getOptions()
    opt = printOptions()
    while True:
        try:
            if opt == "crt":
                create = create_password()
                if create is True:
                    speak("Successfully created your password. Now you can login")
                    logIn = login()
                    return logIn
                else:
                    return create
            speak("Please authenticate yourself...")
            choice = int(takeInput(f"Enter only corresponding number. Eg: 1 for {opt[0]}"))
            if choice <= len(opt):
                action = opt[choice - 1]
                if action == options[0]:
                    create = create_password()
                    if create is True:
                        speak("Successfully created your password. Now you can login")
                        logIn = login()
                        return logIn
                    else:
                        return create
                elif action == options[1]:
                    logIn = login()
                    return logIn
                elif action == options[2]:
                    reset = reset_password()
                    if reset is True:
                        speak("Password successfully reset. Please login again")
                        logIn = login()
                        return login
                    else:
                        return reset
                elif action == options[3]:
                    forgot = forgot_password()
                    return forgot
                elif action == options[4]:
                    return "Exit"
            else:
                speak("Enter appropriate option number.")
        except Exception as e:
            speak(f"Please enter option number {e}")
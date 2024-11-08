from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Generate a key and store it securely
# key = generate_key()
# with open('key.enc', 'wb') as key_file:
#     key_file.write(key)

# Encrypt the image file
# encrypt_file('temp/logo.png', key)

# from cryptography.fernet import Fernet
import tempfile
# import eel

def load_key():
    with open('key.enc', 'rb') as key_file:
        return key_file.read()

def decrypt_file(encrypted_file_path, key):
    fernet = Fernet(key)
    with open(encrypted_file_path, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_file.write(decrypted)
    temp_file.close()
    return temp_file.name

# Load the encryption key
key = load_key()

# Decrypt the image file at runtime
image_path = decrypt_file('temp/logo.png.enc', key)
print(image_path)

# Eel initialization
# eel.init('web')

# Example function to load images in the web app
# @eel.expose
# def get_image_path():
#     return image_path

# Start the Eel application
# eel.start('index.html', size=(800, 600))

# Clean up the temporary file on exit
import atexit
import os

def cleanup():
    os.remove(image_path)

# atexit.register(cleanup)

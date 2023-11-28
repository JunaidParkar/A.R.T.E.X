import pickle

def encrypt_data(data, key):
    encrypted_data = bytearray()
    for byte in data:
        encrypted_data.append(byte ^ key)
    return encrypted_data

def decrypt_data(encrypted_data, key):
    decrypted_data = bytearray()
    for byte in encrypted_data:
        decrypted_data.append(byte ^ key)
    return decrypted_data

def write_to_file(file_path, data):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def read_from_file(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def save_encrypted_data(file_path, data, key):
    encrypted_data = encrypt_data(data, key)
    write_to_file(file_path, encrypted_data)

def load_and_decrypt_data(file_path, key, encoding='utf-8'):
    try:
        encrypted_data = read_from_file(file_path)
        decrypted_data = decrypt_data(encrypted_data, key)
        return decrypted_data.decode(encoding)
    except Exception as e:
        print(f"Error: {e}")
        return None

file_path = "Management\Binaries\datas"
secret_key = 42
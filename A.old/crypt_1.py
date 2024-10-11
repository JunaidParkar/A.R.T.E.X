import pickle

# Example data
data = {
    "securityKey": "gujhbkjiue",
    "jwt": "jiojunlkoi",
    "secretKey": "jnkiunhu",
    "email": "niknklof"
}

# File path where binary data will be stored
file_path = 'data.bin'

# Write data to binary file
with open(file_path, 'wb') as f:
    pickle.dump(data, f)

print(f'Data stored in {file_path}')

# Read data from binary file
with open(file_path, 'rb') as f:
    loaded_data = pickle.load(f)

print('Loaded data:', loaded_data)
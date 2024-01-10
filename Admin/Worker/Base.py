import pickle

def write_binary_file(data, filename):
    serialized_data = pickle.dumps(data)

    with open(filename, 'wb') as file:
        file.write(serialized_data)
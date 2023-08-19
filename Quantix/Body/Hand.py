def printData(data):
    print("")
    print(f"Quantix: {data}")

def printSimple(data):
    print("")
    print(data)

def takeInput(label: str):
    printData(label)
    inp =  input(">> ")
    return inp
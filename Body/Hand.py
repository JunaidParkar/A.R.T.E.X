def printData(data: str):
    print("")
    print(f"Evo: {data}")

def printSimple(data: str):
    print("")
    print(data)

def takeInput(label: str = None):
    if label is None:
        printData("Enter your value here...")
    else:
        printData(label)
    inp =  input(">> ")
    return inp
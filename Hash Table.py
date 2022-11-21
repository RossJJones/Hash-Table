HashTable = []
HashLength = 0

def SetupTable(Length):
    global HashTable
    global HashLength
    HashLength = Length
    for i in range(Length):
        HashTable.append(None)

def ConvertToAscii(data):
    Sum = 0
    for char in data:
        Sum = Sum + ord(char)
    return(Sum)

def HashFunction(data):
    global HashLength
    data = ConvertToAscii(data)
    data = data % HashLength
    return(data)

def AddToTable(data):
    global HashTable
    HashValue = HashFunction(data)
    HashTable[HashValue] = data
    PrintTable()
    
def PrintTable():
    global Hashtable
    for i in range(len(HashTable)-1):
        if HashTable[i] != None:
            print("Position: ",i," Data: "+HashTable[i])

SetupTable(10)
Inp = input("What would you like to add to the hash table? Type End to exit.")
while Inp != "End":
    AddToTable(Inp)
    Inp = input("What would you like to add to the hash table? Type End to exit.")

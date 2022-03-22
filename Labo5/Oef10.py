import sys
from Oef9 import createListFromFile

def ZoekInput(bestand,inp):
    list = []
    for i in createListFromFile(bestand):
        list.append(i.split(','))
    try:
        int(inp)
        for i in list:
            if i[0] == inp:
                print(f"{i[1]} {i[2]}")
    except:
        for i in list:
            if i[1] == inp or i[2] == inp:
                print(f"{i[0]}")
    return ""
        
print(ZoekInput(sys.argv[1], sys.argv[2]))
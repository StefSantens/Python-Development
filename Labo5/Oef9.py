import random
import sys

def createListFromFile(bestand):
    try:
        regels= []
        with open(bestand,"r") as mijn_bestand:
            for i in mijn_bestand.readlines():
                if(i.endswith('\n')):
                    i = i[:-1]
                regels.append(i)
            return regels
    except FileNotFoundError:
        return "Bestand bestaat niet"

def createPassword(bestand):
    list = createListFromFile(bestand)
    if(list =="Bestand bestaat niet"):
        return list
    else:
        wachtwoord = ""
    while(len(wachtwoord) < 12):
        temp=list[random.randint(0,len(list)-1)].capitalize()
        if(len(temp)>=3 and len(wachtwoord)+len(temp) <= 15):
            wachtwoord+=temp
        print(wachtwoord)
    return wachtwoord
print(createPassword(sys.argv[1]))
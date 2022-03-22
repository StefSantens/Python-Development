import sys
import re


def MostCommon(bestand):
    replace = {",": " ", "?": " ","!":" ",".":" ",":":" "}
    try:
        with open(bestand,"r") as mijn_bestand:
            regels = mijn_bestand.read().rstrip()
            for re in replace:
                regels = regels.replace(re," ")
            list = regels.split()
        diction = dict.fromkeys(set(list),0)
        for j in list:
            diction[j] +=1
        return max(diction, key=diction.get)
    except FileNotFoundError:
        print("Bestand bestaat niet")
        
print(MostCommon(sys.argv[1]))
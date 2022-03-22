import sys

def CheckDocstring(bestanden):
    list = []
    for bestand in bestanden:
        try:
            with open(bestand,"r") as mijn_bestand:
                list = mijn_bestand.readlines()
                for i in range(len(list)):
                    list[i] = list[i].lstrip().rstrip()
            for i in range(len(list)):
                if(list[i].startswith("def")):
                    if list[i+1].startswith("'''") :
                        print(f"{bestand} {list[i]} docstring aanwezig")
                    else:
                        print(f"{bestand} {list[i]} docstring niet aanwezig")
        except FileNotFoundError:
            print("Bestand bestaat niet")

def convertSysToList():
    lijst = []
    for i in range(1,len(sys.argv)):
        lijst.append(sys.argv[i])
    return lijst
print(convertSysToList())
print(CheckDocstring(convertSysToList()))
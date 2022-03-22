import sys

def DeleteComments(bestand,bestand2):
    try:
        with open(bestand,"r") as mijn_bestand:
            regels = mijn_bestand.readlines()
            for i in range(len(regels)):
                if regels[i].startswith("#"):
                    regels[i] = regels[i][1:]
        with open(bestand2,"w") as mijn_bestand2:
            for i in range(len(regels)):
                mijn_bestand2.write(regels[i])
    except FileNotFoundError:
        print("Bestand bestaat niet")
        
DeleteComments(sys.argv[1],sys.argv[2])
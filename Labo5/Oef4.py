import sys

def NieuwBestand(bestand,bestand2):
    try:
        with open(bestand,"r") as mijn_bestand:
            regels = mijn_bestand.readlines()
        with open(bestand2,"w") as mijn_bestand2:
            for i in range(len(regels)):
                mijn_bestand2.write(f"{i+1}: "+regels[i])
    except FileNotFoundError:
        print("Bestand bestaat niet")
        
NieuwBestand(sys.argv[1],sys.argv[2])
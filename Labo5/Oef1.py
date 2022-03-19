import sys

def head(bestand):
    try:
        with open(bestand,"r") as mijn_bestand:
            regels = mijn_bestand.readlines()
        for regel in regels[:10]:
            print(regel)
    except FileNotFoundError:
        print("Bestand bestaat niet")
        
head(sys.argv[1])
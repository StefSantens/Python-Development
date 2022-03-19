import sys

def tail(bestand):
    try:
        with open(bestand,"r") as mijn_bestand:
            regels = mijn_bestand.readlines()
        for regel in regels[-10:]:
            print(regel)
    except FileNotFoundError:
        print("Bestand bestaat niet")
        
tail(sys.argv[1])
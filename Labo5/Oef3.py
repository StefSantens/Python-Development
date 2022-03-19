import sys

def cat(bestand,bestand2):
    try:
        with open(bestand,"r") as mijn_bestand:
            print(mijn_bestand.read())
        with open(bestand2,"r") as mijn_bestand2:
            print(mijn_bestand2.read()) 
    except FileNotFoundError:
        print("Bestand bestaat niet")
        
cat(sys.argv[1], sys.argv[2])
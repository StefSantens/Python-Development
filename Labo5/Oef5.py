import sys

def FindLongest(bestand):
    langste = ""
    try:
        with open(bestand,"r") as mijn_bestand:
            regels = mijn_bestand.readlines()
        for regel in regels:
            if(len(regel)> len(langste)):
                langste= regel
        print(langste)
    except FileNotFoundError:
        print("Bestand bestaat niet")
        
FindLongest(sys.argv[1])
import sys

def babyNamen(file):
    list = []
    for i in range(1900,2012):
        bestand = f"labo5-datasets/baby_namen/{i}_{file}.txt"
        try:
            with open(bestand,"r") as mijn_bestand:
                for i in mijn_bestand.readlines():
                    if(i.endswith('\n')):
                        i = i[:-1]
                    list.append(i.split(' '))
            dictionary = {list[i][0]: list[i][1] for i in range(0,len(list))}
        except FileNotFoundError:
            return "Bestand bestaat niet"
    return sorted(dictionary, key = dictionary.get, reverse=True)

def babyNamenBoysAndGirls():
    print(babyNamen("BoysNames"))
    print(babyNamen("GirlsNames"))


print(babyNamenBoysAndGirls())
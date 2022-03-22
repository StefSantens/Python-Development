import sys

def babyNamen(file,year):
    list = []
    bestand = f"labo5-datasets/baby_namen/{year}_{file}.txt"
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

def sameNameBoysAndGirls(year):
    boys = babyNamen("BoysNames",year)
    girls = babyNamen("GirlsNames",year)
    for key in boys:
        for keyj in girls:
            if key == keyj:
                print(key)



print(sameNameBoysAndGirls(1900))
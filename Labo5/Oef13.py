import sys

def babyNamen(file,year1, year2):
    list = []
    for i in range(year1,year2):
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

def MostPopularNamesBoysAndGirls(year1, year2):
    if(year1 > year2):
        temp = year1
        year1 = year2
        year2 = temp
    print(babyNamen("BoysNames",year1, year2))
    print(babyNamen("GirlsNames",year1, year2))


print(MostPopularNamesBoysAndGirls(2002, 2007))


import random


def maak_bingokaart():
    dict = {"B":0,"I":0,"N":0,"G":0,"O":0}
    j = 1
    for key,value in dict.items():
        list = []
        for i in range(5):
            waarde = random.randint(1 + (j-1)*15,j*15)
            list.append(waarde)
        j = j+1
        dict[key] = list
    return dict

def print_bingokaart(dict):
    for key, value in dict.items():
        out = ""
        out += f"{key}\t"
        for i in value:
            out += f"{i}\t"
        print(out)
    return
print_bingokaart(maak_bingokaart())


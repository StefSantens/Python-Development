from Oef14 import dagen

def Is_magisch(day, month, year):
    if(day*month == year%100):
        return True
    else:
        return False

lijst = []
for jaar in range(1901,2000):
    for maand in range(1,13):
        for dag in range(1, dagen(maand,jaar)+1):
            if(Is_magisch(dag, maand, jaar)):
                lijst.append(f"{dag}/{maand}/{jaar}")
for i in range(len(lijst)):
    print(lijst[i])

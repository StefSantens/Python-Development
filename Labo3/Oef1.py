from math import sqrt

def hypo(zijdeX,zijdeY):
    return sqrt((zijdeX**2) + (zijdeY**2))
zijdeX = int(input("Geef de lengte van de eerste zijde : "))
zijdeY = int(input("Geef de lengte van de eerste zijde : "))

print(hypo(zijdeX,zijdeY))
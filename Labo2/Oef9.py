import random
GROEN = [0, 37]
ROOD = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
rad = random.randint(0, 38)
if(rad == 37):
    print("Balletje is beland op vakje 00")
    print(f"Betaal 00")
    exit()
elif(rad == 0):
    print("Balletje is beland op vakje 0")
    print(f"Betaal 0")
    exit()
else:
    print(f"Balletje is beland op vakje {rad}")
    print(f"Betaal {rad}")
if rad in ROOD:
    print("Betaal rood")
else:
    print("Betaal zwart")
if(rad%2 == 0):
    print("Betaal even")
else:
    print("Betaal oneven")
if rad in range(1,18):
    print("Betaal 1 t.e.m. 18")
else:
    print("Betaal 19 t.e.m. 36")

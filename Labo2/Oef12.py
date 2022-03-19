gemiddelde = 0
i = 0
getal = int(input("Geef getal (0 om te stoppen) : "))
while(getal != 0):
    gemiddelde+=getal
    getal = int(input("Geef getal (0 om te stoppen) : "))
    i+=1
print(gemiddelde/i)
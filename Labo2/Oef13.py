som = 0
volwassenen = 0
peuters = 0
kinderen = 0
senioren = 0
leeftijd = input("Geef leeftijd (blanco om te stoppen) : ")
while(leeftijd != ""):
    leeftijds = int(leeftijd)
    if(leeftijds < 3):
        som+=0
        peuters+=1
    elif(3 <= leeftijds <= 12):
        som+=15
        kinderen+=1
    elif(65 <= leeftijds):
        som+=20
        senioren+=1
    else:
        som+=30
        volwassenen+=1
    leeftijd = input("Geef leeftijd (blanco om te stoppen) : ")
print(f"De totaalprijs is {som}")
print(f"0-3 jaar : €{peuters *0:.2f}\n3-12 jaar : €{kinderen * 15,2:.2f}\nVolwassenen : €{volwassenen * 30:.2f}\nSenioren : €{senioren * 20:.2f}")